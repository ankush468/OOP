import os
from stock_oop import Stock
from pprint import pprint as print
from datetime import datetime, timedelta, date

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.getenv('STOCK_API_KEY')
print(STOCK_API_KEY)

PRAM = {
       'function' : "TIME_SERIES_DAILY",
       'symbol' : STOCK_NAME,    
       'apikey' : STOCK_API_KEY
       }


yesterday = (date.today() - timedelta(days=2)).isoformat()
day_before_yesterday = (date.today() - timedelta(days=4)).isoformat()

print(yesterday)
print(day_before_yesterday)


get_stock_price = Stock(STOCK_ENDPOINT,PRAM,yesterday,day_before_yesterday)
Stock_price = get_stock_price.Stock_price()
print(Stock_price)


