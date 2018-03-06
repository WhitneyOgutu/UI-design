from flask import Flask, jsonify, request
from flask_restful import Api, Resource

# Creates an Instance of Flask and wraps it in an Api
app = Flask(__name__)
api = Api(app, prefix="/api/v1")

# A list to store the business
Businesses = []

class BusinessCollection(Resource):
    def post(self):
        data = request.get_json()
        business = {
            "business_name": data ["business_name"],
            "description": data ["description"],
            "location": data ["location"],
            "product_offered": data ["product_offered"]
        }
        Businesses.append(business)
        return {"message": "Business created successfully"}

    def get(self):
        return business

class Business(Resource):
    def get(self, id):
        pass
    
    def put(self, id):
        pass

    def delete(self,id):
        pass

api.add_resource(BusinessCollection, '/businesses')
api.add_resource(Business, '/businesses/<int:id>')