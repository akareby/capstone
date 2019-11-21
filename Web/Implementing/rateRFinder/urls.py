# filename : rateRFinder/urls.py

# history
# 20190902     v.0.0.0    초안 작성                                 김한동
# 20190903     v.0.1.0    기본 페이지 경로 설정, 상세정보 경로 수정        김한동
# 20190905     v.1.0.0    상세정보 구현 완료                          김한동

# discription
# url 연결

from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', UrlCreateView.as_view(), name='add'),
    path('detail/', views.UrlDetail, name='detail'),
]