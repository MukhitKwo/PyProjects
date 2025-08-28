
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import sqlite3


def Books():

    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get('http://books.toscrape.com/')

    con = sqlite3.connect("projects/books/books.db")
    cursor = con.cursor()

    library = []

    while True:
        content = driver.find_element(By.CSS_SELECTOR, "ol.row")
        articles = content.find_elements(By.TAG_NAME, "article")

        for article in articles:

            name_tag = article.find_elements(By.TAG_NAME, "a")
            name_tag[1].click()

            book = driver.find_element(By.CSS_SELECTOR, "div.col-sm-6.product_main")

            name = book.find_element(By.TAG_NAME, "h1").text
            # print("Name:", name)

            price = book.find_element(By.CSS_SELECTOR, "p.price_color").text
            price = round(float(price.lstrip("£"))*1.15, 2)
            # print("Price:", price)

            stock = book.find_element(By.CSS_SELECTOR, "p.instock").text.split()
            stock = int(stock[2].lstrip("("))
            # print("Stock:", stock)

            rating = book.find_element(By.CSS_SELECTOR, "p.star-rating").get_attribute("class").split()[1]
            rating = ratingInt(rating)
            # print("Rating:", rating)

            bookInfo = []
            bookInfo.append(name)
            bookInfo.append(price)
            bookInfo.append(stock)
            bookInfo.append(rating)
            print(bookInfo)

            # library.append(bookInfo)

            driver.back()

            cursor.execute("insert into books (title, price, stock, rating) values (?,?,?,?)", bookInfo)
            # cursor.execute("delete from books")
            con.commit()

        try:

            button = driver.find_element(By.CSS_SELECTOR, "li.next a")
            button.click()
            print("Next page")
        except NoSuchElementException:
            break


#     cursor.execute("""
# CREATE TABLE IF NOT EXISTS books (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     title TEXT,
#     price REAL,
#     stock INTEGER,
#     rating INTEGER
# )
# """)
    

    # cursor.execute("DROP TABLE IF EXISTS books")
    # cursor.executemany("insert into books (title, price, stock, rating) values (?,?,?,?)", library)
    # con.commit()

    con.close()


def ratingInt(rating):
    match rating:
        case "One":
            return 1
        case "Two":
            return 2
        case "Three":
            return 3
        case "Four":
            return 4
        case "Five":
            return 5


if __name__ == "__main__":
    Books()
