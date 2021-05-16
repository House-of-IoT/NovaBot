import requests
import json

class RequestHandler:
    def __init__(self , parent):
        self.count = 0
        self.data = None
        self.parent = parent

    def issue(self):
        self.parent.say("There was an issue with the request!")
        
    async def gather_peers(self):
        connection =self.parent.parent.socket_handler.connection
        #the response is handled in the socket handler
        await connection.send("devices") 

    def get(self,url,timeout):
        try:
            data = requests.get(url, timeout = timeout)
            data_dict = json.loads(data.content.decode("utf8"))
            self.data = data_dict
            return True
        except:
            return False

    def gather_github_stats(self):
        try:
            if self.get("https://api.github.com/users/ronaldcolyar" , 5) == True:
                self.parent.say("you have " + str(self.data["followers"]) +"followers")
            else:
                self.parent.say("Issue gathering")

        except:
            print("issue")

    def say_geek_quote(self):
        if self.get("https://geek-quote-api.herokuapp.com/v1/quote/1" , 5) == True:
            self.parent.say(self.data[0]["quote"])
        else:
            self.issue()
        
    def say_current_weather(self,place):
        url  = f"http://api.weatherapi.com/v1/current.json?key=c74cbac3960c4c729e052715210205&q={place}&aqi=no"
        if self.get(url,5) == True:
            temp_f = self.data["current"]["temp_f"]
            temp_c = self.data["current"]["temp_c"]
            wind_mph = self.data["current"]["wind_mph"]
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

    

    