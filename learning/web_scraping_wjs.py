
# from turtle import title
from requests import options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

driver.get('http://books.toscrape.com/')

time.sleep(2)

titles = driver.find_elements(By.CSS_SELECTOR, 'article.product_pod h3 a')
for title in titles:
    print(title.get_attribute('title'))


driver.quit()
