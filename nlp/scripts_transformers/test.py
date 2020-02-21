# -*- coding: utf-8 -*-
# @File    : test.py
# @Author  : Hua Guo
# @Time    : 2020/2/6 下午3:10
# @Disc    :
import tensorflow_datasets


TFDS_TASK = "sst2"
# print("cifar10....")
# dataset = tensorflow_datasets.load(name='cifar10')
print("ss2...")
data, info = tensorflow_datasets.load(
    # "sst2",
    # data_dir="../../data/nlp/glue",
    # download=False,
    f'glue/{TFDS_TASK}',
    with_info=True,
    # data_dir="/home/guohua/tensorflow_datasets/glue/sst2/1.0.0/"
    # data_dir="../../data/nlp"
)
print(info)