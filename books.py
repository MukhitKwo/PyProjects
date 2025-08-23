from os import name
import requests
from bs4 import BeautifulSoup
import sqlite3


def Books():

    response = requests.get("https://books.toscrape.com/")

    soup = BeautifulSoup(response.content, "html.parser")

    # print(soup.prettify())

    content_div = soup.find("ol", class_="row")
    articles = content_div.find_all("article")

    for article in articles:

        book = []

        name_tag = article.find_all("a")
        name = name_tag[1]["title"]
        book.append(name)

        price_tag = article.find("p", class_="price_color").text
        price = round(float(price_tag.lstrip("£")) * 1.15, 2)
        book.append(price)

        rating_tag = article.find("p", class_="star-rating")
        rating = ratingInt(rating_tag["class"][1])
        book.append(rating)

        stock_tag = article.find("p", class_="instock availability").text
        stock = inStock(stock_tag.strip())
        book.append(stock)

        print(book)


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


def inStock(stock):
    if stock == "In stock":
        return True
    return False

if __name__=="__main__":
    Books()