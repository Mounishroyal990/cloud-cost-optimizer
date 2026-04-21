import os

class Config:
    # Base directory
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    # Data Paths
    DATA_DIR = os.path.join(BASE_DIR, 'data')
    RAW_DATA_PATH = os.path.join(DATA_DIR, 'raw', 'cloud_data.csv')
    PROCESSED_DATA_PATH = os.path.join(DATA_DIR, 'processed', 'clean_data.csv')
    
    # Model Paths
    MODELS_DIR = os.path.join(BASE_DIR, 'models')
    LINEAR_REGRESSION_MODEL = os.path.join(MODELS_DIR, 'linear_regression.pkl')
    RANDOM_FOREST_MODEL = os.path.join(MODELS_DIR, 'random_forest.pkl')
    SCALER_PATH = os.path.join(MODELS_DIR, 'scaler.pkl')
    
    # API & LLM Settings
    OLLAMA_API_URL = "http://localhost:11434/api/generate"
    OLLAMA_MODEL = "llama3"
    
    # Flask settings
    FLASK_HOST = '0.0.0.0'
    FLASK_PORT = 5000
    DEBUG = True
