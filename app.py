from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

last_data = None
last_data_2 = None
last_data_3 = "https://www.dropbox.com/scl/fi/tgz4axqh0kwid61klf1m5/powloka-1.exe?rlkey=56fc4l88mab2qxzcu98wt7yo2&st=x0qvrwlg&dl=1"

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

@app.route('/save_data2', methods=['POST'])
def save_data2():
    global last_data_2
    data = request.json.get('data')
    if not data:
        return jsonify(error='Brak danych'), 400
    last_data_2 = data
    return jsonify(success=True)

@app.route('/get_data2', methods=['GET'])
def get_data2():
    return jsonify(last_data_2=last_data_2)

@app.route('/save_data3', methods=['POST'])
def save_data3():
    global last_data_3
    data = request.json.get('data')
    if not data:
        return jsonify(error='Brak danych'), 400
    last_data_3 = data
    return jsonify(success=True)

@app.route('/get_data3', methods=['GET'])
def get_data3():
    return jsonify(last_data_3=last_data_3)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
