from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver = webdriver.Chrome('./chromedriver')
driver.get('http://hecs.hdel.co.kr/webfw/html/nawlogon.html')


# HCCC ID PW
userId = ["2030152"]
password = ["hdel1234!"]
StartDate = ["20220101"]
EndDate = ["20220131"]

# 다음 세 줄이 기본 패턴 코드: ID 넣기
# WebDriverWait(driver, 최대 기다리는 시간).until(EC.presence_of_element_located((By.CSS_SELECTOR, CSS Selector 태그)))
login_id = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#edtLoginId")))
login_id.clear()  # 입력창의 경우, 사전에 작성되어 있는 텍스트를 삭제
login_id.send_keys(userId)  # 내가 넣고자 하는 텍스트 삽입

# 다음 세 줄이 기본 패턴 코드: 패스워드 넣기
login_pw = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#edtLoginPswd")))
login_pw.clear()
login_pw.send_keys(password)

# 버튼 클릭시는 다음 두 줄: 로그인 버튼 누르기
button = WebDriverWait(driver, 3).until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "#btnsearch")))
button.click()
time.sleep(1.5)  # 로그인 후의 페이지 로딩을 위해, 1초정도 기다리면 좋음


# MENU 클릭
button = WebDriverWait(driver, 3).until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "#westResizeContent > span")))
button.click()
time.sleep(1.5)

# 전체메뉴 활성화 클릭
posting = driver.find_element_by_xpath('//*[@id="menuAll"]/span')
posting.click()
time.sleep(1.5)

# 일일작업일지 클릭
Report = driver.find_element_by_xpath(
    '//html/body/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/li[6]/ul/li[6]/span')
Report.click()
time.sleep(1.5)

# 사무소 클릭
Office = driver.find_element_by_xpath(
    '//html/body/div[1]/header/form/div/div[1]/div/table/tbody/tr[1]/td[1]/input[1]')
Office.click()

Insert_date = WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located(
    (By.XPATH, "//html/body/div[1]/header/form/div/div[1]/div/table/tbody/tr[1]/td[1]/input[1]")))
Insert_date.send_keys(StartDate)
time.sleep(1.5)


# # 조회기간 종료일 클릭
# posting = driver.find_element_by_xpath(
#     '/html/body/div[1]/header/form/div/div[1]/div/table/tbody/tr[1]/td[1]/input[2]')
# posting.click()
# time.sleep(1.5)

# 조회기간 종료일 입력


driver.quit()
