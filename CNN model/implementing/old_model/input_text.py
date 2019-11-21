#
# filename : input_text.py
# history
# =============================
# 20190705 v.0.0.0 초안 작성 강진우
# 20190705 v.0.0.1 주석 작성 강진우
# =============================
# description
#
#
import os
f1 = open("train.txt", 'w')
f2 = open("eval.txt", 'w')

def train_text(dataset, number):

    num = str(number)
    path_dir = dataset + '/' + num
    file_list = os.listdir(path_dir)
    print("file_list: {}".format(file_list))

    for i, j in enumerate(file_list):
        data = dataset + "\\" + num + "\\" + file_list[i] + " " + num + "\n"
        f1.write(data)

def eval_text(dataset, number):

    num = str(number)
    path_dir = dataset + '/' + num
    file_list = os.listdir(path_dir)
    print("file_list: {}".format(file_list))

    for i, j in enumerate(file_list):
        data = dataset + "\\" + num + "\\" + file_list[i] + " " + num + "\n"
        f2.write(data)

for i in range(10):
    train_text('train', i)
    eval_text('eval', i)

f1.close()
f2.close()
# train\0\27653.jpg 0
