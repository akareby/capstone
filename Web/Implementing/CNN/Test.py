#
# filename : Test.py
# history
# =============================
# 20190812 v.0.0.0 초안 작성 강진우
# 20190812 v.0.0.1 주석 작성 강진우
# 20190903 v.0.1.0 predict rate 개선 강진우
# 20190909 v.0.2.0 웹과 통합, TODO 항목 추가  김한동
# 20190911 v.1.0.0 장르를 글자로 표시해줄 수 있는 predictListNaming 함수 추가, TODO 항목 추가 김한동
# 20190915 v.1.1.0 저작권 문제 영상을 위한 판별코드 errorIndex 추가 김한동
# =============================
# description
# 
#
#
import tensorflow as tf
import matplotlib.pyplot as plt
from CNN import Youtube_Crawling
from CNN import Test_preprocessing
from CNN import Test_input
import sys

# TODO :: 결과 중 일반이 5개 이상 있으면 일반으로 분류, 아닐 경우 그냥 유해로 분류
def predictListNaming(predictlist):
    max = 0
    maxIndex = 0

    tplGenre = ('공포', '잔인', '음란', '일반')

    if(predictlist[0][0] < predictlist[0][1]):
        max = predictlist[0][1]
        maxIndex = 1
    else:
        max = predictlist[0][0]
        maxIndex = 0

    if(max < predictlist[0][2]):
        maxIndex = 2
    else:
        maxIndex = maxIndex

    if(predictlist[0][0] + predictlist[0][1] + predictlist[0][2] < 0):
        maxIndex = 3

    return str(tplGenre[maxIndex])

