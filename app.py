from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder='.')
CORS(app)

simulation_data = {}

@app.route('/update_data', methods=['POST'])
def update_data():
    global simulation_data
    simulation_data = request.json
    return jsonify({"status": "success"})

@app.route('/get_data')
def get_data():
    return jsonify(simulation_data)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)