# -*- coding: utf-8 -*-
# @File    : ResNet50.py
# @Author  : Hua Guo
# @Time    : 2020/3/8 上午8:26
# @Disc    :
from typing import List
import tensorflow as tf
from tensorflow.keras import layers, Model


class ConvBNActivation(Model):
    """
    conv + batch nomalization + relu
    """
    def __init__(self, filter: int, kernel_size: List[int], padding: str, activation: str) -> None:
        super(ConvBNActivation, self).__init__()
        self.conv = layers.Conv2D(
            filters=filter,
            kernel_size=kernel_size,
            padding=padding
        )
        self.bn = layers.BatchNormalization()
        self.activation = layers.Activation(activation)

    def call(self, inputs, training=None, mask=None):
        x = self.conv(inputs)
        x = self.bn(x)
        x = self.activation(x)
        return x


class IdentityBlock(Model):
    """S
    In the case where the input activation has the same dimension as the output activation
    Structures are as follow:
        3 conv in the main path
        1 identity in the shortcut path
    """
    def __init__(self, kernel_size: int, filters: List[int]) -> None:
        super(IdentityBlock, self).__init__()
        f1, f2, f3 = filters

        self.conv2 = layers


class ConvBlock(Model):
    """
    In the case where the dimension of the the input activation is different from that of the output activation
    Structures are as follow:
        3 conv in the main path
        1 conv in the shortcut path
    """
    def __init__(self):
        super(ConvBlock, self).__init__()


class ResNet50(Model):
    """
    Residual NN with 50 layers
    Structures stages are as follow:
        1. conv + bn + Relu + max pooling
        2. Convblock + IdentityBlock*2
        3. Convblock + IdentityBlock*2
        4, Convblock + IdentityBlock*5
        5, Convblock + IdentityBlock*2
        6. avg pooling + flatten + fc
    """
    def __init__(self):
        super(ResNet50, self).__init__()


if __name__ == "__main__":
    con_bn_activation = ConvBNActivation(
        filter=10,
        kernel_size=[3, 3],
        padding="valid",
        activation="relu"
    )
    con_bn_activation(tf.ones(shape=(1, 32, 32, 3)))
    print(con_bn_activation.summary())
    # identity = IdentityBlock()