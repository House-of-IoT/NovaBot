class Router:
    def __init__(self , parent):
        self.parent = parent
    

    def route_priority_one(self ,command):
       
        if command == "wikipedia":
            pass
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
        elif command = "peer status":
            pass
        else:
            self.route_priority_two(command)

    def route_priority_two(self,command):
        if command == "weather":
            pass
        elif command == "events":#calendar
            pass
        elif command == "random humor":
            pass
        elif command == "server status":
            pass
        

            

            
        