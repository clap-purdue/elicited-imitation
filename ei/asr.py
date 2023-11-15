# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from typing import Text
import torch
import librosa
from transformers import pipeline, AutoConfig
import os
import torchaudio
import torchaudio.functional as T
import numpy as np
import pandas as pd
import torch
from transformers import pipeline, AutoConfig
import os
import MeCab

# from read_data import *


def normalize(text):
    mecab = MeCab.Tagger("-Owakati")
    # text = "日本語の文章を分かち書きしたい。"
    return mecab.parse(text)


def read_data(abs_path, csv_file):
    dataset = pd.read_csv(os.path.join(abs_path, csv_file))
    dataset["path"] = abs_path + "/" + dataset["audio"]
    return dataset


class AudioReader:
    """
    a class that has a static method `read_audio(audio)` that converts speech to `np.ndarray`
    using either `torchaudio` or `librosa`
    """

    @staticmethod
    def read_audio(audio: Text) -> np.ndarray:
        try:
            audio, sampling_rate = torchaudio.load(audio)
            audio = T.resample(audio, sampling_rate, 16_000)[0]
        except:
            audio, _ = librosa.load(audio, sr=16_000)
        return audio


class WhisperModel:
    """
    This class is used to load the model with streamlit using the lang_id
    """

    def __init__(self, model_name: Text, language: Text) -> None:
        self.model_name = model_name
        self.language = language
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

        self.get_transcription = self.load_model()

    def load_model(self):
        # NOTE: using pipe results in conflict with Wav2Vec2CTCTokenizer when using `set_prefix_tokens`, so we use AutoConfig
        config = AutoConfig.from_pretrained(self.model_name)
        whisper_pipe = pipeline(
            "automatic-speech-recognition",
            model=self.model_name,
            config=config,
            device=self.device,
        )  # , use_auth_token=True)
        x = whisper_pipe.tokenizer.set_prefix_tokens(
            language=self.language, task="transcribe"
        )
        whisper_pipe.model.config.forced_decoder_ids = x
        return whisper_pipe

    def transcribe(self, audio: Text):
        t = self.get_transcription(audio)["text"]
        return normalize(t)


# if __name__ == "__main__":

#     audio = "/japanese/sent1.mp3"
#     model_name = "clu-ling/whisper-large-v2-japanese-5k-steps"
#     x = WhisperModel(model_name=model_name, language="ja")
#     xx = x.transcribe(audio)
#     print(xx)
