# -*- coding: utf-8 -*-
from dataclasses import dataclass


@dataclass
class Config:
    def __init__(self, path=None, tsv_file=None, checkpoint=None, language=None, save_dir=None,  **kwargs):
        self.path = path
        self.tsv_file = tsv_file
        self.checkpoint = checkpoint
        self.language = language
        self.save_dir = save_dir

    @classmethod
    def from_dict(cls, config_dict, return_unused_kwargs, **kwargs):
    
        config = cls(**config_dict)

        to_remove = []
        for key, value in kwargs.items():
            if hasattr(config, key):
                setattr(config, key, value)
                to_remove.append(key)
        for key in to_remove:
            kwargs.pop(key, None)

        if return_unused_kwargs:
            return config, kwargs
        else:
            return config
