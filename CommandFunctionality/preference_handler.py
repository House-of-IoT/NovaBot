import json 

class PreferenceHandler:
    def __init__(self , parent):
        self.old = None # for reverting
        self.parent = parent
        
    def gather_old(self):
        try:
            with open("preference.json" , "r") as file:
                self.old  = file.readlines()
        except:
            pass

    def change_preference(self , change_type ,change_value):
        self.gather_old()
        try:
            old_data = json.loads(self.old)
            old_data[change_type]  = change_type
            new_data = json.dumps(old_data)
            with open("preference.json" , "w") as file:
                file.write(new_data)
        except:
            self.parent.say("Issue changing")
