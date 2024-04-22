# -*- coding: utf-8 -*-
from typing import Text
import os
import pandas as pd
from datasets import Dataset
import MeCab
import torch

from ei.config import Config, Language
from ei.asr import WhisperModel
from ei.metrics import Metrics

__all__ = ["JapaneseEI", "JapaneseUtils"]



class JapaneseEI(Language):
    def __init__(self, config: Config) -> None:
        super().__init__(config)
        self.config = config
        self.device = self.get_device()

    def get_device(self):
        if self.config.device == "cuda":
            device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
            if device:
                print(f"Using {device}")
        elif self.config.device == "mps":
            device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
            if device:
                print(f"Using {device}")
        elif self.config.device is None:
            print("Using cpu")

    def switch_mecab(self, text:str):
        if self.config.mecab == "Owakati":
            return JapaneseUtils.mecab_tagger_owakati(text)
        elif self.config.mecab == "Non-Owakati":
            return JapaneseUtils.mecab_tagger(text)
        else:
            self.config.mecab is None
            return JapaneseUtils.mecab_tagger_owakati(text)

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
        dataset = pd.read_csv(os.path.join(self.config.audio_data_path, self.config.transcript_file))
        dataset["path"] = self.config.audio_data_path + "/" + dataset["audio"]
        hf_dataset = Dataset.from_pandas(dataset)
        return hf_dataset
    
    def mecab_processing(self, batch):
        """
        This method removes punctuation and processes text using MeCab tagger.
        """
        gold = JapaneseUtils.clean_text(batch['gold'])
        batch['gold'] = gold
        batch["mecab_gold"] = self.switch_mecab(batch['gold']).strip()
        batch["mecab_gold_morphemes"] = batch["mecab_gold"].count(' ') 
        return batch
    
    def apply_mecab(self) -> Dataset:
        """
        Dataset({
            features: ['audio', 'gold', 'morphemes', 'score', 'path', 'mecab_gold', 'mecab_gold_morphemes'],
            num_rows: 25
        })
            """
        return self.read_custom_data().map(self.mecab_processing)
    
    def asr_transcriptions(self, batch):
        """
        This method uses a whisper checkpoint and a language id to get the transcriptions for audio files.
        """
        model = WhisperModel(self.config.asr_checkpoint, self.config.language, self.device)
        audio = batch['path']
        transcription = model.transcribe(audio).strip()
        transcription = JapaneseUtils.clean_text(transcription)
        batch['student_transcript'] = self.switch_mecab(transcription).strip()
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
    

    def ei_results(self, batch):
        source = batch['mecab_gold']
        target = batch['student_transcript']
        if self.config.metric == "needlemanwunsch":
            score = Metrics.needleman_wunsch(source, target)
            batch['accuracy'] = score
            return batch
        elif self.config.metric == "smithwaterman":
            score = Metrics.smith_waterman(source, target)
            batch['accuracy'] = score
        elif self.config.metric == "editdistance":
            score = Metrics.edit_distance(source, target)
            batch['accuracy'] = score
            return batch
    
    def get_ei_results(self) -> Dataset:
        res = self.apply_asr_transcriptions().map(self.ei_results)
        return res
        


class JapaneseUtils:
    """
    `JapaneseUtils` contains methods for tagging and cleaning japanese.
    """
    @staticmethod
    def mecab_tagger_owakati(text: Text) -> Text:
        mecab = MeCab.Tagger("-Owakati")
        return mecab.parse(text)

    @staticmethod
    def clean_text(text: Text) -> Text:
        japanese_punctuation = "、。！？「」『』（）｛｝［］【】〈〉《》〔〕…‥・"
        cleaned_text = ''.join(char for char in text if char not in japanese_punctuation)
        return cleaned_text
    
    @staticmethod
    def mecab_tagger(text: Text) -> Text:
        mecab = MeCab.Tagger()
        t = mecab.parse(text)
        lines = t.split("\n")
        retst = ""
        for line in lines:
            items = line.split("\t")
            if len(items)>2:
                retst += items[1] + " "
        return retst