def main(url):
    print("########## Youtube crawling ####################")
    try:
        lstResult = Youtube_Crawling.main(url)
    except:
        print("\n\n")
        print("############### Unable to censor due to copyright issue. ###############")
        errorIndex = 333
        return errorIndex
        sys.exit()

    print("########## Youtube data preprocessing ##########")
    print("########## Youtube data input ##################")
    Test_preprocessing.main()
    Test_input.main()

    testlist, testlist0, testlist1, testlist2, \
    testlist3, testlist4, testlist5, testlist6, \
    testlist7, testlist8, testlist9 = [], [], [], [], [], [], [], [], [], [], []   # predict 이미지 경로와 라벨을 text 로 받아 list 만듦

    with open('predict.txt') as f:     # predict 경로
        for line in f:
            tmp = line.strip().split()
            if (int(tmp[1]) == 0) :
                testlist0.append([tmp[0], tmp[1]])
                testlist.append([tmp[0], tmp[1]])
            elif (int(tmp[1]) == 1) :
                testlist1.append([tmp[0], tmp[1]])
                testlist.append([tmp[0], tmp[1]])
            elif (int(tmp[1]) == 2):
                testlist2.append([tmp[0], tmp[1]])
                testlist.append([tmp[0], tmp[1]])
            elif (int(tmp[1]) == 3) :
                testlist3.append([tmp[0], tmp[1]])
                testlist.append([tmp[0], tmp[1]])
            elif (int(tmp[1]) == 4) :
                testlist4.append([tmp[0], tmp[1]])
                testlist.append([tmp[0], tmp[1]])
            elif (int(tmp[1]) == 5) :
                testlist5.append([tmp[0], tmp[1]])
                testlist.append([tmp[0], tmp[1]])
            elif (int(tmp[1]) == 6) :
                testlist6.append([tmp[0], tmp[1]])
                testlist.append([tmp[0], tmp[1]])
            elif (int(tmp[1]) == 7) :
                testlist7.append([tmp[0], tmp[1]])
                testlist.append([tmp[0], tmp[1]])
            elif (int(tmp[1]) == 8) :
                testlist8.append([tmp[0], tmp[1]])
                testlist.append([tmp[0], tmp[1]])
            elif (int(tmp[1]) == 9) :
                testlist9.append([tmp[0], tmp[1]])
                testlist.append([tmp[0], tmp[1]])

    def readimg(path):
        img = plt.imread(path)      # 이미지를 읽어 픽셀 값으로 변경
        return img

    def batch(path, batch_size):    # batch size 생성
        img, divide, paths = [], [], []
        for i in range(batch_size):
            img.append(readimg(path[0][0]))
            divide.append(int(path[0][1]))
            path.append(path.pop(0))
        return img, divide

    # 3차원 Tensor [100,100,3], Label [10]
    IMG_H = 100
    IMG_W = 100
    IMG_C = 3
    num_class = 3

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
            net = tf.layers.max_pooling2d(net, 2, 2)
            net = tf.layers.conv2d(net, 80, 3, (2, 2), padding='same', activation=tf.nn.relu)
            net = tf.layers.flatten(net)
            # 이미지->CNN->[batch,height,width,depth]
            # 4차원텐서를 1차원벡터로 변경[batch, height*width*depth]
            out = tf.layers.dense(net, num_class) # [batch, class_num]
        with tf.variable_scope('Loss'):
            loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=Y, logits=out))
            #   Optimizing
        train = tf.train.AdamOptimizer(1e-3).minimize(loss)
        saver = tf.train.Saver()

    print("\n")
    # predict
    # TODO :: Refactoring 소요 있음! 반복되는 코드 발견!
    num = 0
    if (num == 0) :
        acc = 0
        predictlist = [[0, 0, 0]]
        with tf.Session(graph=g) as sess:
            sess.run(tf.global_variables_initializer())
            checkpoint = tf.train.latest_checkpoint('logs')
            if checkpoint:
                saver.restore(sess, checkpoint)
            for i in range(len(testlist0)):
                batch_data, batch_label = batch(testlist0, 1)
                logit = sess.run(out, feed_dict={X: batch_data})  # label 예측
                predictlist += logit
        print("########## Youtube Censorship ######################")
        print("===Section_0============================= 10%")
        print(predictlist)
        print(predictListNaming(predictlist))
        lstResult.append(predictListNaming(predictlist))
        num += 1

    if (num == 1) :
        acc = 0
        predictlist = [[0, 0, 0]]
        with tf.Session(graph=g) as sess:
            sess.run(tf.global_variables_initializer())
            checkpoint = tf.train.latest_checkpoint('logs')
            if checkpoint:
                saver.restore(sess, checkpoint)
            for i in range(len(testlist1)):
                batch_data, batch_label = batch(testlist1, 1)
                logit = sess.run(out, feed_dict={X: batch_data})  # label 예측
                acc += 1
                predictlist += logit
        print("===Section_1============================= 20%")
        print(predictlist)
        print(predictListNaming(predictlist))
        lstResult.append(predictListNaming(predictlist))
        num += 1

    if (num == 2) :
        acc = 0
        predictlist = [[0, 0, 0]]
        with tf.Session(graph=g) as sess:
            sess.run(tf.global_variables_initializer())
            checkpoint = tf.train.latest_checkpoint('logs')
            if checkpoint:
                saver.restore(sess, checkpoint)
            for i in range(len(testlist2)):
                batch_data, batch_label = batch(testlist2, 1)
                logit = sess.run(out, feed_dict={X: batch_data})  # label 예측
                acc += 1
                predictlist += logit
        print("===Section_2============================= 30%")
        print(predictlist)
        print(predictListNaming(predictlist))
        lstResult.append(predictListNaming(predictlist))
        num += 1

    if (num == 3) :
        acc = 0
        predictlist = [[0, 0, 0]]
        with tf.Session(graph=g) as sess:
            sess.run(tf.global_variables_initializer())
            checkpoint = tf.train.latest_checkpoint('logs')
            if checkpoint:
                saver.restore(sess, checkpoint)
            for i in range(len(testlist3)):
                batch_data, batch_label = batch(testlist3, 1)
                logit = sess.run(out, feed_dict={X: batch_data})  # label 예측
                acc += 1
                predictlist += logit
        print("===Section_3============================= 40%")
        print(predictlist)
        print(predictListNaming(predictlist))
        lstResult.append(predictListNaming(predictlist))
        num += 1

    if (num == 4) :
        acc = 0
        predictlist = [[0, 0, 0]]
        with tf.Session(graph=g) as sess:
            sess.run(tf.global_variables_initializer())
            checkpoint = tf.train.latest_checkpoint('logs')
            if checkpoint:
                saver.restore(sess, checkpoint)
            for i in range(len(testlist4)):
                batch_data, batch_label = batch(testlist4, 1)
                logit = sess.run(out, feed_dict={X: batch_data})  # label 예측
                acc += 1
                predictlist += logit
        print("===Section_4============================= 50%")
        print(predictlist)
        print(predictListNaming(predictlist))
        lstResult.append(predictListNaming(predictlist))
        num += 1

    if (num == 5) :
        acc = 0
        predictlist = [[0, 0, 0]]
        with tf.Session(graph=g) as sess:
            sess.run(tf.global_variables_initializer())
            checkpoint = tf.train.latest_checkpoint('logs')
            if checkpoint:
                saver.restore(sess, checkpoint)
            for i in range(len(testlist5)):
                batch_data, batch_label = batch(testlist5, 1)
                logit = sess.run(out, feed_dict={X: batch_data})  # label 예측
                acc += 1
                predictlist += logit
        print("===Section_5============================= 60%")
        print(predictlist)
        print(predictListNaming(predictlist))
        lstResult.append(predictListNaming(predictlist))
        num += 1

    if (num == 6) :
        acc = 0
        predictlist = [[0, 0, 0]]
        with tf.Session(graph=g) as sess:
            sess.run(tf.global_variables_initializer())
            checkpoint = tf.train.latest_checkpoint('logs')
            if checkpoint:
                saver.restore(sess, checkpoint)
            for i in range(len(testlist6)):
                batch_data, batch_label = batch(testlist6, 1)
                logit = sess.run(out, feed_dict={X: batch_data})  # label 예측
                acc += 1
                predictlist += logit
        print("===Section_6============================= 70%")
        print(predictlist)
        print(predictListNaming(predictlist))
        lstResult.append(predictListNaming(predictlist))
        num += 1

    if (num == 7) :
        acc = 0
        predictlist = [[0, 0, 0]]
        with tf.Session(graph=g) as sess:
            sess.run(tf.global_variables_initializer())
            checkpoint = tf.train.latest_checkpoint('logs')
            if checkpoint:
                saver.restore(sess, checkpoint)
            for i in range(len(testlist7)):
                batch_data, batch_label = batch(testlist7, 1)
                logit = sess.run(out, feed_dict={X: batch_data})  # label 예측
                acc += 1
                predictlist += logit
        print("===Section_7============================= 80%")
        print(predictlist)
        print(predictListNaming(predictlist))
        lstResult.append(predictListNaming(predictlist))
        num += 1

    if (num == 8) :
        acc = 0
        predictlist = [[0, 0, 0]]
        with tf.Session(graph=g) as sess:
            sess.run(tf.global_variables_initializer())
            checkpoint = tf.train.latest_checkpoint('logs')
            if checkpoint:
                saver.restore(sess, checkpoint)
            for i in range(len(testlist8)):
                batch_data, batch_label = batch(testlist8, 1)
                logit = sess.run(out, feed_dict={X: batch_data})  # label 예측
                acc += 1
                predictlist += logit
        print("===Section_8============================= 90%")
        print(predictlist)
        print(predictListNaming(predictlist))
        lstResult.append(predictListNaming(predictlist))
        num += 1

    if (num == 9) :
        acc = 0
        predictlist = [[0, 0, 0]]
        with tf.Session(graph=g) as sess:
            sess.run(tf.global_variables_initializer())
            checkpoint = tf.train.latest_checkpoint('logs')
            if checkpoint:
                saver.restore(sess, checkpoint)
            for i in range(len(testlist)):
                batch_data, batch_label = batch(testlist9, 1)
                logit = sess.run(out, feed_dict={X: batch_data})  # label 예측
                acc += 1
                predictlist += logit
        print("===Section_9============================= 100%")
        print(predictlist)
        print(predictListNaming(predictlist))
        lstResult.append(predictListNaming(predictlist))
        num += 1

    return lstResult