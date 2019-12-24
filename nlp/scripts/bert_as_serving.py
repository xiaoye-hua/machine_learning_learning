# -*- coding: utf-8 -*-
# @File    : bert_as_serving.py
# @Author  : Hua Guo
# @Time    : 2019/12/8 上午10:44
# @Disc    :
from bert_serving.client import BertClient


bc = BertClient()
# sentences = ["first do it", "then do it right", "then do it better"]
sentences = [
    "最大的优点也就是价钱比较实惠，另外有免费停车场如果住在古镇里面，白天是不允许把车开进去的。这个宾馆的服务员都说自己的餐厅做的当地小吃好吃，实在不敢苟同，份量少，味道也不地道，价格却不低，建议重视当地美食的朋友不要在宾馆的餐厅就餐，会对山西的小吃产生错误", # 2
    "这个配置和价位真的很合适，完全够用，而且小黑的质量非常不错", # 1
    "入住感想如下找不到5星级宾馆的感觉、总体水平最多只能算4星级。虽然房价比中州皇冠便宜100元左右、但所有硬件及软件远不及中州皇冠" # 0
]
result = bc.encode(sentences)
for v in result:
    print(len(v))
    print(v)