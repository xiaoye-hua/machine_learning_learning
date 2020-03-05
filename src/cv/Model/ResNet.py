# -*- coding: utf-8 -*-
# @File    : ResNet.py
# @Author  : Hua Guo
# @Time    : 2019/12/25 下午9:56
# @Disc    :
import tensorflow as tf
from tensorflow.keras import (
    layers,
    Model
)

#
# class ResdualBlock(layers):
#     def __call__(self, *args, **kwargs):
#         pass


class ResNet(Model):
    def __init__(self, label_num):
        super(ResNet, self).__init__()
        # self.ResBlock1 = ResdualBlock()
        # self.ResBlock2
        self.cnn = layers.Conv2D(filters=10, kernel_size=(3, 3))
        self.avg_pooling = layers.AveragePooling2D()
        self.dense = layers.Dense(label_num)

    def call(self, inputs, training=None, mask=None):
        # x = self.ResBlock1(inputs)
        x = self.cnn(inputs)
        x = self.avg_pooling(x)
        x = self.dense(x)
        return x


if __name__ == "__main__":
    label_num = 2
    model = ResNet(label_num=label_num)
    print(model.summary())