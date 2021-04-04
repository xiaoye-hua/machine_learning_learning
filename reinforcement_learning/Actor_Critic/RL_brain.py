#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/4 11:27 下午
# @Author  : guohua08
# @File    : RL_brain.py
import tensorflow as tf
import numpy as np
from abc import ABCMeta, abstractmethod


class ActorBase(metaclass=ABCMeta):
    def choose_action(self, **kwargs):
        pass

    def learn(self, **kwargs):
        pass


class DiscreteActor(ActorBase):
    pass


class Continuous(ActorBase):
    pass


class Critic:
    """
    online learning for value function V(s)
    """
    def __init__(self, sess, feature_num, learning_rate=0.01, reward_decay=0.9):
        self.sess = sess
        self.feature_num = feature_num
        self.gamma = reward_decay
        self.lr = learning_rate
        self._build_net()

    def _build_net(self):
        self.s = tf.placeholder(
            name="s"
            , shape=(None, self.feature_num)
            , dtype=tf.float32
        )
        self.s_ = tf.placeholder(
            name="s_"
            , shape=(None, self.feature_num)
            , dtype=tf.float32
        )
        self.reward = tf.placeholder(
            name="reward"
            , shape=None
            , dtype=tf.float32
        )
        self.v_next= tf.placeholder(
            name="v_next"
            , shape=None
            , dtype=tf.float32
        )
        with tf.variable_scope("value_network"):
            l1 = tf.layers.dense(
                inputs=self.s
                , name="l1"
                , units=10
                , kernel_initializer=tf.random_normal_initializer(0., 0.1)
                , bias_initializer=tf.constant_initializer(0.1)
                , activation=tf.nn.relu
            )
            self.exp_v = tf.layers.dense(
                inputs=l1
                , name="exp_v"
                , units=1
                , kernel_initializer=tf.random_normal_initializer(0., 0.1)
                , bias_initializer=tf.constant_initializer(0.1)
                , activation=tf.nn.relu
            )
        with tf.variable_scope("td_error"):
            self.td_error = self.reward + self.gamma * self.v_next - self.exp_v
        with tf.variable_scope("train_op"):
            self.train_op = tf.train.AdamOptimizer(self.lr).minimize(self.td_error)

    def learn(self, current_state, reward, next_state):
        v_next = self.sess.run(
            self.exp_v
            , feed_dict={
                self.s: next_state[np.newaxis, :]
            }
        )
        _, td_error = self.sess.run(
            [self.train_op, self.td_error]
            , feed_dict={
                self.a: current_state[np.newaxis, :]
                , self.reward: reward[np.newaxis, :]
                , self.v_next: v_next
            }
        )
        return td_error
