# -*- coding: utf-8 -*-
# @File    : model_local_inference.py
# @Author  : Hua Guo
# @Time    : 2019/12/15 下午8:18
# @Disc    :
import tensorflow as tf
from run_classifier import InputExample, convert_single_example
import tokenization


model_path = "./models/bert"
predict_fn = tf.contrib.predictor.from_saved_model(
            model_path
)
input_dict = {}
index = 1
ex_index = 0
label_ids = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
label_list = ['0', '1', '2']
max_seq_length = 70
vocab_file = "../data_model/chinese_L-12_H-768_A-12/vocab.txt"
do_lower_case = True
fix_label = "2"

text = "linux改xp花了一下午时间。散热不好，cpu温度就没下过50，玩游戏能上70，比较吓人。触摸板关不掉，打字经常碰到。"
guid = 'train-%d' % index  # 参数guid是用来区分每个example的
text_a = tokenization.convert_to_unicode(text)  # 要分类的文本
# label = str(line[2])  # 文本对应的情感类别
example = InputExample(guid=guid, text_a=text_a, text_b=None, label=fix_label)


tokenizer = tokenization.FullTokenizer(
        vocab_file=vocab_file, do_lower_case=do_lower_case
)
feature = convert_single_example(ex_index,
                                 example,
                                 label_list,
                                 max_seq_length,
                                 tokenizer
                                 )
# input_dict["input_ids"] = [[101, 8403, 3121, 8766, 5709, 749, 671, 678, 1286, 3198, 7313, 511, 3141, 4178, 679, 1962, 8024, 8476, 3946, 2428, 2218, 3766, 678, 6814, 8145, 8024, 4381, 3952, 2767, 5543, 677, 8203, 8024, 3683, 6772, 1405, 782, 511, 6239, 3043, 3352, 1068, 679, 2957, 8024, 2802, 2099, 5307, 2382, 4821, 1168, 511, 102, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# input_dict["input_mask"] = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# input_dict["segment_ids"] = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# input_dict["label_ids"] = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
input_dict["input_ids"] = [feature.input_ids]
input_dict["input_mask"] = [feature.input_mask]
input_dict["segment_ids"] = [feature.segment_ids]
input_dict["label_ids"] = [label_ids]
prob = predict_fn(input_dict)
print(prob)
