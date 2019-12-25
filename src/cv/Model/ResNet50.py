# -*- coding: utf-8 -*-
# @File    : ResNet50.py
# @Author  : Hua Guo
# @Time    : 2019/12/25 下午9:56
# @Disc    :
from tensorflow.keras.applications import ResNet50

from src.BaseClass.ModelBuilder import ModelBuilder

#
# class ResNet50(ModelBuilder):
#     def build_model(self):
#         pass


model = ResNet50()
print(model.summary())
