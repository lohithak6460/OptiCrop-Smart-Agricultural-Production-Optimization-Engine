import os
import joblib
import pandas as pd
from Machine_Learning.config import MODEL_PATH

class CropPredictor:
    _model = None

    @classmethod
    def get_model(cls):
        """
        Thread-safe singleton model loader. Caches model after loading once.
        """
        if cls._model is None:
            if not os.path.exists(MODEL_PATH):
                raise FileNotFoundError(
                    f"Model file not found at {MODEL_PATH}. "
                    "Please run 'python Data_Analysis/exploratory_analysis.py' followed by "
                    "'python -m Machine_Learning.train' to generate model inputs and train the model."
                )
            cls._model = joblib.load(MODEL_PATH)
        return cls._model

    @classmethod
    def predict(cls, features_dict):
        """
        Given a dictionary of inputs, predict the most suitable crop and confidence.
        Input format: { 'N': 90, 'P': 42, 'K': 43, 'temperature': 20.8, 'humidity': 82, 'ph': 6.5, 'rainfall': 202.9 }
        """
        model = cls.get_model()
        
        # Prepare inputs as a single-row pandas DataFrame
        df_input = pd.DataFrame([features_dict])
        
        # Ensure correct column ordering
        cols = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
        df_input = df_input[cols]
        
        # Get predicted label and probabilities
        prediction = model.predict(df_input)[0]
        
        # Calculate confidence
        probabilities = model.predict_proba(df_input)
        classes = model.classes_
        pred_idx = list(classes).index(prediction)
        confidence = probabilities[0][pred_idx]
        
        return {
            'crop': prediction,
            'confidence': float(confidence)
        }
