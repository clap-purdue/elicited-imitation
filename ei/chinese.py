# -*- coding: utf-8 -*-
from typing import Text
import os
import pandas as pd
from datasets import Dataset

from ei.config import Config, Language
from ei.asr import WhisperModel
from ei.metrics import Metrics

class ChineseEI(Language):
    def __init__(self, config: Config) -> None:
        super().__init__(config)
        self.config = config
        #self.device = self.get_device()


        