from requests import request

class Habit_tracking():

    def __init__(self , user_creation_url:str, user_creation_payload:dict) -> None:
        
        self.user_creation_url = user_creation_url
        self.user_creation_payload = user_creation_payload

    def Create_user(self):

        response = request(method="POST",url=self.user_creation_url,json=self.user_creation_payload)
        return response.json()
    
    def Create_graph(self, graph_creation_url, header_for_all,graph_creation_payload):

        response = request(method="POST",url=graph_creation_url, json=graph_creation_payload, headers=header_for_all)
        return response.json()
    
    def Get_graph(self , get_graph_endpoint, header_for_all):

        response = request(method="GET", url=get_graph_endpoint,headers=header_for_all)
        return response.json()
    
    def Create_pixel(self, post_pixel_endpoint, post_pixel_data , header_for_all):

        response = request(method="POST",url=post_pixel_endpoint, headers=header_for_all , json=post_pixel_data)
        return response.json()
    
    def update_pixel(self, put_graph_endpoint , put_pixel_chnage , header_for_all):

        response = request(method="PUT", url=put_graph_endpoint, json=put_pixel_chnage , headers=header_for_all)
        return response.json()
    
    def Delete_pixel(self, put_graph_endpoint , header_for_all):

        response = request(method="DELETE", url=put_graph_endpoint, headers=header_for_all)
        return response.json()