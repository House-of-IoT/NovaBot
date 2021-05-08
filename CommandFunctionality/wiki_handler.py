import wikipedia



class WikiHandler:
    def __init__(self,parent):
        self.count = 0
        self.current_result = None
        self.parent = parent

    def gather_page(self,page_name):
        self.count +=1
        try:
            self.current_result = wikipedia.summary(page_name,sentences = 5)
            return True
        except:
            return False

    def get_current_result(self):
        return self.current_result
        
    def get_attempts(self):
        self.count

    def search_and_say(self, input_data):
        page_name = input_data[6::]
        print(page_name)
        result = self.gather_page(page_name)
        if result == True:
            self.parent.say(self.current_result)
        else:
            self.parent.say(f"Don't know what {page_name} is")
            
