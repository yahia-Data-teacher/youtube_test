import csv
import json
# import awsgi

from flask import Flask, request, jsonify

app = Flask(__name__)

# Paths to the input CSV and output JSON files

csv_file_path = 'POC_Workiwa_Conso_Bpifrance_20250124.csv'
json_file_path = 'output.json'


# List to hold the data
data = []


# Read the CSV file
with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data.append(row)
        

# Endpoint to GET data
@app.route('/api/data', methods=['GET'])
def get_data1():
    return jsonify(data), 200


# Endpoint to POST data
@app.route('/api/data', methods=['POST'])
def post_data1():
    incoming_data1 = request.json
    print("Received data :", incoming_data1)
    return jsonify({"message": "Data received in Gitpod!", "received_data": incoming_data1}), 200

# def lambda_handler(event, context):
#     return awsgi.response(app, event, context, base64_content_types={"image/png"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5030)