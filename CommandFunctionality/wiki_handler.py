import wikipedia



class WikiHandler:
    def __init__(self):
        self.count = 0
        self.current_result = None

    def gather_page(self,page_name):
        self.count +=1
        try:
            self.current_result = wikipedia.summary(page_name)
            return True
        except:
            return False

    def get_current_result(self):
        return self.current_result
        
    def get_attempts(self):
        self.count
            
