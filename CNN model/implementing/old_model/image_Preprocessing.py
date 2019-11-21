#
# filename : image_Preprocessing.py
# history
# =============================
# 20190705 v.0.0.0 초안 작성 강진우
# 20190705 v.0.0.1 주석 작성 강진우
# 20190707 v.0.0.2 전체 shape 동일하게 조정(182,268,3)하기 위한 resize 구성
# =============================
# description
# TODO :: Image Preprocessing (by OpenCV) 을 통한 feature 검출을 통해 accuracy 개선
#
#
#

from PIL import Image
import os

def turn_to_RGB(dataset, number):
    num = str(number)
    path_dir = dataset + '/' + num
    file_list = os.listdir(path_dir)
    for i, j in enumerate(file_list):
        real_dir = dataset + '/' + num + '/' + file_list[i]
        img = Image.open(real_dir).convert('RGB')
        img.save(real_dir)
        resize_image = Image.open(real_dir).resize((182, 268))
        resize_image.save(real_dir)

for i in range(10):
    turn_to_RGB('train', i)
    turn_to_RGB('eval', i)
