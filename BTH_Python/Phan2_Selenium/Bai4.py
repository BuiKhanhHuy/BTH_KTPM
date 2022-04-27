from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe')
driver.get('https://vi-vn.facebook.com/')

driver.find_element(by=By.XPATH,
                    value='/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]/a').click()

driver.implicitly_wait(10)

driver.find_element(by=By.NAME, value='lastname').send_keys('Huy')
driver.find_element(by=By.NAME, value='firstname').send_keys('Bui Khanh')
driver.find_element(by=By.NAME, value='reg_email__').send_keys('khuy220@gmail.com')
driver.find_element(by=By.NAME, value='reg_email_confirmation__').send_keys('khuy220@gmail.com')
driver.find_element(by=By.NAME, value='reg_passwd__').send_keys('Huy_123456789')

day = Select(driver.find_element(By.ID, value='day'))
day.select_by_value('27')
month = Select(driver.find_element(By.ID, value='month'))
month.select_by_value('2')
year = Select(driver.find_element(By.ID, value='year'))
year.select_by_value('2001')

driver.find_elements(by=By.NAME, value='sex')[1].click()

driver.find_element(by=By.NAME, value='websubmit').click()

driver.close()
