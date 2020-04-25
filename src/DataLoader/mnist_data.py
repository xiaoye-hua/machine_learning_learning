# -*- coding: utf-8 -*-
# @File    : mnist_data.py
# @Author  : Hua Guo
# @Time    : 2020/4/25 上午11:14
# @Disc    :
from tensorflow.examples.tutorials.mnist import input_data


def get_mnist_data(debug: bool) -> tuple:
    if debug:
        total_batch = 10
        batch_size = 2
    else:
        batch_size = 100
    mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)
    if not debug:
        total_batch = int(mnist.train.num_examples / batch_size)
    return mnist, total_batch, batch_size



