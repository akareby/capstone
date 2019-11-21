#
# filename : img_RGB.py
# history
# =============================
# 20190515 v.0.0.0 초안 작성 김한동
# 20190516 v.0.0.1 주석 작성 김한동
# 20190517 v.0.0.2 변경된 폴더명 코드에 반영 김한동
# =============================
# description
# 장르별로 나누어져 있는 폴더에 접근하여 이미지를 읽어 해당 이미지의 pixel값을 csv 파일로 만든다.
#
# TODO :: RGB 특성이 잘 나오지 않을 경우 방법론 생각해보기_idea 1. 사람 형태랑 배경 형태를 따로 구분해서 확인
#

from PIL import Image
import csv
import glob

lstGenre = ['Sports', 'Musical', 'History', 'Music', 'Thriller', 'Family',  'Comedy', \
            'Short', 'Film-Noir', 'Horror', 'Talk-Show', 'Sci-Fi', 'Adult', 'Animation', \
            'Mystery', 'War', 'Action', 'Crime', 'Documentary', 'Biography', 'Drama', \
            'Adventure', 'Fantasy', 'nan', 'Western', 'Romance']

for index in range(0, len(lstGenre)):
    allImages = glob.glob('ClassificationDataFeatures/' + str(index + 1) + '/*.jpg')

    f = open('Results/RGBResults/' + lstGenre[index] + 'Info.csv', 'w', encoding='utf-8', newline='')
    writer = csv.writer(f)

    for fname in allImages:
        img = Image.open(fname)

        w, h = img.size

        for i in range(0, w):
            for j in range(0, h):
                writer.writerow(img.getpixel((i, j)))

        # print(fname)

    f.close()
    print(lstGenre[index] + ' Finish')