from flask import Flask, jsonify, request, make_response, json

from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity


try:
    from WeConnect.models.user import User
    from WeConnect.models.business import Business
    from WeConnect.models.reviews import Review    
except ModuleNotFoundError:
    from models.user import User
    from models.business import Business
    from models.reviews import Review
    

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'wonderwoman'
jwt = JWTManager(app)


Users = []
Businesses = []
Reviews = []

@app.route('/api/auth/register', methods=['GET', 'POST'])  
def register_user():
    if request.method == 'POST':
        data = request.get_json()
        firstname = data.get("firstname")
        username = data.get("username")
        password = data.get("password")
        
        if firstname.strip() == "": 
            return jsonify({"message": "Please input a firstname value"})
        elif username.strip() == "":
            return jsonify({"message": "Please input a username value"})
        elif password.strip() == "":
            return jsonify({"message": "Please input password a value"})
        else:
            user = {new_user.username: new_user.password for new_user in Users}
            if username in user.keys():
                return jsonify({"message": "User already exists"})

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
            access_token = create_access_token(identity=username)
            response = {
                "message": "You are successfully logged in",
                "access_token": access_token
            }
            return (jsonify(response)), 201
        else:
            return jsonify ({'message': 'User does not exist. Proceed to register'}), 500
            
@app.route('/api/register/business', methods=['GET', 'POST'])
@jwt_required
def register_business():
    if request.method == 'POST':
        current_user = get_jwt_identity()
        data = request.get_json()
        businessname = data.get("businessname")
        description = data.get("description")
        location = data.get("location")

        if businessname.strip() == "": 
            return jsonify({"message": "Please input a businessname value"}), 406
        elif description.strip() == "":
            return jsonify({"message": "Please input a description value"})
        elif location.strip() == "":
            return jsonify({"message": "Please input location a value"})
        else:
            business = {new_business.businessname: new_business.description for new_business in Businesses}
            if businessname in business.keys():
                return jsonify({"message": "Business already exists"})

        new_business = Business(businessname, description, location)
        Businesses.append(new_business)
        response = {"message": "Business created successfully",
                    "Business created by": current_user
            }
        return (jsonify(response)), 201

    else:
        if request.method == 'GET':
            return jsonify(Businesses), 200

@app.route('/api/businesses/review', methods=['GET', 'POST'])
@jwt_required
def register_review():
    if request.method == 'POST':
        current_user = get_jwt_identity()
        data = request.get_json()
        title = data.get("title")
        description = data.get("description")

        if title.strip() == "": 
            return jsonify({"message": "Please input a title value"}), 406
        else:
            if description.strip() == "":
                return jsonify({"message": "Please input a description value"})
    
        new_review = Review(title, description)
        Reviews.append(new_review)
        response = {"message": "Review created successfully",
                    "Business created by": current_user
            }
        return (jsonify(response)), 201

    return app


