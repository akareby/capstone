#
# filename : mean_RGB.py
# history
# =============================
# 20190515 v.0.0.0 초안 작성 김한동
# 20190516 v.0.0.1 주석 작성 김한동
# 20190517 v.0.0.2 변경된 폴더명 코드에 반영 김한동
# =============================
# description
# 장르별로 분류된 이미지의 csv 값을 읽어 각 이미지의 RGB 평균 csv를 작성하는 코드
# RGB 데이터 피쳐가 유효한 지 확인하기 위한 코드
#
# TODO :: 너무 오래 걸린다.. 개선 방법이 없을까?
#

import numpy as np
import csv
import os

lstGenre = ['Sports', 'Musical', 'History', 'Music', 'Thriller', 'Family',  'Comedy', \
            'Short', 'Film-Noir', 'Horror', 'Talk-Show', 'Sci-Fi', 'Adult', 'Animation', \
            'Mystery', 'War', 'Action', 'Crime', 'Documentary', 'Biography', 'Drama', \
            'Adventure', 'Fantasy', 'nan', 'Western', 'Romance']

for index in range(6, len(lstGenre)):
    print(lstGenre[index] + ' processing...')
    data = np.loadtxt('Results/RGBResults/' + lstGenre[index] + 'Info.csv', delimiter=',', encoding='UTF8')

    DATA_ROW_SIZE = int(data.size / 3)

    redInfo = data[:, 0]
    greenInfo = data[:, 1]
    blueInfo = data[:, 2]

    f = open('Results/MeanResults/' + lstGenre[index] + 'RGB.csv', 'w', encoding='utf-8', newline='')
    writer = csv.writer(f)

    for i in range(0, len(os.listdir('ClassificationDataFeatures/' + str(index+1)))):
        redSum = 0
        greenSum = 0
        blueSum = 0

        for j in range(0, int(DATA_ROW_SIZE/len(os.listdir('ClassificationDataFeatures/' + str(index+1))))):
            redSum += redInfo[j + int(DATA_ROW_SIZE/len(os.listdir('ClassificationDataFeatures/' + str(index+1))) * i)]
            greenSum += greenInfo[j + int(DATA_ROW_SIZE/len(os.listdir('ClassificationDataFeatures/' + str(index+1))) * i)]
            blueSum += blueInfo[j + int(DATA_ROW_SIZE/len(os.listdir('ClassificationDataFeatures/' + str(index+1))) * i)]

        redMean = redSum / int(DATA_ROW_SIZE/len(os.listdir('ClassificationDataFeatures/' + str(index+1))))
        greenMean = greenSum / int(DATA_ROW_SIZE/len(os.listdir('ClassificationDataFeatures/' + str(index+1))))
        blueMean = blueSum / int(DATA_ROW_SIZE/len(os.listdir('ClassificationDataFeatures/' + str(index+1))))

        writer.writerow([redMean, greenMean, blueMean])
        print(redMean, greenMean, blueMean)

        redMean = 0
        greenMean = 0
        blueMean = 0

    f.close()
    print(lstGenre[index] + 'Finish')