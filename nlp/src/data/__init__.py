# -*- coding: utf-8 -*-
# @File    : __init__.py.py
# @Author  : Hua Guo
# @Time    : 2019/12/4 下午8:37
# @Disc    :
# import numpy as np
# from tqdm import tqdm
# from keras_bert import Tokenizer
# import os
# import codecs
# from src.config import pretrained_path, SEQ_LEN
#
# config_path = os.path.join(pretrained_path, 'bert_config.json')
# checkpoint_path = os.path.join(pretrained_path, 'bert_model.ckpt')
# vocab_path = os.path.join(pretrained_path, 'vocab.txt')
#
# token_dict = {}
# with codecs.open(vocab_path, 'r', 'utf8') as reader:
#     for line in reader:
#         token = line.strip()
#         token_dict[token] = len(token_dict)
#
#
# tokenizer = Tokenizer(token_dict)
# def load_data(path, batch_size):
#     global tokenizer
#     indices, sentiments = [], []
#     for folder, sentiment in (('neg', 0), ('pos', 1)):
#         folder = os.path.join(path, folder)
#         for name in tqdm(os.listdir(folder)):
# #             print(name)
#             with open(os.path.join(folder, name), 'r') as reader:
#                   text = reader.read()
#             ids, segments = tokenizer.encode(text, max_len=SEQ_LEN)
# #             print(ids)
#             indices.append(ids)
#             sentiments.append(sentiment)
#     items = list(zip(indices, sentiments))
#     np.random.shuffle(items)
#     indices, sentiments = zip(*items)
#     indices = np.array(indices)
#     mod = indices.shape[0] % batch_size
#     if mod > 0:
#         indices, sentiments = indices[:-mod], sentiments[:-mod]
#     return [indices, np.zeros_like(indices)], np.array(sentiments)
#
#
# if __name__ == "__main__":
#     debug = True
#
#     if debug:
#         dataset = "./data_model/aclImdb/debug"
#     else:
#         dataset = "./data_model/aclImdb/"
#
#     train_path = os.path.join(dataset, 'train')
#     train_x, train_y = load_data(train_path)
#     print()