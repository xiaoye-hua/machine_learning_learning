#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/3 11:20 下午
# @Author  : guohua08
# @File    : RL_brain.py
import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from BaseClass.RLBrainBase import RLBrainReplayBase

np.random.seed(1)
tf.set_random_seed(1)


class DQN(RLBrainReplayBase):
    def __init__(self,
                 action_num: int,
                 feature_num: int,
                 replace_target_iter=200,
                 batch_size=32,
                 restore_size=200,
                 learning_rate=0.01,
                 reward_decay=0.9,
                 e_greedy=0.9,
                 e_greedy_increase=None
                 ) -> None:
        super(RLBrainReplayBase, self).__init__()
        self.n_action = action_num
        self.n_feature = feature_num
        self.replace_target_iter = replace_target_iter
        self.batch_size = batch_size
        self.restore_size = restore_size
        self.lr = learning_rate
        self.reward_decay = reward_decay
        self.e_greedy_max = e_greedy
        self._build_net()
        # update params of target network
        eval_net_params = tf.get_collection(key="eval_net")
        target_net_params = tf.get_collection(key="target_net")
        self.update_target_net_op = [tf.assign(t, v) for t, v in zip(target_net_params, eval_net_params)]
        self.e_greedy_increase = e_greedy_increase
        self.e_greedy = 0 if e_greedy_increase is not None else self.e_greedy_max

        # [curent_state, action, reward, next_state]  --> [feature_num, 1, 1, feature_num]
        self.restore_memory = np.zeros(shape=(self.restore_size, self.n_feature * 2 + 2))
        # total step to update restore memory
        self.total_step = 0
        # total learn iteration number to update target network
        self.learn_iter_num = 0

        self.sess = tf.Session()
        self.sess.run(tf.global_variables_initializer())
        self.cost_lst = []

    def _build_net(self) -> None:
        self.s = tf.placeholder(name="current_state", shape=[None, self.n_feature], dtype=tf.float32)
        self.q_target = tf.placeholder(name="q_target", shape=[None, self.n_action], dtype=tf.float32)
        self.s_ = tf.placeholder(name="next_state", shape=[None, self.n_feature], dtype=tf.float32)

        # eval network
        with tf.variable_scope("eval_net"):
            collection_names, layer_num, w_init, b_init = ["eval_net", tf.GraphKeys.GLOBAL_VARIABLES], 10, tf.random_normal_initializer(0., 0.3), tf.constant_initializer(0.1)
            with tf.variable_scope("l1"):
                w1 = tf.get_variable(name="w1", shape=(self.n_feature, layer_num), collections=collection_names, initializer=w_init)
                b1 = tf.get_variable(name="b1", shape=(1, layer_num), initializer=b_init, collections=collection_names)
                z1 = tf.nn.relu(tf.matmul(self.s, w1) + b1)
            with tf.variable_scope("l2"):
                w2 = tf.get_variable(name="w2", shape=(layer_num, self.n_action), collections=collection_names, initializer=w_init)
                b2 = tf.get_variable(name="b2", shape=(1, self.n_action), initializer=b_init, collections=collection_names)
                self.q_eval = tf.matmul(z1, w2) + b2
        with tf.variable_scope("loss"):
            self.loss = tf.reduce_mean(self.q_target - self.q_eval)
        with tf.variable_scope("train_op"):
            self._train_op = tf.train.RMSPropOptimizer(self.lr).minimize(self.loss)

        # target network
        # TODO: 放在前面，则神经网络发生变化
        with tf.variable_scope("target_net"):
            collection_names = ["target_net", tf.GraphKeys.GLOBAL_VARIABLES]
            with tf.variable_scope("l1"):
                w1 = tf.get_variable(name="w1", shape=(self.n_feature, layer_num), collections=collection_names, initializer=w_init)
                b1 = tf.get_variable(name="b1", shape=(1, layer_num), initializer=b_init, collections=collection_names)
                z1 = tf.nn.relu(tf.matmul(self.s_, w1) + b1)
            with tf.variable_scope("l2"):
                w2 = tf.get_variable(name="w2", shape=(layer_num, self.n_action), collections=collection_names, initializer=w_init)
                b2 = tf.get_variable(name="b2", shape=(1, self.n_action), initializer=b_init, collections=collection_names)
                self.q_next = tf.matmul(z1, w2) + b2

    # def _build_net(self):
    #     """
    #     q_target = reward + gamma*max(q_next)
    #     """
    #     # ------------------ build evaluate_net ------------------
    #     self.s = tf.placeholder(tf.float32, [None, self.n_features], name='s')  # input
    #     self.q_target = tf.placeholder(tf.float32, [None, self.n_actions], name='Q_target')  # for calculating loss
    #     self.s_ = tf.placeholder(tf.float32, [None, self.n_features], name='s_')    # input
    #     with tf.variable_scope('eval_net'):
    #         # c_names(collections_names) are the collections to store variables
    #         c_names, n_l1, w_initializer, b_initializer = \
    #             ['eval_net_params', tf.GraphKeys.GLOBAL_VARIABLES], 10, \
    #             tf.random_normal_initializer(0., 0.3), tf.constant_initializer(0.1)  # config of layers
    #
    #         # first layer. collections is used later when assign to target net
    #         with tf.variable_scope('l1'):
    #             w1 = tf.get_variable('w1', [self.n_features, n_l1], initializer=w_initializer, collections=c_names)
    #             b1 = tf.get_variable('b1', [1, n_l1], initializer=b_initializer, collections=c_names)
    #             l1 = tf.nn.relu(tf.matmul(self.s, w1) + b1)
    #
    #         # second layer. collections is used later when assign to target net
    #         with tf.variable_scope('l2'):
    #             w2 = tf.get_variable('w2', [n_l1, self.n_actions], initializer=w_initializer, collections=c_names)
    #             b2 = tf.get_variable('b2', [1, self.n_actions], initializer=b_initializer, collections=c_names)
    #             self.q_eval = tf.matmul(l1, w2) + b2
    #
    #     with tf.variable_scope('loss'):
    #         self.loss = tf.reduce_mean(tf.squared_difference(self.q_target, self.q_eval))
    #     with tf.variable_scope('train'):
    #         self._train_op = tf.train.RMSPropOptimizer(self.lr).minimize(self.loss)
    #
    #     # ------------------ build target_net ------------------
    #     with tf.variable_scope('target_net'):
    #         # c_names(collections_names) are the collections to store variables
    #         c_names = ['target_net_params', tf.GraphKeys.GLOBAL_VARIABLES]
    #
    #         # first layer. collections is used later when assign to target net
    #         with tf.variable_scope('l1'):
    #             w1 = tf.get_variable('w1', [self.n_features, n_l1], initializer=w_initializer, collections=c_names)
    #             b1 = tf.get_variable('b1', [1, n_l1], initializer=b_initializer, collections=c_names)
    #             l1 = tf.nn.relu(tf.matmul(self.s_, w1) + b1)
    #
    #         # second layer. collections is used later when assign to target net
    #         with tf.variable_scope('l2'):
    #             w2 = tf.get_variable('w2', [n_l1, self.n_actions], initializer=w_initializer, collections=c_names)
    #             b2 = tf.get_variable('b2', [1, self.n_actions], initializer=b_initializer, collections=c_names)
    #             self.q_next = tf.matmul(l1, w2) + b2

    def take_action(self, observation: np.array) -> int:
        if np.random.random() < self.e_greedy:
            observation = observation[np.newaxis, :]
            pred = self.sess.run(self.q_eval,
                                 feed_dict={self.s:observation}
                                 )
            action = int(np.argmax(pred, axis=1))
        else:
            action = np.random.choice(list(range(self.n_action)))
        return action

    def restore_transition(self, current_state, action, reward, next_state):
        index = self.total_step%self.restore_size
        self.restore_memory[index, :] = np.hstack((current_state, [action], [reward], next_state))
        self.total_step += 1

    def learn(self) -> None:
        # update target net
        if self.learn_iter_num % self.replace_target_iter == 0:
            self.sess.run(self.update_target_net_op)
        self.learn_iter_num += 1
        # sample training data
        if self.total_step>self.restore_size:
            index_array = np.random.choice(self.restore_size, self.batch_size)
        else:
            index_array = np.random.choice(self.total_step, self.batch_size)
        train_data = self.restore_memory[index_array, :]
        try:
            q_pred, q_next = self.sess.run(
                [self.q_eval, self.q_next],
                feed_dict={
                    self.s: train_data[:, :self.n_feature],
                    self.s_: train_data[:, -self.n_feature:]
                }
            )
        except:
            print("hah")
        q_target = q_pred.copy()
        batch_index = list(range(train_data.shape[0]))
        action = train_data[:, self.n_feature].astype("int")
        rewards = train_data[:, self.n_feature + 1]
        q_target[batch_index, action] = rewards + self.reward_decay*np.max(q_next, axis=1)
        _, loss = self.sess.run(
            [self._train_op, self.loss],
            feed_dict={
                self.s: train_data[:, :self.n_feature]
                , self.q_target: q_target
            }
                             )
        self.cost_lst.append(
            loss
        )

        if self.e_greedy_increase is not None and self.e_greedy<self.e_greedy_max:
            self.e_greedy += self.e_greedy_increase

    def plot_cost(self):
        plt.plot(self.cost_lst)
        plt.show()



