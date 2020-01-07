# -*- coding: utf-8 -*-
# @File    : tweet_cleaning.py
# @Author  : Hua Guo
# @Time    : 2020/1/7 下午8:25
# @Disc    :
import re


def detect_retweet(tweet):
    return tweet.startswith("RT:")


def clean_nonalphanumeric(tweet):
    return re.sub("[^a-zA-Z0-9]", "", tweet)


def detect_empty_tweets(tweet):
    return tweet == ""


def clean_mentions(tweet):
    return re.sub("@[\w]*", "", tweet)


def select_valid_tweets(tweets):
    no_retweets  = [t for t in tweets if not detect_retweet(t)]
    clean_tweets = [clean_nonalphanumeric(clean_mentions(t)) for t in no_retweets]
    valid_tweets = [t for t in clean_tweets if not detect_empty_tweets(t)]
    return valid_tweets