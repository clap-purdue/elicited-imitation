# -*- coding: utf-8 -*-
from ei.config import Config
from ei.japanese import JapaneseEI
from ei.chinese import ChineseEI


__all__ = ["ElicitedImitation"]

class ElicitedImitation:
    def __init__(self, config: Config):
        self.config = config
        self.language_handler = self.get_language()

    def get_language(self):
        language_map = {
            'ja': JapaneseEI,
            'ch': ChineseEI
        }
        language_class = language_map.get(self.config.language)
        if not language_class:
            raise ValueError(f"unsupported language code: {self.config.language}")
        return language_class(self.config)

    def perform_elicited_imitation(self):
        return self.language_handler.get_ei_results()
