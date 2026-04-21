import pandas as pd
import os
import sys
from sklearn.preprocessing import StandardScaler
import joblib

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config
from src.utils import logger

def preprocess_data():
    """Loads raw data, cleans it, normalizes features, and saves the cleaned dataset."""
    logger.info("Starting data preprocessing...")
    
    try:
        if not os.path.exists(Config.RAW_DATA_PATH):
           logger.error(f"Raw data file not found at {Config.RAW_DATA_PATH}. Please run generate_data.py first.")
           return
           
        # 1. Load dataset
        df = pd.read_csv(Config.RAW_DATA_PATH)
        initial_shape = df.shape
        logger.info(f"Loaded raw data. Shape: {initial_shape}")
        
        # 2. Remove missing values
        df = df.dropna()
        dropped_na_shape = df.shape
        logger.info(f"Removed missing values. New Shape: {dropped_na_shape} (Removed {initial_shape[0] - dropped_na_shape[0]} rows)")
        
        # 3. Remove duplicates
        df = df.drop_duplicates()
        final_shape = df.shape
        logger.info(f"Removed duplicates. Final Shape: {final_shape} (Removed {dropped_na_shape[0] - final_shape[0]} rows)")

        # 4. Normalize features (Only normalize features, keep target 'cost' unscaled for obvious interpretability)
        features = ['cpu_usage', 'memory_usage', 'storage_usage', 'network_usage']
        scaler = StandardScaler()
        
        # Fit and transform
        df[features] = scaler.fit_transform(df[features])
        
        # Save the scaler so we can transform incoming predict requests
        os.makedirs(os.path.dirname(Config.SCALER_PATH), exist_ok=True)
        joblib.dump(scaler, Config.SCALER_PATH)
        logger.info(f"Scaler saved to {Config.SCALER_PATH}")
        
        # 5. Save cleaned dataset to processed folder
        os.makedirs(os.path.dirname(Config.PROCESSED_DATA_PATH), exist_ok=True)
        df.to_csv(Config.PROCESSED_DATA_PATH, index=False)
        logger.info(f"Cleaned data saved to {Config.PROCESSED_DATA_PATH}")
        
    except Exception as e:
        logger.error(f"An error occurred during preprocessing: {e}")

if __name__ == "__main__":
    preprocess_data()
