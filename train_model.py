import pandas as pd
import sys
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config
from src.utils import logger, save_model

def train_models():
    """Trains regression models, evaluates them, and saves the best."""
    logger.info("Starting model training...")
    
    if not os.path.exists(Config.PROCESSED_DATA_PATH):
        logger.error(f"Processed data file not found at {Config.PROCESSED_DATA_PATH}. Please run data_preprocessing.py first.")
        return

    # 1. Load data
    df = pd.read_csv(Config.PROCESSED_DATA_PATH)
    
    X = df[['cpu_usage', 'memory_usage', 'storage_usage', 'network_usage']]
    y = df['cost']
    
    # 2. Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 3. Train Linear Regression model
    logger.info("Training Linear Regression...")
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)
    lr_pred = lr_model.predict(X_test)
    lr_mae = mean_absolute_error(y_test, lr_pred)
    
    # 4. Train Random Forest model
    logger.info("Training Random Forest...")
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    rf_pred = rf_model.predict(X_test)
    rf_mae = mean_absolute_error(y_test, rf_pred)
    
    # 5. Print out model accuracy results (comparing performance using MAE)
    print("\n--- Model Evaluation Results (MAE) ---")
    print(f"Linear Regression MAE : ${lr_mae:.2f}")
    print(f"Random Forest MAE     : ${rf_mae:.2f}")
    print("--------------------------------------")
    
    # Save the models
    save_model(lr_model, Config.LINEAR_REGRESSION_MODEL)
    save_model(rf_model, Config.RANDOM_FOREST_MODEL)
    
    # Save metrics to json for dashboard
    import json
    metrics = {
        "linear_regression_mae": float(lr_mae),
        "random_forest_mae": float(rf_mae)
    }
    with open(os.path.join(Config.MODELS_DIR, 'metrics.json'), 'w') as f:
        json.dump(metrics, f)
        
if __name__ == "__main__":
    train_models()
