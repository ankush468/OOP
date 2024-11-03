import os
from stock_oop import Stock
from pprint import pprint as print
from datetime import datetime, timedelta, date

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.getenv('STOCK_API_KEY')
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

############################## PRAM for STOCK #######################################
PRAM = {
       'function' : "TIME_SERIES_DAILY",
       'symbol' : STOCK_NAME,    
       'apikey' : STOCK_API_KEY
       }


yesterday = (date.today() - timedelta(days=2)).isoformat()
day_before_yesterday = (date.today() - timedelta(days=4)).isoformat()

# Get stock price from API return string of tuple
get_stock_price = Stock(STOCK_ENDPOINT,PRAM,yesterday,day_before_yesterday)
Stock_price = get_stock_price.Stock_price()

# check the percentage diff between 2 days return float
diff_percentage = get_stock_price.percentage_difference(Stock_price)
print(diff_percentage)

############################## PRAM for NEWS #######################################

NEWS_HEADER = {
       'X-Api-Key': NEWS_API_KEY
}

if diff_percentage > 2:
    print('Get News')

