import os
import sys
import unittest

# Append project root directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Application_Development.app import app
from Machine_Learning.config import FEATURES_CONFIG

class TestFlaskBackend(unittest.TestCase):
    def setUp(self):
        """Configure test client and disable error trapping."""
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.client = app.test_client()

    def test_home_route(self):
        """Test home route status code and HTML rendering content."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'OptiCrop', response.data)
        self.assertIn(b'Soil & Climate Profiling', response.data)

    def test_api_crop_defaults_route(self):
        """Test API endpoints return crop json defaults."""
        response = self.client.get('/api/crop-defaults')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        
        data = response.get_json()
        self.assertIn('rice', data)

    def test_prediction_route_success(self):
        """Test correct inputs submit successfully and render recommendations."""
        form_data = {
            'N': '90',
            'P': '42',
            'K': '43',
            'temperature': '21.0',
            'humidity': '82.0',
            'ph': '6.5',
            'rainfall': '200.0',
            'target_crop': '__recommended__'
        }
        response = self.client.post('/predict', data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Crop Profiling & Soil Optimization Analysis', response.data)
        self.assertIn(b'Rice', response.data)
        self.assertIn(b'Ideal Crop Match', response.data)

    def test_prediction_route_invalid_ph(self):
        """Test invalid float checks redirect users back with warnings."""
        form_data = {
            'N': '90',
            'P': '42',
            'K': '43',
            'temperature': '21.0',
            'humidity': '82.0',
            'ph': '15.0', # Out of bounds
            'rainfall': '200.0',
            'target_crop': '__recommended__'
        }
        response = self.client.post('/predict', data=form_data)
        self.assertEqual(response.status_code, 302)

if __name__ == '__main__':
    unittest.main()
