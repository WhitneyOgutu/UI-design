from flask import Flask, jsonify, request
from flask_restful import Api, Resource

# Creates an Instance of Flask and wraps it in an Api
app = Flask(__name__)
api = Api(app, prefix="/api/v1")

# A list to store the users
Users = []

class UserCollection(Resource):
    def post(self, first_name, last_name, email_address, password):
        data = request.get_json()
        user = {
            "first_name": data["first_name"],
            "last_name": data["last_name"],
            "email_address": data["email_address"],
            "password": data["password"]
        }

        Users.append(user)
        return {"message": "User created successfully"}

    def get(self):
        return user

class User(Resource):
    def get(self, id):
        pass
    
    def put(self, id):
        pass

    def delete(self,id):
        pass

#adds resource to the api
api.add_resource( UserCollection, 'users')

if __name__ == '__main__':
    app.run(debug=True)