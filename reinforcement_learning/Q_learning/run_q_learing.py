#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/3 2:45 下午
# @Author  : guohua08
# @File    : run_q_learing.py
import numpy as np
from Q_learning.maze_env import Maze
from Q_learning.RL_brain import QLearningTable

def update():
    for episode in range(100):
        observation = env.reset()
        step = 0
        while True:
            env.render()
            step += 1
            action = RL_brain.take_action(str(observation))
            observation_, reward, done = env.step(action)
            RL_brain.learn(str(observation), action, str(observation_), reward)
            if done:
                print(f"Episode: {episode}; total steps: {step}; reward: {reward}")
                break
    print("Game Over")

if __name__ == "__main__":
    np.random.seed(2)
    env = Maze()
    RL_brain = QLearningTable(list(range(env.n_actions)))
    env.after(100, update)
    env.mainloop()