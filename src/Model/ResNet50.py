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
    def __init__(self, filter: int, kernel_size: List[int], padding: str, activation: str, stride=None) -> None:
        super(ConvBNActivation, self).__init__()
        if stride is None:
            stride = [1, 1]
        self.conv = layers.Conv2D(
            filters=filter,
            kernel_size=kernel_size,
            padding=padding,
            strides=stride
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

        self.con_bn_ac1 = ConvBNActivation(filter=f1, kernel_size=[1, 1], padding="valid", activation="relu")
        self.con_bn_ac2 = ConvBNActivation(filter=f2, kernel_size=[kernel_size, kernel_size], padding="same", activation="relu")
        self.conv = layers.Conv2D(filters=f3, kernel_size=[1, 1], padding="same")
        self.bn = layers.BatchNormalization()
        self.activation = layers.Activation("relu")

    def call(self, inputs, training=None, mask=None):
        x = self.con_bn_ac1(inputs)
        for l in [
            self.con_bn_ac2,
            self.conv,
            self.bn
        ]:
            x = l(x)
        x = tf.math.add(x, inputs)
        return self.activation(x)


class ConvBlock(Model):
    """
    In the case where the dimension of the the input activation is different from that of the output activation
    Structures are as follow:
        3 conv in the main path
        1 conv in the shortcut path
    """
    def __init__(self, mid_kernel_size: int, shortcut_stride: int, filters: List[int]):
        super(ConvBlock, self).__init__()
        f1, f2, f3 = filters
        self.con_bn_ac1 = ConvBNActivation(filter=f1, kernel_size=[1, 1], padding="valid", activation="relu",
                                           stride=[shortcut_stride, shortcut_stride])
        self.con_bn_ac2 = ConvBNActivation(filter=f2, kernel_size=[mid_kernel_size, mid_kernel_size],
                                           padding="same", activation="relu")
        self.conv = layers.Conv2D(filters=f3, kernel_size=[1, 1], padding="same")
        self.bn = layers.BatchNormalization()
        self.activation = layers.Activation("relu")
        self.conv_shortcut = layers.Conv2D(filters=f3, kernel_size=[1, 1], padding="valid",
                                           strides=[shortcut_stride, shortcut_stride])
        self.bn_shortcut = layers.BatchNormalization()

    def call(self, inputs, training=None, mask=None):
        # shortcut branch
        x_short_cut = self.conv_shortcut(inputs)
        x_short_cut = self.bn_shortcut(x_short_cut)
        # main path
        x = self.con_bn_ac1(inputs)
        for l in [
            self.con_bn_ac2,
            self.conv,
            self.bn
        ]:
            x = l(x)
        x = tf.math.add(x, x_short_cut)
        return self.activation(x)


class ResNet50(Model):
    """
    Residual NN with 50 layers
    Structures stages are as follow:
        0. zero padding
        1. conv + bn + Relu + max pooling
        2. Convblock + IdentityBlock*2
        3. Convblock + IdentityBlock*2
        4, Convblock + IdentityBlock*5
        5, Convblock + IdentityBlock*2
        6. avg pooling + flatten + fc
    """
    def __init__(self, class_num: int) -> None:
        super(ResNet50, self).__init__()
        self.class_num = class_num
        # stage 1
        self.con_bn_ac = ConvBNActivation(
            filter=64,
            kernel_size=[7, 7],
            activation="relu",
            padding="valid"
        )
        self.max_pooling = layers.MaxPool2D((3, 3), strides=(2, 2))
        # stage 2
        self.conv_block1 = ConvBlock(
            mid_kernel_size=3,
            filters=[64, 64, 256],
            shortcut_stride=1
        )
        self.identity_block1 = IdentityBlock(
            kernel_size=3,
            filters=[64, 64, 256]
        )
        self.identity_block2 = IdentityBlock(
            kernel_size=3,
            filters=[64, 64, 256]
        )
        # stage 3
        self.conv_block2 = ConvBlock(
            mid_kernel_size=3,
            filters=[128, 128, 512],
            shortcut_stride=2
        )
        self.identity_block3 = IdentityBlock(
            kernel_size=3,
            filters=[128, 128, 512]
        )
        self.identity_block4 = IdentityBlock(
            kernel_size=3,
            filters=[128, 128, 512]
        )
        self.identity_block5 = IdentityBlock(
            kernel_size=3,
            filters=[128, 128, 512]
        )
        # stage 4
        self.conv_block3 = ConvBlock(
            mid_kernel_size=3,
            filters=[256, 256, 1024],
            shortcut_stride=2
        )
        self.identity_block6 = IdentityBlock(
            kernel_size=3,
            filters=[256, 256, 1024]
        )
        self.identity_block7 = IdentityBlock(
            kernel_size=3,
            filters=[256, 256, 1024]
        )
        self.identity_block8 = IdentityBlock(
            kernel_size=3,
            filters=[256, 256, 1024]
        )
        self.identity_block9 = IdentityBlock(
            kernel_size=3,
            filters=[256, 256, 1024]
        )
        self.identity_block10 = IdentityBlock(
            kernel_size=3,
            filters=[256, 256, 1024]
        )
        # stage 5
        self.conv_block4 = ConvBlock(
            mid_kernel_size=3,
            filters=[512, 512, 2048],
            shortcut_stride=2
        )
        self.identity_block11 = IdentityBlock(
            kernel_size=3,
            filters=[512, 512, 2048]
        )
        self.identity_block12 = IdentityBlock(
            kernel_size=3,
            filters=[512, 512, 2048]
        )

        self.avg_pooling = layers.AveragePooling2D(
            pool_size=(2, 2),
            padding="same"
        )
        self.flat = layers.Flatten()
        self.dese = layers.Dense(
            class_num,
            "softmax"
        )

    def call(self, inputs, training=None, mask=None):
        x = layers.ZeroPadding2D(padding=[3, 3])(inputs)
        for block in [
            # stage 1
            self.con_bn_ac,
            self.max_pooling,
            # stage 2
            self.conv_block1,
            self.identity_block1,
            self.identity_block2,
            # stage 3
            self.conv_block2,
            self.identity_block3,
            self.identity_block4,
            self.identity_block5,
            # stage 4
            self.conv_block3,
            self.identity_block6,
            self.identity_block7,
            self.identity_block8,
            self.identity_block9,
            self.identity_block10,
            # stage 5
            self.conv_block4,
            self.identity_block11,
            self.identity_block12,
            self.avg_pooling,
            self.flat,
            self.dese

        ]:
            x = block(x)
        return x


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
    identity_block = IdentityBlock(
        kernel_size=3,
        filters=[3, 10, 3]
    )
    identity_block(tf.ones(shape=(1, 32, 32, 3)))
    print(identity_block.summary())
    conv_block = ConvBlock(
        mid_kernel_size=3,
        filters=[3, 10, 5],
        shortcut_stride=2
    )
    conv_block(tf.ones(shape=(1, 32, 32, 10)))
    print(conv_block.summary())

    resnet50 = ResNet50(class_num=238)
    resnet50(tf.ones(shape=(1, 32, 32, 3)))
    print(resnet50.summary())