### 매번 수업 들어가기 귀찮아서 만든 수업 들어가기 자동화 프로그램

1. [크롬 드라이버 버전 확인](chrome://settings/help)
2. [크롬 버전에 맞는 드라이버 다운로드](https://chromedriver.chromium.org/downloads)

### 실행
1. 가상환경 설정 : `python -m venv [가상환경 이름]` -> activate
2. 패키지 설치 : `pip install -r requirements.txt` 실행
3. 클래스 입력
    ```python
    ex)
    # 수업 선언
    uni_class1 = 'http://hongik.webex.com/meet/'       # 수업1
    uni_class2 = ''     # 수업2
    uni_class3 = ''     # 수업3
    
    # 요일별 수업 : '(수업, 시작시간, 수업시간)'
    class_mon = [[uni_class1, 11, 1], [uni_class2, 14, 1]]      # 월요일 수업
    class_tues = [[], []]       # 화요일 수업
    class_wed = [[], []]        # 수요일 수업
    ```
4. `python openclass.py` 실행
