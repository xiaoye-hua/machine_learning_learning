# -*- coding: utf-8 -*-
# @File    : ModelBuilder.py
# @Author  : Hua Guo
# @Time    : 2019/12/25 下午9:31
# @Disc    :
from abc import ABCMeta, abstractmethod


class ModelBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_model(self):
        pass