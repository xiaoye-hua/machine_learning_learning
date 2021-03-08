#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/8 7:23 下午
# @Author  : guohua08
# @File    : run_Cartpole.py

import gym
import matplotlib.pyplot as plt
from reinforcement_learning.policy_gradient.RL_brain import PolicyGradient

total_epsodes = 3000
exp_name = "CartPole-v0"

env = gym.make(exp_name)

print(f"action num: {env.action_space.n}")
print(f"observation shape: {env.observation_space.shape}")

RL_agent = PolicyGradient(
    label_num=env.action_space.n
    , feature_num=env.observation_space.shape[0]
)

running_rewards_list = []
total_steps_lst = []
for eps_num in range(total_epsodes):
    observation = env.reset()
    step = 0
    while True:
        env.render()  #render, show the graph
        action = RL_agent.take_action(observation)
        # action = env.action_space.sample()
        observation_, rewards, done, info = env.step(action=action)
        RL_agent.store(reward=rewards, action=action, observation=observation)
        if done:
            ep_rs_sum = sum(RL_agent.rewards)
            total_steps = len(RL_agent.rewards)
            if step == 0:
                running_rewards = ep_rs_sum
            else:
                running_rewards = 0.01 * running_rewards + 0.99 * ep_rs_sum
            running_rewards_list.append(running_rewards)
            total_steps_lst.append(total_steps)
            print(f"Episode num: {eps_num}; running rewards: {running_rewards}; total step in this episode: {total_steps}")
            RL_agent.learn()
            break
        observation = observation_
# plt.plot(running_rewards_list)  # plot the episode vt
# plt.xlabel('episode steps')
# plt.ylabel('running rewards')
# plt.savefig("running_rewards.png")
#
# plt.plot(total_steps_lst)  # plot the episode vt
# plt.xlabel('episode steps')
# plt.ylabel('running rewards')
# plt.savefig("total_steps.png")

# plt.show()