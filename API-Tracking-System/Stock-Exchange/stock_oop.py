from requests import request
class Stock():

    def __init__(self , STOCK_ENDPOINT : str,PRAM:dict, yesterday,day_before_yesterday) -> tuple:

        self.STOCK_ENDPOINT = STOCK_ENDPOINT
        self.PRAM = PRAM
        self.yesterday = yesterday
        self.day_before_yesterday = day_before_yesterday

    def Stock_price(self):
        
        response = request(method="GET",url=self.STOCK_ENDPOINT,params=self.PRAM)
        yesterday_closing_price = response.json()['Time Series (Daily)'][self.yesterday]['4. close']
        day_before_closing_price = response.json()['Time Series (Daily)'][self.day_before_yesterday]['4. close']
        return yesterday_closing_price , day_before_closing_price
    
    def percentage_difference(self , Stock_percentage):

        diff = (float(Stock_percentage[1])) - (float(Stock_percentage[0]))
        avg  = (float(Stock_percentage[1])) + (float(Stock_percentage[0])) /2
        return (diff / avg) * 100
    
