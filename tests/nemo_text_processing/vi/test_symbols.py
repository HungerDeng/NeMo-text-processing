# Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
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

import pytest

from nemo_text_processing.text_normalization.normalize import Normalizer

from ..utils import CACHE_DIR


class TestSymbols:
    normalizer = Normalizer(input_case="cased", lang="vi", cache_dir=CACHE_DIR, post_process=True)

    @pytest.mark.parametrize(
        ("written", "spoken"),
        [
            ("😀", "mặt cười toét"),
            ("🕐", "một giờ"),
            ("🕤", "chín giờ ba mươi phút"),
            ("🇻🇳", "cờ Việt Nam"),
            ("🏳‍🌈", "cờ cầu vồng"),
            ("1️⃣", "phím số một"),
            ("👨‍👩‍👦", "gia đình có người đàn ông, người phụ nữ và con trai"),
            ("💯", "một trăm điểm"),
            ("⁻", "dấu trừ trên"),
            ("₥", "một phần nghìn"),
            ("₿", "bitcoin"),
            ("₿100", "một trăm bitcoin"),
            ("100₿", "một trăm bitcoin"),
            ("10₫", "mười đồng"),
            ("10€", "mười ơ rô"),
        ],
    )
    @pytest.mark.run_only_on("CPU")
    @pytest.mark.unit
    def test_normalize(self, written, spoken):
        assert self.normalizer.normalize(written, verbose=False, punct_post_process=False) == spoken
