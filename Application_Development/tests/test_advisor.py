import os
import sys
import unittest

# Append project root directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Machine_Learning.advisor import CropAdvisor

class TestCropAdvisor(unittest.TestCase):
    def test_load_defaults(self):
        """Test defaults are loaded from JSON."""
        defaults = CropAdvisor.load_defaults()
        self.assertIsInstance(defaults, dict)
        self.assertTrue(len(defaults) > 0)
        self.assertIn('rice', defaults)

    def test_get_crops_list(self):
        """Test listing crops returns sorted array."""
        crops = CropAdvisor.get_crops_list()
        self.assertIsInstance(crops, list)
        self.assertIn('rice', crops)
        self.assertIn('maize', crops)

    def test_analyze_and_optimize(self):
        """Test optimization advice generates correct offset status and severities."""
        rice_ideals = CropAdvisor.load_defaults().get('rice')
        self.assertIsNotNone(rice_ideals)
        
        # Test exact match
        report = CropAdvisor.analyze_and_optimize('rice', rice_ideals)
        self.assertEqual(report['status'], 'success')
        self.assertEqual(report['deviations_count'], 0)
        self.assertEqual(report['advice']['N']['status'], 'Optimal')
        self.assertEqual(report['advice']['N']['severity'], 'success')

        # Test Nitrogen Deficient match
        deviated_inputs = rice_ideals.copy()
        deviated_inputs['N'] = 5 # Extremely deficient
        
        report_def = CropAdvisor.analyze_and_optimize('rice', deviated_inputs)
        self.assertEqual(report_def['advice']['N']['status'], 'Deficient')
        self.assertEqual(report_def['advice']['N']['severity'], 'danger')
        self.assertTrue(report_def['deviations_count'] >= 1)

if __name__ == '__main__':
    unittest.main()
