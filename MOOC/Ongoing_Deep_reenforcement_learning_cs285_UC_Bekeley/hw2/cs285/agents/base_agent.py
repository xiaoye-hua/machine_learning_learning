import numpy as np
import tensorflow as tf


class BaseAgent(object):
    def __init__(self, **kwargs):
        super(BaseAgent, self).__init__(**kwargs)

    def train(self):
        """
        train the agents
        """
        raise NotImplementedError

    def add_to_replay_buffer(self, paths):
        """
        add play record to buffer with ReplayBuffer class
        """
        raise NotImplementedError

    def sample(self, batch_size):
        """
        sample play record from buffer with ReplayBuffer class
        """
        raise NotImplementedError