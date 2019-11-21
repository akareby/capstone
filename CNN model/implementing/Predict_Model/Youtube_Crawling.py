#
# filename : Youtube_Crawling.py
# history
# =============================
# 20190705 v.0.0.0 초안 작성 강대훈
# 20190705 v.0.0.1 주석 작성 강대훈
# 20190828 v.1.0.0 매개변수를 받아 실행할 수 있도록 수정    김한동
# =============================
# description
# url을 입력받고 프레임의 1/20배 만큼 저장
# 이 후 10개의 경로에 저장
#
import os
import cv2, pafy
import shutil

def main(url):

    for i in range(10):
        i_num = str(i)
        # path = "C:/Users/Michael/PycharmProjects/Capstone_Project/predict/"
        path = "predict/"
        if os.path.isdir(path + i_num + "/"):
            shutil.rmtree(path + i_num)
            os.mkdir(path + i_num)
        else:
            os.mkdir(path + i_num)

    thumbnail= 'img.youtube.com/vi/' + url.split('=')[1] + '/' + 'hqdefault.jpg'
    video = pafy.new(url)
    print('제목 :', video.title)
    print('평점 :', video.rating)
    print('시간 :', video.duration)
    print('썸네일 url :', thumbnail)

    count = 0                                                                   # 사진 번호
    best = video.getbest(preftype = 'webm')                                     # 이걸로 url에 있는 동영상 정보를 얻어옴
    # fpath = "C:/Users/Michael/PycharmProjects/Capstone_Project/pre_predict/"    # 초기 데이터 저장 경로
    fpath = "pre_predict/"
    cap = cv2.VideoCapture(best.url)                                            # 캡처 시작

    while cap.isOpened():
        ret,frame = cap.read()
        if not ret:                                                             # 캡처가 끝나면 브레이크
            break
        if(int(cap.get(1)) % 20 == 0):                                          # 기존 프레임보다 20배 빨리
            cv2.imshow('window-name',frame)                                     # 화면 보여줌
            cv2.imwrite(os.path.join(fpath + "frame%d.jpg")% count, frame)      # 저장
            count = count + 1
            if cv2.waitKey(10) & 0xFF == ord('q'):                              # 중간에 q버튼 누르면 종료
                break
    cv2.destroyAllWindows()                                                     # 브레이크 이후 화면창 종료

    # gpath ="C:/Users/Michael/PycharmProjects/Capstone_Project/predict/"          # 데이터 10분할 저장 경로
    gpath = "predict/"
    for i in range(count):                                                      # count를 10분할 해서 옮기는 작업임.
        name = str(gpath)                                                       # gpath를 string으로
        full_file_name = os.path.join(fpath + "frame%d.jpg")% i
        if i<int(count*0.1):
            shutil.move(full_file_name, name+ '0')
        elif i>=int(count*0.1) and i<int(count*0.2):
            shutil.move(full_file_name, name + '1')
        elif (i >= int(count*0.2)) and (i < int(count*0.3)):
            shutil.move(full_file_name, name + '2')
        elif (i >= int(count*0.3)) and (i < int(count*0.4)):
            shutil.move(full_file_name, name + '3')
        elif (i >= int(count*0.4)) and (i < int(count*0.5)):
            shutil.move(full_file_name, name + '4')
        elif (i >= int(count*0.5)) and (i < int(count*0.6)):
            shutil.move(full_file_name, name + '5')
        elif (i >= int(count*0.6)) and (i < int(count*0.7)):
            shutil.move(full_file_name, name + '6')
        elif (i >= int(count*0.7)) and (i < int(count*0.8)):
            shutil.move(full_file_name, name + '7')
        elif (i >= int(count*0.8)) and (i < int(count*0.9)):
            shutil.move(full_file_name, name + '8')
        elif(i >= int(count*0.9)) and (i < count):
            shutil.move(full_file_name, name + '9')
