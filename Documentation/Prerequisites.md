# OptiCrop: Prerequisites & Installation Guide

This document lists the system requirements, library dependencies, and configuration commands to build and run the **Smart Agricultural Production Optimization Engine (OptiCrop)**.

---

## 1. System Requirements

*   **Operating System:** Windows, macOS, or Linux.
*   **Language Runtime:** Python 3.8+ (Python 3.10+ recommended).
*   **Browser:** Modern web browser supporting CSS variables and Backdrop filters (Chrome 80+, Safari 13.1+, Edge 80+, Firefox 75+).

---

## 2. Core Python Libraries

The Python libraries required are specified in the main `requirements.txt` file:

| Package | Version Range | Purpose |
| :--- | :--- | :--- |
| **flask** | >= 3.0.0 | Web application backend router & HTML rendering |
| **numpy** | >= 1.20.0 | Numerical array management |
| **pandas** | >= 1.3.0 | Dataframe parsing & manipulation |
| **scikit-learn**| >= 1.0.0 | ML Pipelines, preprocessing scales, Random Forest |
| **matplotlib** | >= 3.4.0 | Non-interactive data visualization plots generator |
| **seaborn** | >= 0.11.0 | Statistical correlation heatmaps |
| **joblib** | >= 1.1.0 | Serialization & storage of ML pipeline `.pkl` files |
| **pytest** | - | Automated unit testing execution |
| **gunicorn** | - | Production WSGI HTTP server |

---

## 3. Quickstart Commands

To set up the project environment locally:

```bash
# 1. Clone the project workspace
git clone https://github.com/your-username/OptiCrop.git
cd OptiCrop

# 2. Create and activate virtual environment
python -m venv venv
# On Windows powershell:
.\venv\Scripts\Activate.ps1
# On macOS/Linux:
source venv/bin/activate

# 3. Install required libraries
pip install -r requirements.txt

# 4. Generate defaults and run EDA analysis
python Data_Analysis/exploratory_analysis.py

# 5. Train and save model pipeline
python -m Machine_Learning.train

# 6. Execute server
python Application_Development/app.py
```
