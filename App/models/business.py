from flask import Flask

app = Flask(__name__)

class Business:

    Businesses = []

    def __init__(self, businessname, description, location):
        self.businessname = businessname
        self.description = description
        self.location = location

    def create_business(self):
        business = {
            "businessname": "businessname",
            "description": "description",
            "location": "location"
        }

        Business.Businesses.append(business)
        return {"message": "Business created successfully"}

if __name__ == '__main__':
    app.run(debug=True)    