# -*- coding: utf-8 -*-
# @File    : bert_client_imj.py
# @Author  : Hua Guo
# @Time    : 2020/3/18 下午5:27
# @Disc    :
from bert_serving.client import BertClient
from sklearn.metrics.pairwise import cosine_similarity

class Encoding(object):
    def __init__(self):
        self.server_ip = "127.0.0.1"
        self.bert_client = BertClient(ip=self.server_ip)

    def encode(self, query):
        tensor = self.bert_client.encode([query])
        return tensor

    def query_similarity(self, query_list):
        tensors = self.bert_client.encode(query_list)
        return cosine_similarity(tensors)[0][1]

if __name__ == "__main__":
    ec = Encoding()
    print(ec.encode("中国").shape)
    print(ec.encode("美国").shape)
    print("中国和美国的向量相似度:", ec.query_similarity(["中国", "美国"]))
    print("中国和美国的向量相似度:", ec.query_similarity(["中国", "中国"]))
    print("中国和郭桦的向量相似度:", ec.query_similarity(["中国", "郭桦"]))
    print("中国和美国的向量相似度:", ec.query_similarity(["天安门", "天×安门"]))
    print("中国和美国的向量相似度:", ec.query_similarity(["天安门", "tian安门"]))


