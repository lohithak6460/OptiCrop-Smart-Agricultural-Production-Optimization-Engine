import os
import joblib
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

from Machine_Learning.config import MODEL_DIR, MODEL_PATH
from Machine_Learning.preprocess import load_data, prepare_train_test_split

def train_and_evaluate():
    print("--- Starting Machine Learning Model Training ---")
    
    # 1. Load and split data
    X, y = load_data()
    X_train, X_test, y_train, y_test = prepare_train_test_split(X, y)
    print(f"Training set shape: {X_train.shape}")
    print(f"Testing set shape: {X_test.shape}")
    
    # 2. Build Pipeline
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1))
    ])
    
    # 3. Fit Model
    print("Training Random Forest model pipeline...")
    pipeline.fit(X_train, y_train)
    
    # 4. Evaluate Model
    y_pred = pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nModel Accuracy: {accuracy * 100:.2f}%")
    
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # 5. Save Model Pipeline
    os.makedirs(MODEL_DIR, exist_ok=True)
    joblib.dump(pipeline, MODEL_PATH)
    print(f"Successfully saved trained model pipeline to: {MODEL_PATH}")
    
    print("--- Model Training Complete ---")

if __name__ == '__main__':
    train_and_evaluate()
