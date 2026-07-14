import os

# Base Directories - resolves to project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_PATH = os.path.join(BASE_DIR, 'Data_Analysis', 'dataset', 'Crop_recommendation.csv')
MODEL_DIR = os.path.join(BASE_DIR, 'Machine_Learning', 'trained_models')
MODEL_PATH = os.path.join(MODEL_DIR, 'crop_recommendation_model.pkl')

# Expected inputs and range limits for validation
FEATURES_CONFIG = {
    'N': {'name': 'Nitrogen', 'min': 0, 'max': 150, 'unit': 'mg/kg'},
    'P': {'name': 'Phosphorus', 'min': 5, 'max': 145, 'unit': 'mg/kg'},
    'K': {'name': 'Potassium', 'min': 5, 'max': 205, 'unit': 'mg/kg'},
    'temperature': {'name': 'Temperature', 'min': 0, 'max': 50, 'unit': '°C'},
    'humidity': {'name': 'Humidity', 'min': 10, 'max': 100, 'unit': '%'},
    'ph': {'name': 'Soil pH', 'min': 3.5, 'max': 10.0, 'unit': ''},
    'rainfall': {'name': 'Rainfall', 'min': 20, 'max': 300, 'unit': 'mm'}
}
