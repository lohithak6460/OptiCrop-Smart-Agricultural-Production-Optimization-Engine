/**
 * OptiCrop Frontend Controller
 * Synchronizes inputs, manages range sliders, and handles live validation.
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Sync Sliders and Number Inputs
    const features = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'];
    
    features.forEach(feature => {
        const numInput = document.getElementById(`input-${feature}`);
        const sliderInput = document.getElementById(`slider-${feature}`);
        const displayVal = document.getElementById(`display-${feature}`);
        
        if (!numInput || !sliderInput) return;

        // Initialize display value
        if (numInput.value === '') {
            numInput.value = sliderInput.value;
        } else {
            sliderInput.value = numInput.value;
        }
        displayVal.textContent = parseFloat(numInput.value).toFixed(feature === 'ph' || feature === 'temperature' ? 1 : 0);

        // Update when slider changes
        sliderInput.addEventListener('input', (e) => {
            const val = parseFloat(e.target.value);
            numInput.value = val;
            displayVal.textContent = val.toFixed(feature === 'ph' || feature === 'temperature' ? 1 : 0);
            validateInput(numInput, feature);
        });

        // Update when number input changes
        numInput.addEventListener('input', (e) => {
            let val = parseFloat(e.target.value);
            if (isNaN(val)) return;

            const min = parseFloat(numInput.getAttribute('min'));
            const max = parseFloat(numInput.getAttribute('max'));
            
            if (val >= min && val <= max) {
                sliderInput.value = val;
                displayVal.textContent = val.toFixed(feature === 'ph' || feature === 'temperature' ? 1 : 0);
            }
            validateInput(numInput, feature);
        });

        // Trigger validation on blur
        numInput.addEventListener('blur', (e) => {
            let val = parseFloat(e.target.value);
            const min = parseFloat(numInput.getAttribute('min'));
            const max = parseFloat(numInput.getAttribute('max'));
            
            if (isNaN(val)) {
                numInput.value = sliderInput.value;
            } else if (val < min) {
                numInput.value = min;
                sliderInput.value = min;
            } else if (val > max) {
                numInput.value = max;
                sliderInput.value = max;
            }
            displayVal.textContent = parseFloat(numInput.value).toFixed(feature === 'ph' || feature === 'temperature' ? 1 : 0);
        });
    });

    // 2. Real-time Input Validation styling
    function validateInput(element, feature) {
        const val = parseFloat(element.value);
        const min = parseFloat(element.getAttribute('min'));
        const max = parseFloat(element.getAttribute('max'));
        const formGroup = document.getElementById(`group-${feature}`);

        if (isNaN(val) || val < min || val > max) {
            element.style.borderColor = '#ef4444'; // Red
            if (formGroup) {
                formGroup.classList.add('has-error');
            }
        } else {
            element.style.borderColor = ''; // Default
            if (formGroup) {
                formGroup.classList.remove('has-error');
            }
        }
    }

    // 3. Dynamic target selection prompt styling
    const targetCropSelect = document.getElementById('target_crop');
    if (targetCropSelect) {
        targetCropSelect.addEventListener('change', (e) => {
            const selectValue = e.target.value;
            const container = document.getElementById('group-target-crop');
            
            if (selectValue !== '__recommended__') {
                container.style.boxShadow = '0 0 12px rgba(245, 158, 11, 0.15)';
                container.style.borderColor = 'rgba(245, 158, 11, 0.4)';
            } else {
                container.style.boxShadow = '';
                container.style.borderColor = '';
            }
        });
    }

    // 4. Smooth alert fading
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            alert.style.transform = 'translateY(-10px)';
            alert.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            setTimeout(() => {
                alert.remove();
            }, 500);
        }, 6000);
    });
});
