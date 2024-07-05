from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)

# 저장된 모델과 스케일러 로드
with open('iris_model.pkl', 'rb') as file:
    model, scaler = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = np.array(data['features']).reshape(1, -1)
    
    print(f"Received features: {features}")
    
    scaled_features = scaler.transform(features)
    print(f"Scaled features: {scaled_features}")
    
    prediction = model.predict(scaled_features)
    probabilities = model.predict_proba(scaled_features)[0]
    
    print(f"Prediction: {prediction[0]}")
    print(f"Probabilities: {probabilities}")
    
    return jsonify({
        'prediction': int(prediction[0]),
        'probabilities': probabilities.tolist()
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)