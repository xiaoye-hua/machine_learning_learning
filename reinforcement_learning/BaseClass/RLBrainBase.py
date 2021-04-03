#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/3 2:50 下午
# @Author  : guohua08
# @File    : RLBrainBase.py
from abc import ABCMeta, abstractmethod


class RLBrainBase(metaclass=ABCMeta):
    """
    Base class for RL_brain
    """
    @abstractmethod
    def take_action(self, observation):
        pass

    @abstractmethod
    def learn(self, **kwargs):
        pass