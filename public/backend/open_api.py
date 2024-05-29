from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Process the data as needed, for example:
    name = data.get('name')
    university_name = data.get('university_name')
    description = data.get('description')
    modules_sem1 = data.get('modules_sem1', [])
    modules_sem2 = data.get('modules_sem2', [])
    modules_sem3 = data.get('modules_sem3', [])
    modules_sem4 = data.get('modules_sem4', [])
    
    #  the prediction logic, for now i will just echo the received data.
    result = {
        "name": name,
        "university_name": university_name,
        "description": description,
        "modules_sem1": modules_sem1,
        "modules_sem2": modules_sem2,
        "modules_sem3": modules_sem3,
        "modules_sem4": modules_sem4
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
