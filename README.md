# Air Quality Prediction Application

This web application predicts Air Quality Index (AQI) based on various pollutant measurements. It uses a machine learning model trained on global air quality data.

## Features

- Predicts AQI based on PM2.5, PM10, NO2, SO2, CO, O3, and temperature readings
- Provides AQI category classification (Good, Moderate, Unhealthy, etc.)
- Simple and intuitive web interface
- Responsive design

## Technology Stack

- Python 3.8
- Flask web framework
- Scikit-learn for machine learning
- HTML/CSS for frontend
- Pickle for model serialization

## Deployment

This application is configured for deployment on Render.com.

### Requirements

- Python 3.8.12
- Dependencies listed in requirements.txt

### Local Development

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python app.py`
4. Access the application at http://localhost:5000

### Deployment on Render

1. Connect your GitHub repository to Render
2. Create a new Web Service
3. Use the following settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
4. Deploy the application

## Project Structure

- `app.py` - Main Flask application
- `model/` - Directory containing trained ML models
  - `model.pkl` - Trained prediction model
  - `scaler.pkl` - Feature scaler
  - `label_encoder.pkl` - Label encoder for categorical variables
- `templates/` - HTML templates
- `static/` - CSS  files
- `requirements.txt` - Project dependencies
- `Procfile` - Deployment configuration for web servers

.

