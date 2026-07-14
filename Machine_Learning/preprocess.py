import pandas as pd
from sklearn.model_selection import train_test_split
from Machine_Learning.config import DATASET_PATH

def load_data(filepath=DATASET_PATH):
    """
    Loads dataset from CSV and returns features and labels.
    """
    df = pd.read_csv(filepath)
    # Check for missing values and drop if any
    df = df.dropna()
    
    X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
    y = df['label']
    
    return X, y

def prepare_train_test_split(X, y, test_size=0.2, random_state=42):
    """
    Splits features and labels into training and test datasets.
    """
    return train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)
