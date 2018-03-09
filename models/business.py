class Business:
    def __init__(self, businessname, description, location):
        self.businessname = businessname
        self.description = description
        self.location = location
        
    def create_business(self):
       new_business = {
           "businessname": self.businessname, 
           "description": self.description,
            "location": self.location
        }
       return new_business