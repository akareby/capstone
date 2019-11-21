# filename : views.py

# history
# 20190902     v.0.0.0    초안 작성                                 김한동
# 20190903     v.0.1.0    UrlCreateView 추가, UrlDetailView 수정    김한동
# 20190905     v.0.2.0    함수형 뷰 UrlDetail 추가                   김한동
# 20190909     v.1.0.0    CNN 모델과 통합 진행                        김한동
# 20190910     v.1.1.0    모델에서 결과를 받아서 context로 전달          김한동
# 20190915     v.1.2.0    저작권 보호 영상을 걸러내기 위한 부분 추가        김한동
# 20190916     v.1.3.0    결과 분류 고도화                            김한동
# discription
# 기능에 필요한 View 구현

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render

from rateRFinder.models import UrlSaver

from CNN import Test
from CNN import Youtube_Crawling

# Create your views here.
class UrlCreateView(CreateView):

    model = UrlSaver
    fields = ['url']

    # 성공 시 detail로 이동
    success_url = reverse_lazy('detail')
    template_name_suffix = '_create'

def UrlDetail(request):

    # 입력받은 url을 잘 가져온다.
    url = request.POST.get('url')

    # CNN 모델 실행
    result = Test.main(url)

    if result == 333:
        context = {
            'url': url,
        }
        return render(request, 'rateRFinder/urlsaver_error.html', context)
    else:
        title = result[0]
        rating = result[1]
        duration = result[2]
        imgUrl = "https://" + result[3]

        step0 = result[4]
        step1 = result[5]
        step2 = result[6]
        step3 = result[7]
        step4 = result[8]
        step5 = result[9]
        step6 = result[10]
        step7 = result[11]
        step8 = result[12]
        step9 = result[13]

        horrorCount = 0
        brutalCount = 0
        adultCount = 0
        normalCount = 0
        maxCount = 0

        totalResult = ''

        for i in range(4, 13):
            if result[i] == '공포':
                horrorCount += 1
            elif result[i] == '잔인':
                brutalCount += 1
            elif result[i] == '음란':
                adultCount += 1
            else:
                normalCount += 1

        if normalCount >= 5:
            totalResult = '일반'
        else:
            if horrorCount < brutalCount:
                maxCount = brutalCount
                if maxCount < adultCount:
                    totalResult = '음란'
                else:
                    totalResult = '잔인'
            else:
                maxCount = horrorCount
                if maxCount < adultCount:
                    totalResult = '음란'
                else:
                    totalResult = '공포'

        context = {
            'url' : url,
            'title' : title,
            'rating' : rating,
            'duration' : duration,
            'imgUrl' : imgUrl,
            'step0' : step0,
            'step1' : step1,
            'step2': step2,
            'step3': step3,
            'step4': step4,
            'step5': step5,
            'step6': step6,
            'step7': step7,
            'step8': step8,
            'step9': step9,
            'totalResult' : totalResult,
        }

        return render(request, 'rateRFinder/urlsaver_detail.html', context)
