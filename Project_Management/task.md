# Task Checklist: Workspace Reorganization

- [x] Restructuring Workspace Directories
    - [x] Create directories for each team heading: `Business_Analysis`, `Data_Analysis`, `Machine_Learning`, `Application_Development`, `Documentation`, `Project_Management`
    - [x] Move existing files to their respective folders
    - [x] Remove deprecated root folders (`src/`, `models/`, `notebooks/`, `docs/`, `static/`, `templates/`, `tests/`)
- [x] Data Analysis Configuration (Data Analysis Team)
    - [x] Move dataset and update paths in `Data_Analysis/exploratory_analysis.py`
    - [x] Execute EDA to build crop ideal values and update analytics images
- [x] Machine Learning Pipeline Reconfiguration (Machine Learning Team)
    - [x] Update import paths in `Machine_Learning/config.py`, `preprocess.py`, `train.py`, `predict.py`, and `advisor.py`
    - [x] Train and save the ML model to `Machine_Learning/trained_models/`
- [x] Flask Backend Reconfiguration (App Dev Team)
    - [x] Update template and static paths in `Application_Development/app.py`
- [x] Team Documentation Setup (Documentation Team)
    - [x] Move and update `Workflow.md`, `ER_Diagram.md`, and create academic reports: `Prerequisites.md`, `Conclusion.md`, `README.md`
- [x] Verification & Testing
    - [x] Move and update test cases inside `Application_Development/tests/`
    - [x] Execute all tests using `pytest`
