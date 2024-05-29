from flask import Flask, request, jsonify
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open('svm_model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    modules = np.array([data['module1'], data['module2'], data['module3'], ...])
    prediction = model.predict([modules])
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
