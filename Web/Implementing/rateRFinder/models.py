# filename : models.py

# history
# 20190902     v.0.0.0    초안 작성                                 김한동
# 20190904     v.0.1.0    관리자화면 출력 메세지 수정                    김한동
# 20190905     v.0.1.1    TODO 항목 추가                            김한동
# 20190909     v.1.0.0    model 최종본                              김한동

# discription
# model 정보

from django.db import models

# Create your models here.

class UrlSaver(models.Model):

    url = models.URLField('Youtube URL')

    def __str__(self):
        return "id : " + str(self.id) + ", URL : " + self.url
