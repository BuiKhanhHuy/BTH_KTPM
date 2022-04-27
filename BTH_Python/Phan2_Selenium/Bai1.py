from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe')
driver.get('https://www.google.com/')

inp = input("Nhap du lieu tim kiem: ")

# nhap du lieu tim kiem
inp_tag = driver.find_element(by=By.NAME, value='q')
inp_tag.send_keys(inp)
inp_tag.submit()

# lay du lieu
posts = driver.find_elements(by=By.CLASS_NAME, value='g')
for post in posts:
    text = post.find_element(by=By.TAG_NAME, value='a').text
    url = post.find_element(by=By.TAG_NAME, value='a').get_attribute('href')
    print('+ Tittle:', text)
    print('+ Url:', url)
    print('\n')

driver.close()
