# LearningVisualizer.py
#
# history
# =============================
# 20190705 v.0.0.0 초안 작성 김한동
# 20190000 v.0.1.0 validation set 사용이 정확도에 악영향을 끼쳐 일단 제외 김한동
# =============================
# description
# 기존 만들어진 코드의 학습 정확도(acc), 손실 함수 계수(loss), 최적화 정확도(val_acc), 최적화 손실 함수 계수(val_loss)를 시각화하여 데이터셋과 모델을 평가하기 위해 keras로 재작성
# tensorflow로 작성된 코드와 비교를 위해 본 모델로 실험한 부분은 모두 주석처리

from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
# from keras.utils import np_utils

# from PIL import Image

# 데이터셋을 만들기 위해 ImageDateGenerator 사용
train_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        'train',
        target_size=(100, 100),
        batch_size=3,
        class_mode='categorical')

test_datagen = ImageDataGenerator(rescale=1./255)

test_generator = test_datagen.flow_from_directory(
        'eval',
        target_size=(100, 100),
        batch_size=3,
        class_mode='categorical')

# 최적화 데이터셋을 만들기 위한 부분
# 20190000 @김한동, 균일한 그래프를 그리지 못하고 제대로 적용되지 않아 제외
# val_datagen = ImageDataGenerator(rescale=1./255)
#
# val_generator = val_datagen.flow_from_directory(
#         'val',
#         target_size=(100, 100),
#         batch_size=3,
#         class_mode='binary')

# Build Model
model = Sequential()
model.add(Conv2D(20, kernel_size = (5, 5), padding = 'same', activation = 'relu', input_shape = (100, 100, 3)))
model.add(MaxPooling2D(pool_size = (2, 2)))

model.add(Conv2D(40, kernel_size = (5, 5), padding = 'same', activation = 'relu'))
model.add(Flatten())

model.add(Dense(128, activation = 'relu'))
model.add(Dense(3, activation = 'softmax'))

# Prepare model for learning
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Learn model
# from keras.callbacks import EarlyStopping
# early_stopping = EarlyStopping(patience=5)
hist = model.fit_generator(
        train_generator,
        steps_per_epoch=35,
        epochs=25)
        # validation_data=val_generator,
        # validation_steps=4)
        # callbacks=[early_stopping])

# Evaluate model
# print("-- Evaluate --")
# scores = model.evaluate_generator(test_generator, steps=7)
# print("%s : %.2f%%" %(model.metrics_names[0], scores[0]*100))
# print("%s: %.2f%%" %(model.metrics_names[1], scores[1]*100))

# Use model
# print("-- Predict --")
# output = model.predict_generator(test_generator, steps=8)
# np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
# print(test_generator.class_indices)
# print(output)

# Visualization
fig, loss_ax = plt.subplots()

acc_ax = loss_ax.twinx()

loss_ax.plot(hist.history['loss'], 'y', label='train loss')
# loss_ax.plot(hist.history['val_loss'], 'r', label='val loss')

acc_ax.plot(hist.history['acc'], 'b', label='train acc')
# acc_ax.plot(hist.history['val_acc'], 'g', label='val acc')

loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
acc_ax.set_ylabel('accuray')

loss_ax.legend(loc='upper left')
acc_ax.legend(loc='lower left')

plt.show()