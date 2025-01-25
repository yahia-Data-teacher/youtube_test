import csv
import json

from flask import Flask, request, jsonify

app = Flask(__name__)

# Paths to the input CSV and output JSON files
csv_file_path1 = 'POC_Workiwa_Conso_Sites_Bpifrance_20250124.csv'
csv_file_path2 = 'POC_Workiwa_Conso_Bpifrance_20250124.csv'
json_file_path1 = 'output1.json'
json_file_path2 = 'output2.json'

# List to hold the data
data1 = []
data2 = []

# Read the CSV file
with open(csv_file_path1, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data1.append(row)

# Read the CSV file
with open(csv_file_path2, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data2.append(row)
        

# Endpoint to GET data
@app.route('/api/data1', methods=['GET'])
def get_data1():
    return jsonify(data1), 200

# Endpoint to GET data
@app.route('/api/data2', methods=['GET'])
def get_data2():
    return jsonify(data2), 200

# Endpoint to POST data
@app.route('/api/data1', methods=['POST'])
def post_data1():
    incoming_data1 = request.json
    print("Received data in Gitpod:", incoming_data1)
    return jsonify({"message": "Data received in Gitpod!", "received_data": incoming_data1}), 200

# Endpoint to POST data
@app.route('/api/data2', methods=['POST'])
def post_data2():
    incoming_data2 = request.json
    print("Received data in Gitpod:", incoming_data2)
    return jsonify({"message": "Data received in Gitpod!", "received_data": incoming_data2}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5030)