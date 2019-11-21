#
# filename : Input_text.py
# history
# =============================
# 20190705 v.0.0.0 초안 작성 강진우
# 20190705 v.0.0.1 주석 작성 강진우
# =============================
# description
#
#
#
import os

def eval_text(txtPath, dataset, number):

    num = str(number)
    path_dir = dataset + '/' + num
    file_list = os.listdir(path_dir)

    for i, j in enumerate(file_list):
        # data = dataset + "\\" + num + "\\" + file_list[i] + " " + num + "\n"
        data = dataset + "/" + num + "/" + file_list[i] + " " + num + "\n"    # for Mac
        txtPath.write(data)

def main():
    f = open("predict.txt", 'w')

    for i in range(10):
        eval_text(f, 'CNN/predict', i)

    f.close()
