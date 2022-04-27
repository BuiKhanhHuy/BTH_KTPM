from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../driver/chromedriver.exe")
driver.get("https://vnexpress.net")
driver.implicitly_wait(20)

articles = driver.find_elements(By.CSS_SELECTOR, 'article.item-news')

for article in articles:
    try:
        title = article.find_element(By.CSS_SELECTOR, "p.description > a").get_attribute('title')
        link = article.find_element(By.CSS_SELECTOR, 'p.description > a').get_attribute('href')
        description = article.find_element(By.CSS_SELECTOR, 'p.description > a').text
        print('Title: ', title)
        print('Description: ', description)
        print('Link: ', link)
        print('\n')
    except NoSuchElementException:
        print("Error 404")

driver.close()
