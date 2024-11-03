import os
from stock_oop import Stock
from news_oop import News
from pprint import pprint as print
from datetime import datetime, timedelta, date

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.getenv('STOCK_API_KEY')
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

############################## PRAM for STOCK #######################################
# PRAM_STOCK = {
#        'function' : "TIME_SERIES_DAILY",
#        'symbol' : STOCK_NAME,    
#        'apikey' : STOCK_API_KEY
#        }


yesterday = (date.today() - timedelta(days=2)).isoformat()
day_before_yesterday = (date.today() - timedelta(days=4)).isoformat()

# # Get stock price from API return string of tuple
# get_stock_price = Stock(STOCK_ENDPOINT,PRAM_STOCK,yesterday,day_before_yesterday)
# Stock_price = get_stock_price.Stock_price()

# # check the percentage diff between 2 days return float
# diff_percentage = get_stock_price.percentage_difference(Stock_price)
# print(diff_percentage)
diff_percentage =5
############################## PRAM for NEWS #######################################

NEWS_HEADER = {
       'X-Api-Key': NEWS_API_KEY
}

PRAM_NEWS = {
    'q':COMPANY_NAME,
    'from':day_before_yesterday,
    'to' : yesterday,
    'sortBy': 'popularity'
}

if diff_percentage > 2:
    get_news = News(NEWS_ENDPOINT,NEWS_HEADER,PRAM_NEWS)
    news = get_news.get_news_api()
    print(news)

