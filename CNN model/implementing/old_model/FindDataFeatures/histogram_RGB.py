#
# filename : histogram_RGB.py
# history
# =============================
# 20190521 v.0.0.0 초안 작성 김한동
#
# =============================
# description
# 위협으로 분류한 장르의 데이터 30개와 비위협 분류한 장르 데이터 30개를 선별하여 히스토그램을 그리는 코드
# 통계학에서 모집단이 어떠한 분포를 따르던 표본의 갯수 n이 충분히 크다면(보톹 30 이상) 표본은 정규분포를 따르는 원리를 이용
# 피쳐의 특징을 잡고자 함
# RGB 데이터 피쳐가 유효한 지 확인하기 위한 코드
#
# notice  : csv 파일의 크기가 너무 커서 깃허브에 올리지 못하므로 각자 로컬에서 실행해볼 것
#

import pandas as pd
import matplotlib.pyplot as plt

# 위협으로 분류한 데이터 읽어들이기
# dfThriller = pd.read_csv('Results/RGBResults/ThrillerInfo.csv')
# dfCrime = pd.read_csv('Results/RGBResults/CrimeInfo.csv')
# dfWar = pd.read_csv('Results/RGBResults/WarInfo.csv')

# 위협이 아닌 데이터 읽기
# 애니메이션은 현실과 괴리감이 있을 수 있으므로 제외하는게 어떤가?
# 드라마 자체도 애매할 수 있지만 일단 보자
dfComedy = pd.read_csv('Results/RGBResults/ComedyInfo.csv')
dfDrama = pd.read_csv('Results/RGBResults/DramaInfo.csv')

# 위협 10개 추출
# dfThriller_10 = dfThriller.head(487760)
# dfCrime_10 = dfCrime.head(487760)
# dfWar_10 = dfWar.head(487760)

# 위협 아님에서 15개씩 추출
dfComedy_15 = dfComedy.head(731640)
dfDrama_15= dfDrama.head(731640)

# 색 별 영역을 저장할 리스트 생성
lstRed = []
lstGreen = []
lstBlue = []

for i in range(0, 731640):
    # lstRed.append(dfThriller_10['188'][i])
    # lstGreen.append(dfThriller_10['173'][i])
    # lstBlue.append(dfThriller_10['106'][i])
    lstRed.append(dfComedy_15['2'][i])
    lstBlue.append(dfComedy_15['2'][i])
    lstGreen.append(dfComedy_15['2'][i])

for i in range(0, 731640):
    # lstRed.append(dfCrime_10['81'][i])
    # lstGreen.append(dfCrime_10['155'][i])
    # lstBlue.append(dfCrime_10['158'][i])
    lstRed.append(dfDrama_15['159'][i])
    lstGreen.append(dfDrama_15['100'][i])
    lstBlue.append(dfDrama_15['104'][i])

# for i in range(0, 487760):
    # lstRed.append(dfWar_10['251'][i])
    # lstGreen.append(dfWar_10['252'][i])
    # lstBlue.append(dfWar_10['234'][i])

fig = plt.figure()

ax1 = fig.add_subplot(3, 1, 1)
ax2 = fig.add_subplot(3, 1, 2)
ax3 = fig.add_subplot(3, 1, 3)

ax1.set_title('Red')
# ax1.set_xlabel('degree')
# ax1.set_ylabel('Frequency')

ax2.set_title('Green')
# ax2.set_xlabel('degree')
# ax2.set_ylabel('Frequency')

ax3.set_title('Blue')
# ax3.set_xlabel('degree')
# ax3.set_ylabel('Frequency')

ax1.hist(lstRed, color='r', rwidth=0.7)
ax2.hist(lstGreen, color='g', rwidth=0.7)
ax3.hist(lstBlue, color='b', rwidth=0.7)

plt.show()