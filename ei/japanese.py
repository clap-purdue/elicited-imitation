# -*- coding: utf-8 -*-
from typing import Text
import os
import pandas as pd
from datasets import Dataset
import MeCab
from ei.asr import WhisperModel
from ei.config import Config
from ei.metrics import NeedlemanWunsch

n = NeedlemanWunsch()


class JapaneseUtils:
    """
    `JapaneseUtils` contains methods for tagging and cleaning japanese.
    """
    @staticmethod
    def mecab_tagger(text: Text) -> Text:
        mecab = MeCab.Tagger("-Owakati")
        return mecab.parse(text)

    @staticmethod
    def clean_text(text: Text) -> Text:
        japanese_punctuation = "、。！？「」『』（）｛｝［］【】〈〉《》〔〕…‥・"
        cleaned_text = ''.join(char for char in text if char not in japanese_punctuation)
        return cleaned_text



class ElicitedImitation(Config):
    def __init__(self, config: Config, *args, **kwargs):
        super().__init__(config)
        self.config = config

    def read_custom_data(self) -> Dataset:
        """
        ei = ElicitedImitation(config)
        ei.read_custom_data()
        reads the dataset and returns a HF dataset as follows:

        Dataset({
            features: ['audio', 'gold', 'morphemes', 'score', 'path'],
            num_rows: 25
        })
        """
        dataset = pd.read_csv(os.path.join(self.config.path, self.config.tsv_file))
        dataset["path"] = self.config.path + "/" + dataset["audio"]
        hf_dataset = Dataset.from_pandas(dataset)
        return hf_dataset
    
    @staticmethod
    def mecab_processing(batch):
        """
        This method removes punctuation and processes text using MeCab tagger.
        """
        gold = JapaneseUtils.clean_text(batch['gold'])
        batch['gold'] = gold
        batch["mecab_gold"] = JapaneseUtils.mecab_tagger(gold).strip()
        batch["mecab_gold_morphemes"] = batch["mecab_gold"].count(' ') 
        return batch
    
    def apply_mecab(self) -> Dataset:
        """
        Dataset({
            features: ['audio', 'gold', 'morphemes', 'score', 'path', 'mecab_gold', 'mecab_gold_morphemes'],
            num_rows: 25
        })
            """
        return self.read_custom_data().map(ElicitedImitation.mecab_processing)
    
    def asr_transcriptions(self, batch):
        """
        This method uses a whisper checkpoint and a language id to get the transcriptions for audio files.
        """
        model = WhisperModel(self.config.checkpoint, self.config.language)
        audio = batch['path']
        transcription = model.transcribe(audio).strip()
        transcription = JapaneseUtils.clean_text(transcription)
        batch['student_transcript'] = JapaneseUtils.mecab_tagger(transcription).strip()
        batch["mecab_student_morphemes"] = batch['student_transcript'].count(' ') 
        return batch
    
    def apply_asr_transcriptions(self) -> Dataset:
        """
        Dataset({
            features: ['audio', 'gold', 'morphemes', 'score', 'path', 'mecab_gold', 'mecab_morphemes', 'student_transcript', 'mecab_student_morphemes'],
            num_rows: 2
        })
        """
        return self.apply_mecab().map(self.asr_transcriptions)
    
    @staticmethod
    def ei_results(batch):
        source = batch['mecab_gold']
        target = batch['student_transcript']
        accuracy, scaled_accuracy, _, _ = n.elicited_imitation(source, target)
        batch['accuracy'] = accuracy
        batch['scaled_accuracy'] = scaled_accuracy
        return batch
    
    def get_ei_results(self) -> Dataset:
        res = self.apply_asr_transcriptions().map(ElicitedImitation.ei_results)
        return res
        

