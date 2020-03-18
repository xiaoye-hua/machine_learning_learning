# -*- coding: utf-8 -*-
# @File    : similarity_test.py
# @Author  : Hua Guo
# @Time    : 2020/3/18 下午4:59
# @Disc    :
import jieba
from operator import itemgetter
from bert_client_imj import Encoding
# from bert_serving.client import BertClient


# 创建n-gram
def compute_ngrams(sequence, n):
    lst = list(zip(*[sequence[index:] for index in range(n)]))
    for i in range(len(lst)):
        lst[i] = ''.join(lst[i])
    return lst

# 模板
# template = '伊斯兰组织'
# 示例句子
# doc = "巴基斯坦当地时间2014年12月16日早晨，巴基斯坦塔利班运动武装分子袭击了西北部白沙瓦市一所军人子弟学校，打死141人，其中132人为12岁至16岁的学生。"

template = "天安门"
doc = "我爱北京天安门,tian安门上太阳升"

words = list(jieba.cut(doc))
all_lst = []
for j in range(1, 5):
    all_lst.extend(compute_ngrams(words, j))

ec = Encoding()
similar_word_dict = {}

# 查找文章中与template的最接近的词语
for word in all_lst:
    # print(word)
    if word not in similar_word_dict.keys():
        similar_word_dict[word] = ec.query_similarity([word, template])

# 按相似度从高到低排序
sorted_dict = sorted(similar_word_dict.items(), key=itemgetter(1), reverse=True)
print(sorted_dict)

print('与%s最接近的实体是: %s，相似度为 %s.' %(template, sorted_dict[0][0], sorted_dict[0][1]))