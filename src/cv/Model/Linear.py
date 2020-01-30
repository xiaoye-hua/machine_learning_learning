# -*- coding: utf-8 -*-
# @File    : Linear.py
# @Author  : Hua Guo
# @Time    : 2020/1/30 下午5:49
# @Disc    : linear model:  w*a + b = y
import tensorflow as tf
# from tensorflow.keras import layers, models


# class Linear(layers):
#     # pass
#     def __init__(self):
#         super(Linear, self).__init()
#
#     def build(self):
#         pass
#
#     def call(self, input):
#         pass
class Linear(
    # tf.keras.Model
    tf.keras.layers.Layer
             ):

  def __init__(self, units=32):
    super(Linear, self).__init__()
    self.units = units

  def build(self, input_shape):
    self.w = self.add_weight(
                            shape=(input_shape[-1], self.units),
                             initializer='random_normal',
                             trainable=True)
    self.b = self.add_weight(shape=(self.units,),
                             initializer='random_normal',
                             trainable=True)

  def call(self, inputs):
    return tf.matmul(inputs, self.w) + self.b


if __name__ == "__main__":
    # train_x = [1, 2, 3, 4]
    # train_y = [2, 4, 6, 8]

    # 2x + 3
    def target_func(x):
        return float(2*x + 3)

    train_x = [1.0]
    train_y = [5.0]
    # train_x = [float(value) for value in range(1, 1000)]
    # train_y = [target_func(x) for x in train_x]
    epoches = 10000000
    # x = tf.ones((1, 1))
    linear_layer = Linear(1)
    linear_layer.compile(
        optimizer='adam',
        loss="mean_squared_error",
        metrics=['accuracy']
    )
    # model.compile(optimizer='adam',
    #               loss='sparse_categorical_crossentropy',
    #               metrics=['accuracy'])
    linear_layer.fit(
        # (train_x, train_y)
        x=train_x,
        y=train_y,
        epochs=epoches
                     )

    sample = [1.0]
    predict = linear_layer.predict(sample)
    groud_truth = target_func(sample[0])
    print(predict)
    print(groud_truth)
    # y = linear_layer(x)
    # print(y)