import json
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="../driver/chromedriver.exe")

driver = webdriver.Chrome(service=service)
driver.get("https://lms.ou.edu.vn/")
driver.implicitly_wait(20)

# dang nhap hoc ky
driver.find_element(By.CLASS_NAME, 'main-btn').click()

# dang nhap
driver.find_element(By.CSS_SELECTOR, 'button.login100-form-btn').click()

# lay thong tin username, password
# nhap thong tin username, password vao file user.json
with open('./user.json', 'r') as f:
    user = json.load(f)

# nhap thong tin dang nhap
user_type = Select(driver.find_element(By.ID, 'form-usertype'))
user_type.select_by_value('svcq')

driver.find_element(By.ID, "form-username").send_keys(user.get('username'))
driver.find_element(By.ID, "form-password").send_keys(user.get('password'))
driver.find_element(By.CSS_SELECTOR, 'button.m-loginbox-submit-btn').click()

courses = driver.find_elements(By.CSS_SELECTOR, 'div.dashboard-card > div.card-body > div > div > a span.multiline')

for course in courses:
    print(course.text)

driver.close()




