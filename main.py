import requests
from bs4 import BeautifulSoup
import pandas as pd

link = "https://www.ebay.com/e/fashion/bo7-omega-021720"

my_content = requests.get(link)

soup = BeautifulSoup(my_content.text, 'html.parser')

ul = soup.find(
    'ul', attrs={'class': 'b-list__items_nofooter srp-results srp-grid'})


titles = []
prices = []
shippings = []
urls = []
total_cost = []

for items in ul.findAll('li', attrs={'class': 's-item'}):
    titles.append(items.find('h3', attrs={'class': 's-item__title'}).text)
    prices.append(items.find(
        'span', attrs={'class': 's-item__price'}).text[1::])
    shippings.append(items.find(
        'span', attrs={'class': 's-item__shipping'}).text[1:-9])
    urls.append(items.find('a', href=True)['href'])
    total_cost.append(float((items.find(
        'span', attrs={'class': 's-item__price'}).text[1::]).replace(',', ''))+float((items.find(
            'span', attrs={'class': 's-item__shipping'}).text[1:-9]).replace(',', '')))
# print(titles)
# print(prices)

my_list = pd.DataFrame(
    {'Product Name': titles, 'Price': prices, 'Shipping': shippings, 'Total_Cost': total_cost, 'URL': urls})
my_list.to_csv('prices.csv')
