#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/3 11:21 下午
# @Author  : guohua08
# @File    : run_DQN.py
import numpy as np
import matplotlib.pylab as plt

from Deep_Q_Learning.maze_env import Maze
from Deep_Q_Learning.RL_brain import DQN


def update():
    # learn_step_interval = 200
    total_step = 0
    reward_lst = []
    running_reward = -1
    for episode in range(300):
        observation = env.reset()
        step = 0
        action_lst = []
        while True:
            env.render()
            total_step += 1
            step += 1
            action = RL_brain.take_action(observation=observation)
            observation_, reward, done = env.step(action)
            action_lst.append(action)
            RL_brain.restore_transition(
                current_state=observation,
                action=action,
                reward=reward,
                next_state=observation_
            )
            if total_step>200 and total_step%5 == 0:
                RL_brain.learn()
            observation = observation_
            if done:
                running_reward = running_reward * 0.99 + reward * 0.01
                reward_lst.append(running_reward)
                print(f"Episode: {episode}; steps for single episode: {step}; reward: {reward}; running_reward:{running_reward}")
                break
        # print(action_lst)
    print("Game Over")
    env.destroy()
    RL_brain.plot_cost()
    plt.plot(reward_lst)
    plt.show()


if __name__ == "__main__":
    np.random.seed(2)
    env = Maze()
    RL_brain = DQN(
        action_num=len(env.action_space)
        , feature_num=env.n_features
        , learning_rate = 0.01
        , reward_decay = 0.9
        , e_greedy = 0.9
        , replace_target_iter=200
        , restore_size = 2000
    )
    env.after(100, update)
    env.mainloop()
