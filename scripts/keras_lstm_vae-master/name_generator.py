# encoding=utf-8
import numpy as np
import matplotlib.pyplot as plt
import os
# from lstm_vae import create_lstm_vae
from lstm_vae.vae_tensorflow import create_lstm_vae
# from utils import name_to_vec, vec_to_name
import tensorflow as tf
import numpy as np

def get_data(NAME_MAX_LEN):
    # read data from file
    # data = np.fromfile('sample_data.dat').reshape(419,13)
    # timesteps = 3
    # dataX = []
    # for i in range(len(data) - timesteps - 1):
    #     x = data[i:(i+timesteps), :]
    #     dataX.append(x)
    # return np.array(dataX)
    names = set()
    for filename in [
        #     'male.txt', 'female.txt'
        'chi_names_debug'
    ]:
        for line in open(os.path.join('../data/', filename)):
            if len(line.strip()):
                names.add(line.strip().lower())
    chars_dict = list(set(
        ''.join(list(names))
    )) + ['<END>', '<NULL>']
    indices_for_chars = {c: i for i, c in enumerate(chars_dict)}
     # include the <END> char
    name_vecs = np.array([name_to_vec(n, NAME_MAX_LEN, indices_for_chars) for n in names])
    # name_vecs = name_vecs.reshape(shape=())
    def one_hot(array, nb_classes):
        import numpy as np
        targets = np.array([array]).reshape(-1)
        one_hot_targets = np.eye(nb_classes)[targets]
        return one_hot_targets
    name_vecs = np.array([one_hot(array, len(chars_dict)) for array in name_vecs])
    return name_vecs, chars_dict, indices_for_chars

def name_to_vec(name, maxlen, indices_for_chars):
    v = np.zeros(maxlen, dtype=int)
    null_idx = indices_for_chars['<NULL>']
    v.fill(null_idx)
#     print(v)
    for i, c in enumerate(name):
        if i >= maxlen: break
        n = indices_for_chars.get(c, null_idx)
        v[i] = n
    v[min(len(name), maxlen-1)] = indices_for_chars['<END>']
    return v

def vec_to_name(vec, chars):
    name = ''
    for x in vec:
        char = chars[x]
        if len(char) == 1:
            name += char
        elif char == '<END>':
            return name
    return name



if __name__ == "__main__":
    # tf.dataset
    debug = True


    NAME_MAX_LEN = 5
    val_name = '石容千'
    batch_size = 64
    # chars = list('abcdefghijklmnopqrstuvwxyz') + ['<END>', '<NULL>']

    x, chars, indice_for_chars = get_data(NAME_MAX_LEN)
    model_path = '../models/chi_names/'
    # print(x.shape)
    if debug:
        x = x[:100]
    # print(x.shape)


    print(name_to_vec('石容千', NAME_MAX_LEN, indice_for_chars))
    print(vec_to_name(name_to_vec('石容千', NAME_MAX_LEN, indice_for_chars), chars))
    # assert vec_to_name(name_to_vec('石容千')) == '石容千'


    # x = x.reshape((x.shape[0], 1,  x.shape[1]))
    input_dim = x.shape[-1] # 13
    timesteps = x.shape[1] # 3
    # input_dim = len(chars)
    # timesteps = NAME_MAX_LEN

    batch_size = 1
    vae, enc, gen = create_lstm_vae(
        input_dim,
        timesteps=timesteps,
        batch_size=batch_size,
        intermediate_dim=64,
        latent_dim=NAME_MAX_LEN,
        epsilon_std=1. ,
        model_file_path = model_path
    )

    # print(help(vae.fit))
    vae.fit(
        x,
        # 非监督学习, y是啥
        x,
        batch_size=batch_size,
        nb_epoch=1,
        validation_split=0.1,
        # verbose=2
    )
    # validation
    name = val_name
    val_vec = name_to_vec(name, NAME_MAX_LEN, indice_for_chars)
    val_vec = np.array(val_vec).reshape([-1, NAME_MAX_LEN])
    target_vec = gen.predict(
        val_vec
    )
    target_vec = target_vec.reshape([NAME_MAX_LEN, len(chars)])
    target_vec = tf.argmax(target_vec, axis=1)
    with tf.Session() as sess:
        target_vec = sess.run(target_vec)
    target_name = vec_to_name(target_vec, chars)
    # print(target_vec)
    print('{} ---> {}'.format(name, target_name))
    # print(dir(target_vec))

    # model save
    # train log
    #


    # preds = vae.predict(x, batch_size=batch_size)
    # # pick a column to plot.
    # print("[plotting...]")
    # print("x: %s, preds: %s" % (x.shape, preds.shape))
    # plt.plot(x[:,0,3], label='data')
    # plt.plot(preds[:,0,3], label='predict')
    # plt.legend()
    # plt.show()


