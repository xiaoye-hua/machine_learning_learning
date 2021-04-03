#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/3 2:45 下午
# @Author  : guohua08
# @File    : BaseBrainClass.py
import pandas as pd
import numpy as np

from BaseClass.RLBrainBase import RLBrainBase


class BaseBrainClass(RLBrainBase):
    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
        super(RLBrainBase, self).__init__()
        self.actions = actions
        self.lr = learning_rate
        self.gamma = reward_decay
        self.eposilon = e_greedy
        self.q_table = pd.DataFrame(columns=actions)

    def take_action(self, observation):
        self._check_state_exist(observation)
        if np.random.random() < self.eposilon:
            values = self.q_table.loc[observation]
            action = np.random.choice(pd.Series(self.actions)[values == max(values)])
        else:
            action = np.random.choice(self.actions)
        return action

    def learn(self, state, action, new_state, reward):
        pass

    def _check_state_exist(self, state):
        if state not in self.q_table.index:
            self.q_table = self.q_table.append(
                pd.Series(
                    data=[0]*len(self.actions)
                    , index=self.actions
                    , name=state
                )
            )


