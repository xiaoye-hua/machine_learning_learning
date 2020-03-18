
import tensorflow as tf

from tensorflow.keras import datasets, layers, models

# import sys
# sys.path.append("../")
# from src.cv.Model import model_builder_dict
# from src.cv.Model.ResNet import ResNet
from src.Model.ResNet50 import ResNet50
from src.Model.CNNModel import CNN




debug = True
debug_data_length = 100
model_builder_key = "cnn_model"
label_num = 10
res_block_num = 3
conv_filter_num = 64
channel_num = 3
if debug:
    batch_size = 10
    train_epoches = 1
else:
    train_epoches = 3
model_dir = "models"


(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# Normalize pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0
if debug:
    train_images = train_images[:debug_data_length, :, :]
    train_labels = train_labels[:debug_data_length, :]
    test_images = test_images[:debug_data_length, :, :]
    test_labels = test_labels[:debug_data_length, :]


# # ## Input_fn
#
# # In[9]:
#
#
# def input_fn(X, y, batch_size, epoch=1):
# #     def fun():
#     dataset = tf.data.Dataset.from_tensor_slices((X, y))
#     return dataset.repeat(epoch).batch(batch_size=batch_size)


print("*"*30)
print(train_images.shape)
print(train_labels.shape)
datasets = tf.data.Dataset.from_tensor_slices((train_images, train_labels)).repeat(train_epoches).batch(batch_size=batch_size)
test_dataset = tf.data.Dataset.from_tensor_slices((test_images, test_labels)).batch(batch_size=batch_size)


# model = ResNet50(
#     class_num=label_num
# )
train_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name='accuracy')

model = CNN()
model.compile(
    optimizer="adam",
    loss = "sparse_categorical_crossentropy",
    metrics=[train_accuracy]
)
model.fit(
    datasets,
    validation_data=test_dataset
)

model.save(model_dir)
# tf.keras.models.save_model(models, model_dir)