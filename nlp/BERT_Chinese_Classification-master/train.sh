#!/usr/bin/env bash

python run_classifier.py \
  --data_dir=debug_data \
  --task_name=sim \
  --vocab_file=../data_model/chinese_L-12_H-768_A-12/vocab.txt \
  --bert_config_file=../data_model/chinese_L-12_H-768_A-12/bert_config.json \
  --output_dir=sim_model \
  --do_train=true \
  --do_eval=true \
  --init_checkpoint=../data_model/chinese_L-12_H-768_A-12/bert_model.ckpt \
  --max_seq_length=70 \
  --train_batch_size=1 \
  --learning_rate=5e-5 \
  --num_train_epochs=10.0
