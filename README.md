# OptiCrop: Smart Agricultural Production Optimization Engine

OptiCrop is an ensemble machine learning decision engine and soil chemical advisory system. It is designed to match soil profiles (NPK, pH) and environmental parameters (temperature, humidity, rainfall) to optimal crops, outputting precise correction recommendations.

This codebase is organized exactly like a collaborative team project, structured around distinct **Team Modules** and responsibilities.

---

## 👥 Academic Team & Roles

*   **Team Leader (K Lohitha):** Repository integration, main layouts, backend testing.
*   **Data Analysis Team (Gondinigari Sneha):** Feature profiling and Exploratory Data Analysis.
*   **Business Analysis Team (Jahnavi Dunthala):** BRDs, literature surveys, and agricultural advisory calculations.
*   **Machine Learning Team (Kalagotla Fathima):** Preprocessing, model building, validation (Random Forest).
*   **Application Development Team (Dhanireddy Sirisha):** Flask backend routing, CSS styling, Javascript synchronizations, and deployment.

---

## 📂 Project Structure by Team Module

```
Opti Crop/
│
├── Business_Analysis/                   # Business Analysis Team
│   ├── Business_Problem.md              # Problem definition
│   ├── Business_Requirements.md         # Functional/non-functional requirements
│   └── Literature_Survey_&_Impact.md    # Survey overview & social-business impact
│
├── Data_Analysis/                       # Data Analysis Team
│   ├── dataset/
│   │   └── Crop_recommendation.csv      # Source CSV dataset
│   └── exploratory_analysis.py          # Data distribution parsing & charts script
│
├── Machine_Learning/                    # Machine Learning Team
│   ├── preprocess.py                    # Dataset cleanup & split utilities
│   ├── train.py                         # Model pipeline building & saving
│   ├── predict.py                       # Thread-safe model predictions
│   ├── advisor.py                       # Core soil adjustment recommendations
│   └── crop_defaults.json               # Serialised crop averages database
│
├── Application_Development/             # Application Development Team
│   ├── app.py                           # Flask backend web controller
│   ├── templates/                       # HTML5 dashboards (base, index, result)
│   ├── static/                          # CSS glassmorphic style & synched JS
│   └── tests/                           # Unit tests (models, advisor, backend)
│
├── Documentation/                       # Documentation Team
│   ├── Workflow.md                      # GitFlow, branches, PR review lists
│   ├── ER_Diagram.md                    # Multi-tiered schema & flow charts
│   ├── Prerequisites.md                 # Setup specifications
│   ├── Conclusion.md                    # Project summary outcomes
│   └── README.md                        # Documentation summary index
│
├── Project_Management/                  # Project Management Team
│   ├── Deployment_Guide.md              # Live hosting instructions (Render / PythonAnywhere)
│   └── task.md                          # Interactive tasks checklist
│
├── requirements.txt                     # Shared library dependencies
└── README.md                            # High-level entry guide (this file)
```

---

## ⚡ Quickstart Guide

To run the application locally:

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Generate data benchmarks & train the model:**
    ```bash
    python Data_Analysis/exploratory_analysis.py
    python -m Machine_Learning.train
    ```
3.  **Run the Flask application:**
    ```bash
    python Application_Development/app.py
    ```
4.  **Open in browser:**
    Access `http://127.0.0.1:5000/`.

5.  **Run tests:**
    ```bash
    pytest Application_Development/tests/
    ```
