class Review:
    def __init__(self, title, description):
        self.title = title
        self.description = description
    
    def create_review(self):
       new_review = {
           "title": self.title, 
           "description": self.description
        }
       return new_review