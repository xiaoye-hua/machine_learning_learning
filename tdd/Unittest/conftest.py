# -*- coding: utf-8 -*-
# @File    : conftest.py
# @Author  : Hua Guo
# @Time    : 2020/1/7 下午8:32
# @Disc    :
import pytest

@pytest.fixture
def good_and_bad_tweets():
    """
    Covers the following scenarios:
        - Tweet is empty from the start
        - Tweet is empty after cleaning
        - Tweet is useful after cleaning
    """
    sample_tweets = ["",
                     "@Somebody$%&/(",
                     "I will survive"]

    return sample_tweets