import logging
import joblib
import os

# Configure basic logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def save_model(model, filepath):
    """Saves a machine learning model to disk."""
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        joblib.dump(model, filepath)
        logger.info(f"Model saved successfully to {filepath}")
    except Exception as e:
        logger.error(f"Error saving model to {filepath}: {e}")

def load_model(filepath):
    """Loads a machine learning model from disk."""
    try:
        if not os.path.exists(filepath):
             logger.warning(f"File not found: {filepath}. Return None.")
             return None
        model = joblib.load(filepath)
        logger.info(f"Model loaded successfully from {filepath}")
        return model
    except Exception as e:
        logger.error(f"Error loading model from {filepath}: {e}")
        return None

def validate_input_data(data):
    """Validates the input dictionary used for inferences."""
    required_keys = ['cpu', 'memory', 'storage', 'network']
    for key in required_keys:
        if key not in data:
            logger.error(f"Missing required key in input: {key}")
            return False, f"Missing required key: {key}"
        try:
            val = float(data[key])
            if val < 0:
                 return False, f"Value for {key} cannot be negative."
        except ValueError:
            return False, f"Key '{key}' must be a number."
            
    return True, "Valid"
