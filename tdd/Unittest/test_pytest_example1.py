# -*- coding: utf-8 -*-
# @File    : test_pytest_example1.py
# @Author  : Hua Guo
# @Time    : 2020/1/7 下午8:23
# @Disc    :
from src.tdd.tweet_cleaning import select_valid_tweets


def test_tweet_selection(good_and_bad_tweets):
    tweet_selection = select_valid_tweets(good_and_bad_tweets)
    print(tweet_selection)
    assert len(tweet_selection) == 1
    assert isinstance(tweet_selection, list)