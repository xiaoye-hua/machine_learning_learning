# -*- coding: utf-8 -*-
# @File    : LSTM.py
# @Author  : Hua Guo
# @Time    : 2020/3/17 下午8:29
# @Disc    :
import tensorflow as tf
from tensorflow.keras import Model


class LSTM(Model):
    def __init__(self):
        super(LSTM, self).__init__()

    def call(self, inputs, training=None, mask=None):
        pass