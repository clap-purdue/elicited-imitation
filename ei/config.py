# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Any, Dict, Optional

__all__ = ["Config", "Language"]

@dataclass
class Config:
    """
    This Config dataclass stores some arguments.

    config = Config(
        audio_data_path="~/Desktop/japanese", 
        transcript_file="japanese-data.csv", 
        asr_checkpoint="openai/whisper-large-v3", 
        language="ja", 
        save_dir="~/Desktop",
        metric="needlemanwunsch",
        device="cuda"
    )
    """
    audio_data_path: Optional[str] = None
    transcript_file: Optional[str] = None
    asr_checkpoint: Optional[str] = None
    language: Optional[str] = None
    save_dir: Optional[str] = None
    metric: Optional[str] = None
    device: Optional[str] = None

    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any], return_unused_kwargs: bool=False, **kwargs) -> Any:
        
        known_keys = {key: config_dict[key] for key in config_dict if key in cls.__annotations__}
        config = cls(**known_keys)

        unused_kwargs = {key: value for key, value in kwargs.items() if key not in cls.__annotations__}

        for key, value in kwargs.items():
            if key in cls.__annotations__:
                setattr(config, key, value)

        if return_unused_kwargs:
            return config, unused_kwargs
        else:
            return config






class Language:
    """
    Base class for the languages used in the system.
    """
    def __init__(self, config: Config) -> Config:
        self.config = config

    def get_ei_results(self):
        raise NotImplementedError("This method should be overridden by subclasses.")
