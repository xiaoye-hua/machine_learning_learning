# -*- coding: utf-8 -*-
# @File    : DataLoader.py
# @Author  : Hua Guo
# @Time    : 2019/12/16 下午9:08
# @Disc    :
import os
from tqdm import tqdm


class DataLoader:
    @staticmethod
    def load_data(path):
        data_lst = []
        for folder, sentiment in (('neg', 0), ('pos', 1)):
            folder = os.path.join(path, folder)
            for name in tqdm(os.listdir(folder)):
                with open(os.path.join(folder, name), 'r') as reader:
                    text = reader.read()
                data_lst.append([text, sentiment])
        return data_lst