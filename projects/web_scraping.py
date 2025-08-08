# from time import sleep
# import requests  # used for gettings raw data
# from bs4 import BeautifulSoup

# response = requests.get("https://www.scrapethissite.com/")

# print(response.status_code)  # returns status (200 good)
# # print(response.content) # returns data unformated

# soup = BeautifulSoup(response.content, "html.parser")  # Converts HTML into a searchable object

# # print(soup.prettify()) # formats the data for easier reading

# # finds the FIRST div with class article--viewer_content
# content_div = soup.find("div", id="homepage")

# print(content_div.prettify())

# # if content_div:
# #     for paragraph in content_div.find_all("p"):  # finds all <p> tags inside that div
# #         print(paragraph.text.strip())  # prints the text of each paragraph, with whitespace stripped
# # else:
# #     print("No article content found")


from turtle import title
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
