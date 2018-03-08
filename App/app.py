from flask import Flask, jsonify, request, make_response

try: 
    from App.config import DevelopmentConfig, TestingConfig, ProductionConfig
    from App.models.user import User
    from App.models.business import Business
except ModuleNotFoundError:
    from config import DevelopmentConfig, TestingConfig, ProductionConfig
    from models.user import User
    from models.business import Business

Users = []
Businesses = []

def create_app(config_name):
    app = Flask(__name__)
    if config_name == "Development":
        app.config.from_object(DevelopmentConfig)
    elif config_name == "Testing":
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(ProductionConfig)

    # attach routes and custom error pages here
    @app.errorhandler(404)
    def resource_not_found(e):
       response = jsonify({"error": "Resource not found"})
       return response 

    @app.route('/api/auth/register', methods=['GET', 'POST'])
    def register_user():
        if request.method == 'POST':
            data = request.get_json()
            firstname = data.get("firstname")
            username = data.get("username")
            password = data.get("password")
            new_user = User(firstname, username, password)
            Users.append(new_user)
            response = {"message": "User created successfully"}
            return (jsonify(response)), 201
    
    @app.route('/api/auth/login', methods=['POST'])
    def login_user():
        if request.method == 'POST':
            data = request.get_json()
            username = data.get("username")
            password = data.get("password")
            details = {new_user.username: new_user.password for new_user in Users}
            if username in details.keys():
                try:
                    if password == details[username]:
                        token = username
                        response = {
                            'message': 'You are successfully logged in',
                            'token': token
                        }
                        return jsonify(response), 200
                    # else: 
                    #     response = {'message': 'Input correct email or password'}
                    #     return jsonify(response), 401

                except Exception:
                    response = {'message': 'User does not exist. Proceed to register'}
                    return jsonify(response), 500

    @app.route('/api/auth/logout', methods=['POST'])
    def logout_user():
        auth_header = request.headers.get('Authorization')
        token = auth_header.split(" ")[1]
        if token:
            details = {new_user.username: new_user.password for new_user in Users}
            if token in details.keys():
                try:
                    response = {
                        'message': 'You are successfully logged out',
                        'token': ''
                    }
                    return jsonify(response), 200
                    # else: 
                    #     response = {'message': 'Input correct email or password'}
                    #     return jsonify(response), 401

                except Exception:
                    response = {'message': 'User does not exist. Proceed to register'}
                    return jsonify(response), 500


    @app.route('/api/register/business', methods=['GET', 'POST'])
    def register_business():
        if request.method == 'POST':
            data = request.get_json()
            businessname = data.get("businessname")
            description = data.get("description")
            location = data.get("location")
            new_business = Business(businessname, description, location)
            Businesses.append(new_business)
            response = {"message": "Business created successfully"}
            return (jsonify(response)), 201
            
    return app

