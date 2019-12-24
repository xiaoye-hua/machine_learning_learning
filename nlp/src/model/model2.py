# -*- coding: utf-8 -*-
# @File    : model2.py
# @Author  : Hua Guo
# @Time    : 2019/12/18 下午9:30
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
                lr = 1e-3,
                lr_d = 1e-10, units = 64, spatial_dr = 0.3, kernel_size1=3, kernel_size2=2,
                     dense_units=32, dr=0.1, conv_size=32
                     ):

    # inp = Input(shape=(max_len,))
    # 直接load训练好的为embedding_matrix 没在这儿训练
    # x = Embedding(19479, embed_size, weights=[embedding_matrix], trainable=False)(inp)
    inp = Input(shape=(1, input_dim))

    # x = Embedding(
    #     input_dim=char_dim,
    #     output_dim=embedding_dim,
    #     input_length=input_dim
    # )(inp)
    # gpu = tf.test.is_gpu_available()

    # 丢掉整个dim, 普通的丢掉几个元素而已
    # ? 下一步如何衔接dim?
    x1 = SpatialDropout1D(spatial_dr)(inp)

    # bidirection wrapper in rnn
    # CuDNN... 英伟达出品,只能在GPU上跑
    # if gpu:
    #     x_gru = Bidirectional(CuDNNGRU(units, return_sequences=True))(x1)
    # else:
    x_gru = Bidirectional(GRU(units, return_sequences=True))(x1)
    x1 = Conv1D(conv_size, kernel_size=kernel_size1, padding='valid', kernel_initializer='he_uniform')(x_gru)
    # global average pooling operation for temporal data
    avg_pool1_gru = GlobalAveragePooling1D()(x1)
    max_pool1_gru = GlobalMaxPooling1D()(x1)

    x3 = Conv1D(conv_size, kernel_size=kernel_size2, padding='valid', kernel_initializer='he_uniform')(x_gru)
    avg_pool3_gru = GlobalAveragePooling1D()(x3)
    max_pool3_gru = GlobalMaxPooling1D()(x3)

    # if gpu:
    #     x_lstm = Bidirectional(CuDNNLSTM(units, return_sequences=True))(x1)
    # else:
    x_lstm = Bidirectional(LSTM(units, return_sequences=True))(x1)
    x1 = Conv1D(conv_size, kernel_size=kernel_size1, padding='valid', kernel_initializer='he_uniform')(x_lstm)
    avg_pool1_lstm = GlobalAveragePooling1D()(x1)
    max_pool1_lstm = GlobalMaxPooling1D()(x1)

    x3 = Conv1D(conv_size, kernel_size=kernel_size2, padding='valid', kernel_initializer='he_uniform')(x_lstm)
    avg_pool3_lstm = GlobalAveragePooling1D()(x3)
    max_pool3_lstm = GlobalMaxPooling1D()(x3)

    x = concatenate([avg_pool1_gru, max_pool1_gru, avg_pool3_gru, max_pool3_gru,
                     avg_pool1_lstm, max_pool1_lstm, avg_pool3_lstm, max_pool3_lstm])
    x = BatchNormalization()(x)
    x = Dropout(dr)(Dense(dense_units, activation='relu')(x))
    x = BatchNormalization()(x)
    x = Dropout(dr)(Dense(int(dense_units / 2), activation='relu')(x))

    x = Dense(1, activation="sigmoid")(x)

    model = Model(inputs=inp, outputs=x)
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
    optimizer = tf.train.AdamOptimizer(learning_rate=lr)
    model.compile(loss="binary_crossentropy", optimizer=optimizer, metrics=metrics)
    return model