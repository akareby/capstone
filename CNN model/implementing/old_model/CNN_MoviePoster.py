#
# filename : CNN_MoviePoster.py
# history
# =============================
# 20190705 v.0.0.0 초안 작성 강진우
# 20190705 v.0.0.1 주석 작성 강진우
# 20190707 v.0.0.2 memory 부족문제로 batch_size 수정, 전체 shape 동일하게 조정(182,268,3)
# =============================
# description
# TODO :: Image Preprocessing (by OpenCV) 을 통한 feature 검출을 통해 accuracy 개선
# TODO :: 낮은 accuracy 개선을 위해 hyperparameter 수정 및 hidden layer 조정
# TODO :: 위협안정 모델을 위한 label의 수정과 이미지 분류 재조정
# TODO :: network를 통한 cnn 개선 (ex. AlexNet, ResNet etc...)

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

trainlist, testlist = [], []    # train, eval 이미지 경로와 라벨을 text로 받아 list 만듦
with open('train.txt') as f:    # train 경로
    for line in f:
        tmp = line.strip().split()
        trainlist.append([tmp[0], tmp[1]])

with open('eval.txt') as f:     # eval 경로
    for line in f:
        tmp = line.strip().split()
        testlist.append([tmp[0], tmp[1]])

def readimg(path):
    img = plt.imread(path)      # 이미지를 읽어 픽셀 값으로 변경
    return img

def batch(path, batch_size):    # batch 생성
    img, label, paths = [], [], []
    for i in range(batch_size):
        img.append(readimg(path[0][0]))
        label.append(int(path[0][1]))
        path.append(path.pop(0))
    return img, label

# 3차원 Tensor [182,268,3], Label [10]
IMG_H = 268
IMG_W = 182
IMG_C = 3
num_class = 10

# 학습에 쓰일 그래프 생성, Convolutional Neural Network 및 softmax를 이용한 loss 계산
# convolution - pooling - convolution - pooling - .....- classification
with tf.Graph().as_default() as g:
    X = tf.placeholder(tf.float32, [None, IMG_H, IMG_W, IMG_C]) # [batch, 268, 182, 3]
    Y = tf.placeholder(tf.int32, [None])

    with tf.variable_scope('CNN'):
        net = tf.layers.conv2d(X, 20, 3, (2, 2), padding='same', activation=tf.nn.relu)
        # conv2d(입력이미지, 출력채널갯수, kerel사이즈, stride, padding, 활성함수)
        net = tf.layers.max_pooling2d(net, 2, 2)
        # pooling2d(입력, pooling사이즈, stride, padding)
        net = tf.layers.conv2d(net, 40, 3, (2, 2), padding='same', activation=tf.nn.relu)
        net = tf.layers.flatten(net)
        # 이미지->CNN->[batch,height,width,depth]
        # 4차원텐서를 1차원벡터로 변경[batch, height*width*depth]
        out = tf.layers.dense(net, num_class) # [batch, class_num]

    with tf.variable_scope('Loss'):
        loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=Y, logits=out))
    #   Optimizing
    train = tf.train.AdamOptimizer(1e-3).minimize(loss)
    saver = tf.train.Saver()

np.sum([np.product(var.shape) for var in g.get_collection('trainable_variables')]).value

# session을 실행하여 학습 시작, epoch = 30, batch = 100
batch_size = 100
with tf.Session(graph=g) as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(30):
        batch_data, batch_label = batch(trainlist, batch_size)
        _, l = sess.run([train, loss], feed_dict={X: batch_data, Y: batch_label})
        print(i, l)
    saver.save(sess, 'logs/model.ckpt', global_step=i + 1)

# 학습된 데이터를 불러와 테스트 실행
acc = 0
with tf.Session(graph=g) as sess:
    sess.run(tf.global_variables_initializer())
    checkpoint = tf.train.latest_checkpoint('logs')
    if checkpoint:
        saver.restore(sess, checkpoint)
    for i in range(len(testlist)):
        batch_data, batch_label = batch(testlist, 1)
        logit = sess.run(out, feed_dict={X: batch_data}) # label 예측
        if np.argmax(logit[0]) == batch_label[0]:
            acc += 1
        else:
            print(logit[0], batch_label[0])
    print(acc / len(testlist))
