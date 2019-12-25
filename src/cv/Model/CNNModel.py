# -*- coding: utf-8 -*-
# @File    : CNNModel.py
# @Author  : Hua Guo
# @Time    : 2019/12/25 下午9:33
# @Disc    :
from tensorflow.keras import layers, models

from src.BaseClass.ModelBuilder import ModelBuilder


class CNNModel(ModelBuilder):
    def build_model(self):
        model = models.Sequential()
        model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        model.add(layers.Flatten())
        model.add(layers.Dense(64, activation='relu'))
        model.add(layers.Dense(10, activation='softmax'))
        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        return model


if __name__ == "__main__":
    model = CNNModel().build_model()
    print(model.summary())