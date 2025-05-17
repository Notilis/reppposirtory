from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

last_data = None

@app.route('/save_data', methods=['POST'])
def save_data():
    global last_data
    data = request.json.get('data')
    if not data:
        return jsonify(error='Brak danych'), 400
    last_data = data
    return jsonify(success=True)

@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify(last_data=last_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
