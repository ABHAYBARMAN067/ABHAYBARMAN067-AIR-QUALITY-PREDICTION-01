from flask import Flask, render_template, request
import pickle
import numpy as np

# Load pre-trained model and scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

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
        # Get user inputs
        pm25 = float(request.form['pm25'])
        pm10 = float(request.form['pm10'])
        no2 = float(request.form['no2'])
        so2 = float(request.form['so2'])
        co = float(request.form['co'])
        o3 = float(request.form['o3'])
        temperature = float(request.form['temperature'])
        
        # Prepare input for model
        user_input = np.array([[pm25, pm10, no2, so2, co, o3, temperature]])
        scaled_input = scaler.transform(user_input)
        
        # Predict AQI
        predicted_aqi = model.predict(scaled_input)[0]
        
        # Get AQI category
        category = get_aqi_category(predicted_aqi)
        
        return render_template('index.html', aqi=predicted_aqi, category=category)
    
    return render_template('index.html', aqi=None, category=None)

if __name__ == '__main__':
    app.run(debug=True)
