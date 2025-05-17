from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

last_data = None

@app.route('https://flask-backend-u1sd.onrender.com/save_data', methods=['POST'])
def save_data():
    global last_data
    data = request.json.get('data')
    if not data:
        return jsonify(error='Brak danych'), 400
    last_data = data
    return jsonify(success=True)

@app.route('https://flask-backend-u1sd.onrender.com/get_data', methods=['GET'])
def get_data():
    return jsonify(last_data=last_data)
