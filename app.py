from flask import Flask, render_template, request
import pickle
import numpy as np
import os

# Get the directory path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load pre-trained model and scaler with proper paths
model_path = os.path.join(BASE_DIR, 'model', 'model.pkl')
scaler_path = os.path.join(BASE_DIR, 'model', 'scaler.pkl')
label_encoder_path = os.path.join(BASE_DIR, 'model', 'label_encoder.pkl')

model = pickle.load(open(model_path, 'rb'))
scaler = pickle.load(open(scaler_path, 'rb'))

app = Flask(__name__)

# Function to categorize AQI
def get_aqi_category(aqi):
    if 0 <= aqi <= 50:
        return 'Good'
    elif 51 <= aqi <= 100:
        return 'Moderate'
    elif 101 <= aqi <= 150:
        return 'Unhealthy for Sensitive Groups'
    elif 151 <= aqi <= 200:
        return 'Unhealthy'
    elif 201 <= aqi <= 300:
        return 'Very Unhealthy'
    else:
        return 'Hazardous'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Get user inputs
            pm25 = float(request.form['pm25'])
            pm10 = float(request.form['pm10'])
            no2 = float(request.form['no2'])
            so2 = float(request.form['so2'])
            co = float(request.form['co'])
            o3 = float(request.form['o3'])
            temperature = float(request.form['temperature']) if 'temperature' in request.form else float(request.form['temp'])
            
            # Prepare input for model
            user_input = np.array([[pm25, pm10, no2, so2, co, o3, temperature]])
            scaled_input = scaler.transform(user_input)
            
            # Predict AQI
            predicted_aqi = model.predict(scaled_input)[0]
            
            # Get AQI category
            category = get_aqi_category(predicted_aqi)
            
            result = f"AQI: {predicted_aqi:.2f} - Category: {category}"
            return render_template('index.html', result=result)
        except Exception as e:
            return render_template('index.html', result=f"Error: {str(e)}")
    
    return render_template('index.html', result=None)

@app.route('/predict', methods=['POST'])
def predict():
    return index()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

