## KM_Portal
> 계명대학교 하계방학 해커톤 최우수(1등) 수상  
4조 계명포털 - 계대 학생들을 위한 커뮤니티

<img width="205" alt="교내캡스톤 최우수" src="https://user-images.githubusercontent.com/74866067/229506212-2e6b69e8-efbd-4df7-ab8b-7c3d7ea1c5b9.png">


<br>
<br>

<br>

## 사용 기술스택

```
Back : python3, Django
Front : HTML5, CSS3, BootStrap5, JavaScript
```

<br>
<br>

## API

* #### [카카오 맵 api](#맵)

 -학교 지도와 주요 시설을 표시하고 마커에 꿀팁 정보 등 확인
 
 ```
 var marker1 = new kakao.maps.Marker({
    map: map, 
    position: new kakao.maps.LatLng(35.85534833720473, 128.48569272749938)
});
// 커스텀 오버레이에 표시할 컨텐츠 입니다
var content1 = '<div class="wrap">' + 
            '    <div class="info">' + 
            '        <div class="title">' + 
            '            봉경관(사)' + 
            '            <div class="close" onclick="closeOverlay1()" title="닫기"></div>' + 
            '        </div>' + 
            '        <div class="body">' + 
            '            <div class="img">' +
            '                <img src="/static/images/map/1.jpg" width="73" height="70">' +
            '           </div>' + 
            '            <div class="desc">' + 
            '                <div class="ellipsis">사회과학대학</div>' + 
            '                <div class="jibun ellipsis">행정실 : 053-580-5392</div>' + 
            '            </div>' + 
            '        </div>' + 
            '    </div>' +    
            '</div>';
// 마커 위에 커스텀오버레이를 표시합니다
var overlay1
// 마커를 클릭했을 때 커스텀 오버레이를 표시합니다
kakao.maps.event.addListener(marker1, 'click', function() {
    overlay1 = new kakao.maps.CustomOverlay({
    content: content1,
    map: map,
    position: marker1.getPosition()       
});
});
// 커스텀 오버레이를 닫기 위해 호출되는 함수입니다 
function closeOverlay1() {
    overlay1.setMap(null);     
}
 ```

* #### [웹 스크래핑](#알리미)

-학교와 관련된 공지, 정보 등을 크롤링해서 한눈에 확인 가능

-bs4 이용

```
def check_standard():
    data = {}
    url = "https://www.kmu.ac.kr/uni/main/page.jsp?mnu_uid=143&"
    res = requests.get(url)
    xml = res.text
    n = 1

    soup = BeautifulSoup(xml, 'html.parser')
    datalist = soup.find('tbody').findAll('tr')
    for i in datalist:
        data[f"st_sub{n}"] = (i.find('td', class_='subject').text)
        data[f"st_href{n}"] = (i.find('td', class_='subject').find('a')["href"])
        data[f"st_wrt{n}"] = (i.find('td', class_='writer').text)
        data[f"st_date{n}"] = (i.find('td', class_='date').text)
        n = n+1
        if n is 10:
            break;
    return data
```

* #### CRUD

-게시판 별 구분되는 모델

-작성,읽기,수정,삭제 (로그인 확인, 페이징) 등

```
@login_message_required
def free_write(request): # 수정 : 함수이름 free 추가 redirect /board >> /board/free 변경
    if request.method == "POST":
        user = request.user
        title = request.POST['title']
        content = request.POST['content']
        post = FreePosting(user=user, title=title, content=content, date=timezone.now()) # 수정 : Post >> FreePosting
        post.save()
        return redirect('/board/free')
    else:
        form = PostForm()
    return render(request, "board/write.html", {'form': form,'url':'free'})

def free_index(request): # 수정함 : context url free 추가 함수이름 free추가 postList, postNum Post >> FreePosting 변경
        # 게시물 목록 출력
    postList = FreePosting.objects.all().order_by('-id')
    postNum = FreePosting.objects.count()
        #페이징처리
    page = request.GET.get('page', '1')
    paginator = Paginator(postList, '10')
    page_obj = paginator.page(page)
    context = {'postList': postList ,'postNum':postNum,'page_obj':page_obj,'url':'free','boardname':'자유'} 
    return render(request, 'board/list.html', context)
```


<br>
<br>

## 화면구성

* #### 메인화면
<img width="1280" alt="메인" src="https://user-images.githubusercontent.com/74866067/139051474-addbb342-c80e-4813-b52d-18a4d35e7266.PNG">


* #### 맵
<img width="507" alt="맵캡처" src="https://user-images.githubusercontent.com/74866067/139052937-918e5f77-041f-492e-b3b3-a3da09b8d670.PNG">


* #### 게시판
<img width="631" alt="게시판캡처" src="https://user-images.githubusercontent.com/74866067/139051738-3a44b8c5-6528-4392-a034-805a857fcf3c.PNG">


* #### 게시글
<img width="630" alt="게시글캡처" src="https://user-images.githubusercontent.com/74866067/139051779-527da519-92ea-451f-b2de-ea46709e2178.PNG">


* #### 질문게시판
<img width="1183" alt="질문이캡처" src="https://user-images.githubusercontent.com/74866067/139051855-d2d35ca9-1392-44d2-a97a-3d8a8c598b77.PNG">


* #### 질문 글, 채택
<img width="368" alt="질문글캡처" src="https://user-images.githubusercontent.com/74866067/139051902-efb26395-ec56-40e1-bf9f-8a81ad2876fa.PNG">
<img width="372" alt="질문글채택캡처" src="https://user-images.githubusercontent.com/74866067/139051908-7b099d97-1f31-4e51-8f1d-2b9bf2a164cd.PNG">


* #### 알리미

<img width="1040" alt="알리미캡처" src="https://user-images.githubusercontent.com/74866067/139051966-885dcc71-d29e-4ef7-b035-9b171c8866e7.PNG">


* #### 회원가입
<img width="661" alt="가입캡처" src="https://user-images.githubusercontent.com/74866067/139052006-947832a5-44bd-44d1-9163-5785eaf6a266.PNG">


* #### 로그인
<img width="237" alt="로그인캡처" src="https://user-images.githubusercontent.com/74866067/139052025-de9374b3-1c68-469a-af63-76edda88b2c5.PNG">

<img width="816" alt="네비캡처" src="https://user-images.githubusercontent.com/74866067/139052043-9ba18c44-882b-41d9-9d24-479f79720cfa.PNG">


* #### 마이페이지
<img width="501" alt="마이페이지캡처" src="https://user-images.githubusercontent.com/74866067/139052058-e00a1c28-4ecb-4e09-812b-97a3fa603623.PNG">
