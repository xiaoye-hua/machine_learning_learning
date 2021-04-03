#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/3 5:00 下午
# @Author  : guohua08
# @File    : SarsaRL_brain.py
from Q_learning_Sarsa.RL_brain.BaseBrainClass import BaseBrainClass


class SarasTable(BaseBrainClass):
    def learn(self, state, action, new_state, reward):
        self._check_state_exist(new_state)
        predict_q = self.q_table.loc[state, action]
        if new_state != "terminal":
            new_action = self.take_action(str(new_state))
            real_q = reward + self.gamma*self.q_table.loc[new_state, new_action]
        else:
            real_q = reward
        self.q_table.loc[state, action] += self.lr*(real_q-predict_q)