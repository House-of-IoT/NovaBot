import requests
import json

class RequestHandler:
    def __init__(self , parent):
        self.count = 0
        self.data = None

    def gather_geek_quote(self):
        try:
            data = requests.get("https://geek-quote-api.herokuapp.com/v1/quote/1" , timeout = 2)
            data_dict = json.loads(data.content)
            self.data = data_dict["quote"]
            return True
        except:
            return False
    
       
 
