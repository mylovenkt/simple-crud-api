from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()

#(POST)
@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()

    # Kiểm tra dữ liệu đầu vào
    if not data.get('email') or not data.get('username') or not data.get('birthday'):
        return jsonify({"message": "Email, username, and birthday are required."}), 400

    # Kiểm tra xem email đã tồn tại chưa
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"message": "Email already exists."}), 400

    new_user = User(email=data['email'], username=data['username'], birthday=data['birthday'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully."}), 201

#(GET)
@app.route('/get_user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)

    if user:
        return jsonify({"id": user.id, "email": user.email, "username": user.username, "birthday": user.birthday})
    else:
        return jsonify({"message": "User not found."}), 404

#(PUT)
@app.route('/update_user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()

    user = User.query.get(user_id)

    if not user:
        return jsonify({"message": "User not found."}), 404

    if data.get('email'):
        if User.query.filter_by(email=data['email']).first():
            return jsonify({"message": "Email already exists."}), 400
        user.email = data['email']

    if data.get('username'):
        user.username = data['username']

    if data.get('birthday'):
        user.birthday = data['birthday']

    db.session.commit()
    return jsonify({"message": "User updated successfully."})

#(DELETE)
@app.route('/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({"message": "User not found."}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted successfully."})

if __name__ == '__main__':
    app.run(debug=True)
