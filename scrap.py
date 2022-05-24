import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/'

r = requests.get(url)

soup = BeautifulSoup(r.text)

article = soup.find_all('article', class_ = 'product_pod')

for book in article:
    title = book.find_all('a')[1]['title']
    price = book.find('p', class_ = 'price_color').text
    print(price)
