# -*- coding: utf-8 -*-
# @File    : CNNModel.py
# @Author  : Hua Guo
# @Time    : 2019/12/25 下午9:33
# @Disc    :
from tensorflow.keras import layers, Model

from src.BaseClass.ModelBuilder import ModelBuilder


class CNN(Model):
    def __init__(self):
        super(CNN, self).__init__()
        self.l1 = layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3))
        self.bn1 = layers.BatchNormalization()
        self.l2 = layers.MaxPooling2D((2, 2))
        self.l3 = layers.Conv2D(64, (3, 3), activation='relu')
        self.l4 = layers.MaxPooling2D((2, 2))
        self.l5 = layers.Conv2D(64, (3, 3), activation='relu')
        self.l6 = layers.Flatten()
        self.l7 = layers.Dense(64, activation='relu')
        self.dense = layers.Dense(10, activation="softmax")

    def call(self, inputs, training=None, mask=None):
        # x = self.ResBlock1(inputs)
        x = self.l1(inputs)
        for layer in [
            self.bn1,
            self.l2,
            self.l3,
            self.l4,
            self.l5,
            self.l6,
            self.l7,
            self.dense
        ]:
            x = layer(x)
        return x


class CNNModel(ModelBuilder):

    def build_model(self):
        model = CNN()
        # model = ResNet()
        # model = models.Sequential()
        # model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
        # model.add(layers.MaxPooling2D((2, 2)))
        # model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        # model.add(layers.MaxPooling2D((2, 2)))
        # model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        # model.add(layers.Flatten())
        # model.add(layers.Dense(64, activation='relu'))
        # model.add(layers.Dense(10))
        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy']
                      )
        return model


if __name__ == "__main__":
    pass
    # cnn = CNN()
    # cnn(tf.ones(shape=(1, 32, 32, 3)))
    # print(cnn.summary())
    # cnn.build()
    # model = CNNModel().build_model()
    # print(model.summary())
    # block = ConvBlock()
    # identity_block = ResnetIdentityBlock(1, [1, 2, 3])
    # print()
