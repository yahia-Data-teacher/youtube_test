from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data
sample_data = {
    "status": "success",
    "data": [
        {"employee_salary": "320800", "employee_age": "52", "profile_image": ""},
    {"employee_salary": "45000", "employee_age": "34", "profile_image": ""},
    {"employee_salary": "67000", "employee_age": "29", "profile_image": ""},
    {"employee_salary": "89000", "employee_age": "41", "profile_image": ""},
    {"employee_salary": "120000", "employee_age": "36", "profile_image": ""},
    {"employee_salary": "55000", "employee_age": "27", "profile_image": ""},
    {"employee_salary": "78000", "employee_age": "45", "profile_image": ""},
    {"employee_salary": "95000", "employee_age": "38", "profile_image": ""},
    {"employee_salary": "110000", "employee_age": "50", "profile_image": ""},
    {"employee_salary": "320800", "employee_age": "52", "profile_image": ""},
    {"employee_salary": "43000", "employee_age": "31", "profile_image": ""},
    {"employee_salary": "62000", "employee_age": "28", "profile_image": ""},
    {"employee_salary": "85000", "employee_age": "40", "profile_image": ""},
    {"employee_salary": "130000", "employee_age": "37", "profile_image": ""},
    {"employee_salary": "54000", "employee_age": "26", "profile_image": ""},
    {"employee_salary": "77000", "employee_age": "44", "profile_image": ""},
    {"employee_salary": "96000", "employee_age": "39", "profile_image": ""},
    {"employee_salary": "115000", "employee_age": "51", "profile_image": ""},
    {"employee_salary": "320800", "employee_age": "52", "profile_image": ""},
    {"employee_salary": "44000", "employee_age": "33", "profile_image": ""},
    {"employee_salary": "66000", "employee_age": "30", "profile_image": ""},
    {"employee_salary": "88000", "employee_age": "42", "profile_image": ""},
    {"employee_salary": "125000", "employee_age": "35", "profile_image": ""},
    {"employee_salary": "56000", "employee_age": "25", "profile_image": ""},
    {"employee_salary": "79000", "employee_age": "46", "profile_image": ""},
    {"employee_salary": "94000", "employee_age": "37", "profile_image": ""},
    {"employee_salary": "105000", "employee_age": "49", "profile_image": ""},
    {"employee_salary": "320800", "employee_age": "52", "profile_image": ""},
    {"employee_salary": "41000", "employee_age": "32", "profile_image": ""},
    {"employee_salary": "63000", "employee_age": "29", "profile_image": ""},
    {"employee_salary": "87000", "employee_age": "43", "profile_image": ""},
    {"employee_salary": "135000", "employee_age": "36", "profile_image": ""},
    {"employee_salary": "58000", "employee_age": "24", "profile_image": ""},
    {"employee_salary": "81000", "employee_age": "47", "profile_image": ""},
    {"employee_salary": "92000", "employee_age": "38", "profile_image": ""},
    {"employee_salary": "100000", "employee_age": "48", "profile_image": ""},
    {"employee_salary": "320800", "employee_age": "52", "profile_image": ""},
    {"employee_salary": "42000", "employee_age": "31", "profile_image": ""},
    {"employee_salary": "64000", "employee_age": "28", "profile_image": ""},
    {"employee_salary": "86000", "employee_age": "41", "profile_image": ""},
    {"employee_salary": "140000", "employee_age": "37", "profile_image": ""},
    {"employee_salary": "59000", "employee_age": "23", "profile_image": ""},
    {"employee_salary": "82000", "employee_age": "45", "profile_image": ""},
    {"employee_salary": "91000", "employee_age": "39", "profile_image": ""},
    {"employee_salary": "95000", "employee_age": "47", "profile_image": ""},
    {"employee_salary": "320800", "employee_age": "52", "profile_image": ""},
    {"employee_salary": "40000", "employee_age": "30", "profile_image": ""},
    {"employee_salary": "65000", "employee_age": "27", "profile_image": ""},
    {"employee_salary": "84000", "employee_age": "40", "profile_image": ""},
    {"employee_salary": "145000", "employee_age": "38", "profile_image": ""},
    {"employee_salary": "60000", "employee_age": "22", "profile_image": ""},
    {"employee_salary": "83000", "employee_age": "44", "profile_image": ""},
    {"employee_salary": "90000", "employee_age": "37", "profile_image": ""},
    {"employee_salary": "98000", "employee_age": "46", "profile_image": ""},
    {"employee_salary": "320800", "employee_age": "52", "profile_image": ""},
    {"employee_salary": "39000", "employee_age": "29", "profile_image": ""},
    {"employee_salary": "61000", "employee_age": "26", "profile_image": ""},
    {"employee_salary": "83000", "employee_age": "39", "profile_image": ""},
    {"employee_salary": "150000", "employee_age": "36", "profile_image": ""},
    {"employee_salary": "62000", "employee_age": "21", "profile_image": ""},
    {"employee_salary": "84000", "employee_age": "43", "profile_image": ""},
    {"employee_salary": "89000", "employee_age": "38", "profile_image": ""},
    {"employee_salary": "99000", "employee_age": "45", "profile_image": ""},
    {"employee_salary": "320800", "employee_age": "52", "profile_image": ""},
    {"employee_salary": "38000", "employee_age": "28", "profile_image": ""},
    {"employee_salary": "60000", "employee_age": "25", "profile_image": ""},
    {"employee_salary": "82000", "employee_age": "38", "profile_image": ""},
    {"employee_salary": "155000", "employee_age": "35", "profile_image": ""},
    {"employee_salary": "63000", "employee_age": "20", "profile_image": ""},
    {"employee_salary": "85000", "employee_age": "42", "profile_image": ""},
    {"employee_salary": "88000", "employee_age": "37", "profile_image": ""},
    {"employee_salary": "100000", "employee_age": "44", "profile_image": ""},
    {"employee_salary": "320800", "employee_age": "52", "profile_image": ""},
    {"employee_salary": "37000", "employee_age": "27", "profile_image": ""},
    {"employee_salary": "59000", "employee_age": "24", "profile_image": ""},
    {"employee_salary": "81000", "employee_age": "37", "profile_image": ""},
    {"employee_salary": "160000", "employee_age": "34", "profile_image": ""},
    {"employee_salary": "64000", "employee_age": "19", "profile_image": ""},
    {"employee_salary": "86000", "employee_age": "41", "profile_image": ""},
    {"employee_salary": "87000", "employee_age": "36", "profile_image": ""},
    {"employee_salary": "101000", "employee_age": "43", "profile_image": ""},
    {"employee_salary": "320800", "employee_age": "52", "profile_image": ""},
    {"employee_salary": "36000", "employee_age": "26", "profile_image": ""},
    {"employee_salary": "58000", "employee_age": "23", "profile_image": ""},
    {"employee_salary": "80000", "employee_age": "36", "profile_image": ""},
    {"employee_salary": "165000", "employee_age": "33", "profile_image": ""},
    {"employee_salary": "65000", "employee_age": "18", "profile_image": ""},
    {"employee_salary": "87000", "employee_age": "40", "profile_image": ""},
    {"employee_salary": "86000", "employee_age": "35", "profile_image": ""},
    {"employee_salary": "102000", "employee_age": "42", "profile_image": ""},
    {"employee_salary": "320800", "employee_age": "52", "profile_image": ""},
    {"employee_salary": "35000", "employee_age": "25", "profile_image": ""},
    {"employee_salary": "57000", "employee_age": "22", "profile_image": ""},
    {"employee_salary": "79000", "employee_age": "35", "profile_image": ""},
    {"employee_salary": "170000", "employee_age": "32", "profile_image": ""},
    {"employee_salary": "66000", "employee_age": "17", "profile_image": ""},
    {"employee_salary": "88000", "employee_age": "39", "profile_image": ""},
    {"employee_salary": "85000", "employee_age": "34", "profile_image": ""},
    {"employee_salary": "103000", "employee_age": "41", "profile_image": ""}
    ]
}

# Endpoint to GET data
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(sample_data), 200

# Endpoint to POST data
@app.route('/api/data', methods=['POST'])
def post_data():
    incoming_data = request.json
    print("Received data in Gitpod:", incoming_data)
    return jsonify({"message": "Data received in Gitpod!", "received_data": incoming_data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5033)