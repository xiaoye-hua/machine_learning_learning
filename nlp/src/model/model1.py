# -*- coding: utf-8 -*-
# @File    : model1.py
# @Author  : Hua Guo
# @Time    : 2019/12/18 下午9:02
# @Disc    :
import tensorflow as tf
from tensorflow.keras.layers import LSTM,  Dense
from tensorflow.keras.layers import Input, Dense, Dropout, Flatten, BatchNormalization
from tensorflow.keras.layers import Bidirectional, GlobalMaxPool1D, MaxPooling1D, Add, Flatten, GlobalAveragePooling1D, GlobalMaxPooling1D, concatenate, SpatialDropout1D
from tensorflow.keras.layers import Dense, Input, LSTM, Embedding, Dropout, Activation, Conv1D, GRU, CuDNNGRU, CuDNNLSTM, BatchNormalization
from tensorflow.keras.layers import Embedding
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.optimizers import Adam


def build_model(input_dim,
                     lstm_dim=256,
                     ):
    inp = Input(shape=(1, input_dim))
    x = LSTM(
        units=lstm_dim
    )(inp)
    output = Dense(
        units=1,
        activation='sigmoid'
    )(x)
    model = Model(
        inputs=inp,
        outputs=output
    )
    optimizer = tf.train.AdamOptimizer()

    metrics = [
      tf.keras.metrics.TruePositives(name='tp'),
      tf.keras.metrics.FalsePositives(name='fp'),
      tf.keras.metrics.TrueNegatives(name='tn'),
      tf.keras.metrics.FalseNegatives(name='fn'),
      tf.keras.metrics.BinaryAccuracy(name='accuracy'),
      tf.keras.metrics.Precision(name='precision'),
      tf.keras.metrics.Recall(name='recall'),
      # tf.keras.metrics.AUC(name='auc'),
]
    model.compile(
        # optimizer=Adam(),
        optimizer=optimizer,
        # loss='categorical_crossentropy',
        loss = tf.keras.losses.BinaryCrossentropy(),
        metrics=metrics,
    )
    return model