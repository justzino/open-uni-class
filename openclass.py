from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from datetime import datetime
import sys
import os


chrome_options = Options()
chrome_options.add_argument("--headless")

if getattr(sys, 'frozen', False):
    chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
    # webdriver 설정 (chrome) - Headless 모드
    # browser = webdriver.Chrome(chromedriver_path, options=chrome_options)

    # webdriver 설정 (chrome) - 일반 모드
    browser = webdriver.Chrome(chromedriver_path)
else:
    browser = webdriver.Chrome()

# 크롬 브러우저 내부 대기
browser.implicitly_wait(1)

# 브라우저 사이즈
browser.set_window_size(1920, 1280)

# 수업 선언
uni_class1 = 'http://hongik.webex.com/meet/'       # 수업1
uni_class2 = ''     # 수업2
uni_class3 = ''     # 수업3
uni_class4 = ''     # 수업4
uni_class5 = ''     # 수업5

# 요일별 수업 : '(수업, 시작시간, 수업시간)'
class_mon = [[uni_class1, 11, 1], [uni_class2, 14, 1]]      # 월요일 수업
class_tues = [[], []]
class_wed = [[], []]
class_thur = [[], []]
class_fri = [[], []]


# 수업 입장 (요일별 수업 변수 입력)
def enter_class(class_week):
    for cls in class_week:
        if cls[1]*60 - 20 <= time_now.hour*60 + time_now.minute <= (cls[1] + cls[2])*60 - 20:
            # 페이지 이동
            browser.get(cls[0])


MON, TUE, WED, THUR, FRI, SAT, SUN = 0, 1, 2, 3, 4, 5, 6

# 현재 시간
time_now = datetime.now()

# 요일 확인후 수업 오픈
if time_now.weekday() == MON:
    enter_class(class_mon)
elif time_now.weekday() == TUE:
    enter_class(class_tues)
elif time_now.weekday() == WED:
    enter_class(class_wed)
elif time_now.weekday() == THUR:
    enter_class(class_thur)
elif time_now.weekday() == FRI:
    enter_class(class_fri)
