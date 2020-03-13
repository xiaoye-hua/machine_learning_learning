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


class ConvBlock(Model):
    def __init__(self, filters):
        super(ConvBlock, self).__init__()
        self.c1 = layers.Conv2D(
            filters=filters,
            kernel_size=(3, 3),
            data_format="channels_last",
            strides=[1, 1],
            padding="same",
            # use_bias=False
        )
        self.bn = layers.BatchNormalization()
        self.activation = layers.Activation("relu")

    # def call(self, inputs):
    def call(self, inputs, training=None, mask=None):
        x = self.c1(inputs)
        for layer in [
            self.bn,
            self.activation
        ]:
            x = layer(x)
        return x


class ResidualBlock(Model):
    def __init__(self, filters):
        super(ResidualBlock, self).__init__()
        self.conv1 = layers.Conv2D(
            filters=filters,
            kernel_size=(3, 3),
            data_format="channels_last",
            strides=[1, 1],
            padding="same"
        )
        self.bn1 = layers.BatchNormalization()
        self.activation1 = layers.Activation("relu")
        self.conv2 = layers.Conv2D(
            filters=filters,
            kernel_size=(3, 3),
            data_format="channels_last",
            strides=[1, 1],
            padding="same"
        )
        self.bn2 = layers.BatchNormalization()
        self.activation2 = layers.Activation("relu")

    def call(self, inputs, training=None, mask=None):
        x = self.conv1(inputs)
        for layer in [
            self.bn1,
            self.activation1,
            self.conv2,
            self.bn2
        ]:
            x = layer(x)
        return self.activation2(tf.add(inputs, x))


# class ResNet(Model):
#     def __init__(self, label_num=10, res_block_num=10, conv_filter_num=10):
#         super(ResNet, self).__init__()
#         self.con_block1 = ConvBlock(filters=conv_filter_num)
#         self.res_block_lst = []
#         for _ in range(res_block_num):
#             self.res_block_lst.append(
#                 ResidualBlock(filters=conv_filter_num)
#             )
#         self.con_block2 = ConvBlock(filters=2)
#         self.flat = layers.Flatten()
#         self.dense = layers.Dense(label_num, activation="softmax")
#
#     def call(self, inputs, training=None, mask=None):
#         x = self.con_block1(inputs)
#         for layer in self.res_block_lst:
#             x = layer(x)
#         for layer in [
#             self.con_block2,
#             self.flat,
#             self.dense
#         ]:
#             x = layer(x)
#         return x
class ResNet(Model):
    def __init__(self, label_num, res_block_num, conv_filter_num, channel_num):
        super(ResNet, self).__init__()
        self.channel_num = channel_num
        self.conv1 = layers.Conv2D(
            filters=conv_filter_num,
            kernel_size=(3, 3),
            data_format="channels_last",
            strides=[1, 1],
            padding="same"
        )
        # self.con_block1 = ConvBlock(filters=conv_filter_num)
        # self.res_block_lst = []
        # for _ in range(res_block_num):
        #     self.res_block_lst.append(
        #         ResidualBlock(filters=conv_filter_num)
        #     )
        # self.con_block2 = ConvBlock(filters=2)
        self.flat = layers.Flatten()
        self.dense = layers.Dense(label_num, activation="softmax")

    def call(self, inputs, training=None, mask=None):
        # s_planes = tf.reshape(inputs,[-1, SUIT_NUM, CARD_SET_NUM, self.channel_num])
        x = self.conv1(inputs)
        # for layer in self.res_block_lst:
        #     x = layer(x)
        for layer in [
            # self.con_block2,
            self.flat,
            self.dense
        ]:
            x = layer(x)
        return x


if __name__ == "__main__":
    # conv_block = ConvBlock(filters=10)
    # conv_block(tf.ones(shape=(1, 32, 32, 3)))
    # # print(conv_block.summary())
    #
    # residual_block = ResidualBlock(filters=10)
    # residual_block(tf.ones(shape=(1, 32, 32, 10)))
    # print(residual_block.summary())
    model = ResNet(
        label_num=2,
        res_block_num=5,
        conv_filter_num=10
    )
    model(tf.ones(shape=(1, 32, 32, 10)))
    print(model.summary())
    estimator = tf.keras.estimator.model_to_estimator(
        keras_model=model
    )