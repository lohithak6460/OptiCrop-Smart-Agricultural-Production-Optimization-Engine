# Project Deployment Guide

This guide describes how to host the **OptiCrop** web application online on Render and PythonAnywhere.

---

## 1. Deploying on Render (Fully Automated via GitHub)

1.  Push the final codebase to the `main` branch on GitHub.
2.  Log in to [Render](https://render.com/) and click **New +** $\rightarrow$ **Web Service**.
3.  Connect your GitHub repository.
4.  Configure Settings:
    *   **Runtime:** `Python`
    *   **Branch:** `main`
    *   **Build Command:**
        ```bash
        pip install -r requirements.txt && python Data_Analysis/exploratory_analysis.py && python -m Machine_Learning.train
        ```
    *   **Start Command:**
        ```bash
        gunicorn Application_Development.app:app
        ```
5.  Select the **Free** instance and deploy.

---

## 2. Deploying on PythonAnywhere (Manual terminal setup)

1.  Create a free account on [PythonAnywhere](https://www.pythonanywhere.com/).
2.  In a Bash console, clone the repository:
    ```bash
    git clone https://github.com/your-username/OptiCrop.git
    cd OptiCrop
    ```
3.  Set up environment and train:
    ```bash
    mkvirtualenv --python=/usr/bin/python3.10 opti-env
    pip install -r requirements.txt
    python Data_Analysis/exploratory_analysis.py
    python -m Machine_Learning.train
    ```
4.  Add web app manual config, virtualenv path `/home/your-username/.virtualenvs/opti-env`, source path `/home/your-username/OptiCrop`.
5.  Update the WSGI configuration file:
    ```python
    import sys
    import os

    path = '/home/your-username/OptiCrop'
    if path not in sys.path:
         sys.path.append(path)
         
    from Application_Development.app import app as application
    ```
6.  Reload web app.
