# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import torchaudio.transforms as T
from transformers import pipeline, AutoConfig


__all__  = ["AudioReader", "WhisperModel"]


class WhisperModel:
    """
    This class is used to load the model with streamlit using the lang_id
    """

    def __init__(self, model_name: str, language: str, device: str) -> None:
        self.model_name = model_name
        self.language = language
        self.device = device

        self.get_transcription = self.load_model()

    def load_model(self) -> pipeline:
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

    def transcribe(self, audio: str) -> str:
        return self.get_transcription(audio)["text"]
    