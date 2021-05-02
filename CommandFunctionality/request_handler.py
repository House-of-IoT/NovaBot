import requests
import json

class RequestHandler:
    def __init__(self , parent):
        self.count = 0
        self.data = None
        self.parent = parent

    def issue():
        self.parent.say("There was an issue with the request!")
        
    def get(self,url,timeout):
        try:
            data = requests.get("https://geek-quote-api.herokuapp.com/v1/quote/1" , timeout = timeout)
            data_dict = json.loads(data.content.decode("utf8"))
            self.data = data_dict
            return True
        except:
            return False

    def say_geek_quote(self):
        if self.get("https://geek-quote-api.herokuapp.com/v1/quote/1" , 5) == True:
            self.parent.say(self.data[0]["quote"])
        else:
            self.issue()
        
    def say_weather_current(self,place):
        url  = f"http://api.weatherapi.com/v1/current.json?key=c74cbac3960c4c729e052715210205&q={place}&aqi=no"
        if self.get(url) == True:
            temp_f = self.data["current"]["temp_f"]
            temp_c = self.data["current"]["temp_c"]
            wind_mph = self.data["wind_mph"]
            self.parent.say(f"Here is the data for {place}")
            self.parent.say(f"{temp_f}  degrees fahrenheit")
            self.parent.say(f"{temp_c}  degrees celcius")
            self.parent.say(f" wind speed is {wind_mph} miles per hour")
        else:
           self.issue()

    def say_geek_joke(self):
        if self.get("https://geek-jokes.sameerkumar.website/api",5)  == True:
            self.parent.say(self.data[0]["quote"])
        else:
            self.issue()

    

    