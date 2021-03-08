# Copyright (c) 2021, Summarizers. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import torch
from typing import Dict
from experiments.lightning_base import LightningBase


class BartForSeq2SeqLM(LightningBase):

    def __init__(self, cfg_path, cfg_name):
        """
        Constructor of BartForSeq2SeqLM

        Args:
            cfg_path (str): parents path
            cfg_name (str): config file name

        """
        super().__init__(**self.load_args(cfg_path, cfg_name))
        from transformers import BartForConditionalGeneration, BartTokenizer

        self.tokenizer = BartTokenizer.from_pretrained(
            "sshleifer/distilbart-xsum-12-3")
        self.model = BartForConditionalGeneration.from_pretrained(
            "sshleifer/distilbart-xsum-12-3")

        if self.precision == 16:
            self.model = self.model.half()

    def training_step(self, batch, batch_idx) -> Dict:
        """Training steps"""
        pass

    @torch.no_grad()
    def validation_step(self, batch, batch_idx) -> Dict:
        """Validation steps"""
        pass