# -*- coding: utf-8 -*-
# @File    : bert_as_serving.py
# @Author  : Hua Guo
# @Time    : 2019/12/8 上午10:44
# @Disc    :
from bert_serving.client import BertClient


bc = BertClient()
# sentences = ["first do it", "then do it right", "then do it better"]
sentences = ["中华", "美国", "日本"]
result = bc.encode(sentences)
for v in result:
    print(len(v))
    print(v)
