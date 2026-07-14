import os
import sys
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

# Add project root directory to path to allow importing from Machine_Learning
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from Machine_Learning.config import FEATURES_CONFIG
from Machine_Learning.predict import CropPredictor
from Machine_Learning.advisor import CropAdvisor

app = Flask(
    __name__,
    template_folder=os.path.join(PROJECT_ROOT, 'Application_Development', 'templates'),
    static_folder=os.path.join(PROJECT_ROOT, 'Application_Development', 'static')
)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'opti-crop-secure-secret-key-1829371')

@app.route('/')
def home():
    """
    Renders the homepage. Fetches the list of all crop categories from the dataset
    to populate the target crop dropdown list and passes form configurations.
    """
    crops = CropAdvisor.get_crops_list()
    return render_template(
        'index.html', 
        crops=crops, 
        features_config=FEATURES_CONFIG
    )

@app.route('/predict', methods=['POST'])
def predict():
    """
    Handles form submission, validates parameters, performs ML crop prediction,
    and calls the Advisor module to yield nutrient optimization tips.
    """
    try:
        # 1. Parse inputs
        inputs = {}
        for feature in FEATURES_CONFIG.keys():
            val_str = request.form.get(feature)
            if not val_str:
                flash(f"Missing value for {FEATURES_CONFIG[feature]['name']}.", "danger")
                return redirect(url_for('home'))
            
            try:
                val = float(val_str)
            except ValueError:
                flash(f"Value for {FEATURES_CONFIG[feature]['name']} must be a valid number.", "danger")
                return redirect(url_for('home'))
            
            # Validation bounds check
            cfg = FEATURES_CONFIG[feature]
            if val < cfg['min'] or val > cfg['max']:
                flash(f"{cfg['name']} value of {val} must be between {cfg['min']} and {cfg['max']}.", "warning")
                return redirect(url_for('home'))
            
            inputs[feature] = val

        target_crop = request.form.get('target_crop')
        if not target_crop:
            flash("Please select a target crop for optimization.", "danger")
            return redirect(url_for('home'))

        # 2. Run ML Prediction
        prediction_result = CropPredictor.predict(inputs)
        recommended_crop = prediction_result['crop']
        confidence = prediction_result['confidence']

        # If user chooses 'recommended' as target, map it
        if target_crop == '__recommended__':
            target_crop = recommended_crop

        # 3. Run Optimization Advisor Engine
        optimization_report = CropAdvisor.analyze_and_optimize(target_crop, inputs)
        
        if optimization_report.get('status') == 'error':
            flash(optimization_report.get('message'), "danger")
            return redirect(url_for('home'))

        # 4. Render Results
        return render_template(
            'result.html',
            inputs=inputs,
            recommended_crop=recommended_crop.capitalize(),
            confidence=round(confidence * 100, 1),
            target_crop=target_crop.capitalize(),
            report=optimization_report,
            features_config=FEATURES_CONFIG
        )

    except Exception as e:
        app.logger.error(f"Error handling prediction request: {str(e)}", exc_info=True)
        flash(f"An unexpected error occurred during analysis: {str(e)}", "danger")
        return redirect(url_for('home'))

@app.route('/api/crop-defaults')
def api_crop_defaults():
    """
    API endpoint returning crop default values. Useful for updating the frontend
    charts or slider defaults dynamically.
    """
    return jsonify(CropAdvisor.load_defaults())

if __name__ == '__main__':
    # Running Flask local development server
    app.run(debug=True, host='127.0.0.1', port=5000)
