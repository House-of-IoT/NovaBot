class Router:
    def __init__(self , parent):
        self.parent = parent
    

    def route_priority_one(self ,command):
       
        if "what is" in command:
            self.parent.wiki_handler.search_and_say(command)

        elif command == "status":
            pass
        elif command == "twitter status":
            pass
        elif command == "github status":
            pass
        elif command == "disable camera":
            pass
        elif command == "silent mode":
            pass
        elif command == "logging mode":
            pass
        elif command == "peer status":
            pass
        else:
            self.route_priority_two(command)

    def route_priority_two(self,command):
        if command == "weather":
            pass
        elif command == "events":#calendar
            pass
        elif command == "server status":
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
    

            

            
        