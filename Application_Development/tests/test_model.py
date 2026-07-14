import os
import sys
import unittest

# Append project root directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Machine_Learning.predict import CropPredictor

class TestCropPredictor(unittest.TestCase):
    def test_model_loaded(self):
        """Test that the singleton model loads successfully."""
        model = CropPredictor.get_model()
        self.assertIsNotNone(model)

    def test_prediction_output(self):
        """Test that the prediction returns the expected format and confidence range."""
        dummy_inputs = {
            'N': 90,
            'P': 42,
            'K': 43,
            'temperature': 20.87,
            'humidity': 82.0,
            'ph': 6.5,
            'rainfall': 202.93
        }
        result = CropPredictor.predict(dummy_inputs)
        
        self.assertIn('crop', result)
        self.assertIn('confidence', result)
        self.assertIsInstance(result['crop'], str)
        self.assertIsInstance(result['confidence'], float)
        self.assertTrue(0.0 <= result['confidence'] <= 1.0)
        self.assertEqual(result['crop'].lower(), 'rice')

if __name__ == '__main__':
    unittest.main()
