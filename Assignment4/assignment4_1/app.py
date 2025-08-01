from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = 'data.json'

@app.route('/api', methods=['GET'])
def get_data():
    if not os.path.exists(DATA_FILE):
        return jsonify({"error": "Data file not found"}), 404

    with open(DATA_FILE, 'r') as file:
        try:
            data = json.load(file)
            return jsonify(data)
        except json.JSONDecodeError:
            return jsonify({"error": "Error reading JSON data"}), 500

if __name__ == '__main__':
    app.run(debug=True)
