import os
import pandas as pd
import numpy as np
import json
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import seaborn as sns
import sys

# Append project root to sys.path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from Machine_Learning.config import DATASET_PATH, BASE_DIR

def run_eda():
    print("--- Starting Exploratory Data Analysis ---")
    
    # Check if dataset exists
    if not os.path.exists(DATASET_PATH):
        raise FileNotFoundError(f"Dataset not found at: {DATASET_PATH}")
        
    df = pd.read_csv(DATASET_PATH)
    print(f"Dataset shape: {df.shape}")
    print("\nColumns and Info:")
    print(df.info())
    
    print("\nSummary Statistics:")
    print(df.describe())
    
    # Ensure static images directory exists inside Application_Development
    images_dir = os.path.join(BASE_DIR, 'Application_Development', 'static', 'images')
    os.makedirs(images_dir, exist_ok=True)
    
    # 1. Generate Correlation Heatmap
    plt.figure(figsize=(10, 8))
    numeric_df = df.drop(columns=['label'])
    corr = numeric_df.corr()
    sns.heatmap(corr, annot=True, cmap='viridis', fmt='.2f', linewidths=0.5)
    plt.title('Correlation Matrix of Soil & Weather Conditions')
    plt.tight_layout()
    corr_img_path = os.path.join(images_dir, 'correlation_matrix.png')
    plt.savefig(corr_img_path, dpi=150)
    plt.close()
    print(f"Saved correlation heatmap to: {corr_img_path}")
    
    # 2. Generate Distribution of features
    fig, axes = plt.subplots(3, 3, figsize=(15, 12))
    features = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
    axes = axes.flatten()
    
    for i, feature in enumerate(features):
        sns.histplot(df[feature], kde=True, ax=axes[i], color='forestgreen')
        axes[i].set_title(f'Distribution of {feature}')
        axes[i].set_xlabel(feature)
        axes[i].set_ylabel('Count')
        
    # Hide unused axes
    for j in range(len(features), len(axes)):
        fig.delaxes(axes[j])
        
    plt.tight_layout()
    dist_img_path = os.path.join(images_dir, 'features_distribution.png')
    plt.savefig(dist_img_path, dpi=150)
    plt.close()
    print(f"Saved features distribution to: {dist_img_path}")
    
    # 3. Generate Crop Nutrient Averages (Soil Optimization Data)
    crop_averages = df.groupby('label').mean().to_dict(orient='index')
    
    # Save to Machine_Learning/crop_defaults.json
    ml_dir = os.path.join(BASE_DIR, 'Machine_Learning')
    os.makedirs(ml_dir, exist_ok=True)
    defaults_path = os.path.join(ml_dir, 'crop_defaults.json')
    
    with open(defaults_path, 'w') as f:
        json.dump(crop_averages, f, indent=4)
        
    print(f"Saved crop ideal nutrient averages to: {defaults_path}")
    print("--- EDA Complete Successfully ---")

if __name__ == '__main__':
    run_eda()
