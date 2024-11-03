from requests import request
class News():

    def __init__(self,NEWS_ENDPOINT:str,NEWS_HEADER:dict,PRAM_NEWS:dict) -> list:

        self.NEWS_ENDPOINT = NEWS_ENDPOINT
        self.NEWS_HEADER = NEWS_HEADER
        self.PRAM_NEWS = PRAM_NEWS


    def get_news_api(self):

        response = request(method="GET",url=self.NEWS_ENDPOINT,headers=self.NEWS_HEADER,params=self.PRAM_NEWS)
        return response.json()['articles'][1:4]