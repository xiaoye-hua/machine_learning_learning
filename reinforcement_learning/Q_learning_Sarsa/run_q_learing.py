#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/3 2:45 下午
# @Author  : guohua08
# @File    : run_q_learing.py
# On-policy Q learning
import numpy as np
from Q_learning_Sarsa.maze_env import Maze
from Q_learning_Sarsa.RL_brain.QLearningRL_brain import QLearningTable


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
            observation = observation_
            if done:
                print(f"Episode: {episode}; total steps: {step}; reward: {reward}")
                break
    print("Game Over")
    env.destroy()

if __name__ == "__main__":
    """
    on-policy Q learing
    """
    np.random.seed(2)
    env = Maze()
    RL_brain = QLearningTable(actions=list(range(env.n_actions)))
    env.after(100, update)
    env.mainloop()