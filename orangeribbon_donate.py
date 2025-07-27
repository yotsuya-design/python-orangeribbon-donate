import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

# クレジットカード情報
CARD_NUMBER = "1234567890123456"
CARD_EXPIRES_MONTH = "01"
CARD_EXPIRES_YEAR = "2030"
CARD_NAME = "YAMADA TARO"
CARD_CVV = "1234"

# 寄付者情報
LAST_NAME = "山田"
FIRST_NAME = "太郎"
LAST_NAME_KANA = "山田"
FIRST_NAME_KANA = "タロウ"
ZIP_CODE = "123-4567"
PREFECTURE = "東京都"
ADDRESS_LINE2 = "新宿区新宿123-45"
ADDRESS_LINE3 = "株式会社〇〇"
PHONE_NUMBER = "0312345678"
EMAIL_FULL = "taro@ooo.oo.jp"
# メール確認欄が2分割されているため、@の前後を分けて入力
EMAIL_PART1 = "taro"
EMAIL_PART2 = "oooo.oo.jp"

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

################################################################################
# カートに「寄付」を入れる
################################################################################

driver.get('https://service01-bf02.ebisumart.com/ORANGERIBBON/cart_index.html?request=insert&item_cd=000')

time.sleep(5)

# 注文フォームへ（ご注文手続きボタンをクリック）
driver.find_element(By.CLASS_NAME, 'go').click()

time.sleep(5)

################################################################################
# フォーム入力
################################################################################

driver.find_element(By.ID, "L_NAME").send_keys(LAST_NAME)
driver.find_element(By.ID, "F_NAME").send_keys(FIRST_NAME)
driver.find_element(By.ID, "L_KANA").send_keys(LAST_NAME_KANA)
driver.find_element(By.ID, "F_KANA").send_keys(FIRST_NAME_KANA)

driver.find_element(By.ID, "ZIP").send_keys(ZIP_CODE)
Select(driver.find_element(By.ID, "ADDR1")).select_by_value(PREFECTURE)
driver.find_element(By.ID, "ADDR2").send_keys(ADDRESS_LINE2)
driver.find_element(By.ID, "ADDR3").send_keys(ADDRESS_LINE3)

driver.find_element(By.ID, "TEL").send_keys(PHONE_NUMBER)

driver.find_element(By.ID, "PC_MAIL").send_keys(EMAIL_FULL)
driver.find_element(By.ID, "PC_MAIL_CONFIRM1").send_keys(EMAIL_PART1)
driver.find_element(By.ID, "PC_MAIL_CONFIRM2").send_keys(EMAIL_PART2)

driver.find_element(By.NAME, "KESSAI_ID").click()

Select(driver.find_element(By.ID, "zeus_token_card_expires_month")).select_by_value(CARD_EXPIRES_MONTH)
Select(driver.find_element(By.ID, "zeus_token_card_expires_year")).select_by_value(CARD_EXPIRES_YEAR)
driver.find_element(By.ID, "zeus_token_card_number").send_keys(CARD_NUMBER)
driver.find_element(By.ID, "zeus_token_card_name").send_keys(CARD_NAME)
driver.find_element(By.ID, "zeus_token_card_cvv").send_keys(CARD_CVV)

# 入力内容の確認（内容確認へボタンをクリック）
driver.find_element(By.CLASS_NAME, 'next').click()

time.sleep(5)

################################################################################
# 決済実行
################################################################################

driver.find_element(By.CLASS_NAME, 'next').click()

time.sleep(30)

driver.quit()