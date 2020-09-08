# Introduction

### 2019년 상명대학교 캡스톤 디자인

### CNN을 이용한 유튜브 영상 유해등급 판독  

<br/>

|     팀원     |                       역할                        |          책임                        |
| :---------: | :----------------------------------------------: | :---------------------------------: |
|  김한동  |     PM &#128081;, 웹 디자인 및 설계     |   프로젝트와 관련된 모든 활동 담당 및 관리, UI 설계, 서버 설계 및 관리 |
|  강진우  | 메인 코더 |  AI 개발의 메인 코더   |
|  강대훈  |  서브 코더, 데이터 관리자  |  데이터 추출 및 저장 관련 코더  |
|  김영완  |     산출물 관리자          | 프로젝트에서 나오는 모든 산출물을 관리        |

                     

<br/>
  
#### **Background**  
<br/>
<img src="/test_img/1.PNG" width="50%" height="50%">  

- 유튜브에 특별한 인증이 필요 없이도 볼 수 있는 유해한 동영상들이 많이 있다




#### Data Set
<br/>
<img src="/test_img/2.PNG" width="50%" height="50%"> 

- '공포', '음란', '잔인'이라는 주제로한 데이터  
- 선정성을 가진 데이터 약 1500개, 비선정성을 가진 데이터 약 1500개

#### CNN
<br/>
<img src="/test_img/4.PNG" width="50%" height="50%">

- 프로그램 구조  

<img src="/test_img/5.PNG" width="50%" height="50%">

- 3 Layers, Batch Size = 300, Epoch = 300

#### Web
<br/>
<img src="/test_img/6.PNG" width="50%" height="50%">
<img src="/test_img/7.PNG" width="50%" height="50%">

#### 시연
<br/>
<img src="/test_img/8.PNG" width="50%" height="50%">

- 콘솔창에서 데이터를 판별하는 작업  
<img src="/test_img/9.PNG" width="50%" height="50%">

- 일반 동영상  
<br/>

<img src="/test_img/10.PNG" width="50%" height="50%">
<img src="/test_img/11.PNG" width="50%" height="50%">

- 선정성이 있는 동영상
