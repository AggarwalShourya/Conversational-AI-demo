from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/tshirts", methods=["GET"])
def get_tshirts():
    data = [
        {"order_id": 1, "name": "White Tee", "price": 25, "rating": 4.3},
        {"order_id": 2, "name": "Black Oversized", "price": 45, "rating": 4.8},
        {"order_id": 3, "name": "Red V-Neck", "price": 20, "rating": 4.5},
        {"order_id": 4, "name": "Blue Shorts", "price": 10, "rating": 4.1},
    ]
    return jsonify(data)