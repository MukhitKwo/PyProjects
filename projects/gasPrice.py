from time import sleep
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

response = requests.get(
    "https://contaspoupanca.pt/carro/combustiveis/2025-08-14-preco-dos-combustiveis-na-proxima-semana--18-a-24-de-agosto--f520d954")

# print(response.status_code)

soup = BeautifulSoup(response.content, "html.parser")

# print(soup.prettify())

content_div = soup.find("div", class_="item-6 item-6-15 item-even CT-html")
content_span = content_div.find("span")

# print(content_span)
values = content_span.text.strip("| Semanas anteriores* ")
values = values.replace("(", " ").replace(")", " ").replace("=", "0").replace("}", " ").replace(",", ".")
values = values.split()
values = [float(v) * 0.01 for v in values]

price = 1.5

# print(values)

for p, v in enumerate(values.copy()):
    price += v
    price = round(price, 4)
    values[p] = price

days = []
for n in range(len(values) - 1, -1, -1):
    days.append(n)


# for n in zip(days,values):
#     print(n)

plt.plot(days, values)
plt.title("Gas Prices")
plt.xlabel("Weeks ago")
plt.ylabel("Price diference")
plt.gca().invert_xaxis()  # This reverses the x-axis
plt.show()
