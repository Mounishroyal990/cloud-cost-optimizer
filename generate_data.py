import pandas as pd
import numpy as np
import os
import sys

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config
from src.utils import logger

def generate_synthetic_data(num_samples=500):
    """Generates synthetic cloud resource usage data."""
    logger.info(f"Generating {num_samples} samples of synthetic data...")
    
    np.random.seed(42)
    
    # Generate features
    # usage percentages 0 to 100
    cpu_usage = np.random.uniform(5.0, 99.0, num_samples)      
    memory_usage = np.random.uniform(10.0, 95.0, num_samples) 
    
    # storage in GB (50 GB to 2000 GB)
    storage_usage = np.random.uniform(50.0, 2000.0, num_samples) 
    
    # network traffic in GB (1 GB to 500 GB)
    network_usage = np.random.uniform(1.0, 500.0, num_samples)   
    
    # Intentionally add some NA values and duplicates for preprocessing to handle
    cpu_usage[np.random.choice(num_samples, 5, replace=False)] = np.nan
    memory_usage[np.random.choice(num_samples, 5, replace=False)] = np.nan
    
    # Calculate Cost (Base Cost + Usage Variables + Complex Non-Linearities + Noise)
    # E.g. $0.05 per CPU unit, $0.02 per Memory unit, $0.01 per GB Storage, $0.15 per GB Network
    base_cost = 20.0
    
    # 1. Base Linear Component
    cost = (base_cost + 
            (cpu_usage * 0.4) + 
            (memory_usage * 0.15) + 
            (storage_usage * 0.03) + 
            (network_usage * 0.10))
    
    # 2. Non-Linear Tiers: High Usage Surcharge (Simulating "Burst" pricing)
    # If CPU > 85%, add a flat $30 penalty for premium tier
    cost += np.where(cpu_usage > 85, 30.0, 0.0)
    
    # 3. Resource Interaction: High CPU + High Network = Extra overhead cost
    # This is something Linear Regression cannot easily capture
    cost += (cpu_usage * network_usage * 0.002)
    
    # 4. Exponential Storage Growth: Larger storage clusters are harder to manage
    cost += (storage_usage ** 1.2) * 0.01
    
    # 5. Random Noise
    cost += np.random.normal(0, 3.0, num_samples)

    # To ensure no negative costs
    cost = np.where(cost < base_cost, base_cost, cost)
    
    df = pd.DataFrame({
        'cpu_usage': cpu_usage,
        'memory_usage': memory_usage,
        'storage_usage': storage_usage,
        'network_usage': network_usage,
        'cost': cost
    })
    
    # Add a few duplicate rows
    duplicates = df.sample(n=10, random_state=42)
    df = pd.concat([df, duplicates], ignore_index=True)
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(Config.RAW_DATA_PATH), exist_ok=True)
    
    # Save to CSV
    df.to_csv(Config.RAW_DATA_PATH, index=False)
    logger.info(f"Successfully generated and saved data to {Config.RAW_DATA_PATH}")

if __name__ == "__main__":
    generate_synthetic_data(600)
