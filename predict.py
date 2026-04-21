import sys
import os
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config
from src.utils import logger, load_model

def predict_cost(cpu, memory, storage, network):
    """
    Accepts raw resource usages, scales them using the saved scaler, 
    and predicts cloud cost using the trained Random Forest model.
    """
    try:
        # Load the saved Random Forest model
        model = load_model(Config.RANDOM_FOREST_MODEL)
        if model is None:
            raise FileNotFoundError("Random Forest Model not found. Run train_model.py first.")
            
        # Load the saved Linear Regression model
        lr_model = load_model(Config.LINEAR_REGRESSION_MODEL)
            
        # Load the saved scaler
        scaler = load_model(Config.SCALER_PATH)
        if scaler is None:
             raise FileNotFoundError("Scaler not found. Run data_preprocessing.py first.")

        # Create DataFrame for prediction so names match during scaling
        input_data = pd.DataFrame([{
            'cpu_usage': float(cpu),
            'memory_usage': float(memory),
            'storage_usage': float(storage),
            'network_usage': float(network)
        }])
        
        # Scale the input data using the loaded scaler
        scaled_input = scaler.transform(input_data)
        
        # Predict using both models
        rf_prediction = float(model.predict(scaled_input)[0])
        lr_prediction = float(lr_model.predict(scaled_input)[0]) if lr_model else rf_prediction
        
        return {
            'random_forest': rf_prediction,
            'linear_regression': lr_prediction
        }
        
    except Exception as e:
        logger.error(f"Error making prediction: {e}")
        return None

if __name__ == "__main__":
    # Test Prediction Module independently
    predicted = predict_cost(cpu=50, memory=60, storage=1000, network=200)
    print(f"\nPredicted Cost (RF): ${predicted['random_forest']:.2f}")
