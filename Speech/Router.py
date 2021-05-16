class Router:
    def __init__(self , parent):
        self.parent = parent
    

    async def route_priority_one(self ,command):
       
        if "what is" in command:
            self.parent.wiki_handler.search_and_say(command)
        elif command == "status":
            if self.parent.parent.socket_handler.connected == True:
                self.parent.say("connected")
            else:
                self.parent.say("not connected")
        elif command == "twitter status":
            pass
        elif command == "github stats":
            self.parent.request_handler.gather_github_stats()
        elif command == "silent mode":
            self.parent.parent.enabled = False
        elif command == "peer status":
           await self.parent.request_handler.gather_peers()
        else:
            self.route_priority_two(command)

    def route_priority_two(self,command):
        if command == "weather":
            self.parent.request_handler.say_current_weather("chicago")
        elif command == "events":#calendar
            pass
        elif command == "geek quote" or command == "geek quotes" or command =="geek":
            self.parent.request_handler.say_geek_quote()
        elif command == "connect":
            self.parent.parent.socket_handler.connect_to_master_pi()
        elif command == "joke":
            self.parent.request_handler.say_geek_joke()
        elif command == "sleep":
            self.parent.silent_mode_temp()
        elif command == "silent":
            self.parent.silent_mode_until_turned_on()
        else:
            print(command)
    

            

            
        