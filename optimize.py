import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.predict import predict_cost

def optimize_resources(cpu, memory, storage, network):
    """
    Applies logic to reduce unnecessary resources dynamically,
    calculates original vs optimized cost, and returns savings percentages.
    """
    
    # Simple heuristic optimization:
    # If a resource is high, we scale it down suggesting rightsizing.
    # We maintain a floor to not break things (e.g. CPU floor of 10%).
    
    opt_cpu = max(10, cpu * 0.7 if cpu > 50 else cpu * 0.9)
    opt_memory = max(16, memory * 0.8 if memory > 64 else memory * 0.9)
    opt_storage = max(50, storage * 0.85 if storage > 500 else storage * 0.95)
    opt_network = max(1, network * 0.8 if network > 100 else network * 0.9)
    
    # Calculate costs (returns dict mapping model names to predictions)
    original_preds = predict_cost(cpu, memory, storage, network)
    optimized_preds = predict_cost(opt_cpu, opt_memory, opt_storage, opt_network)
    
    # Base system actions around the better performing Random Forest model
    original_cost = original_preds['random_forest']
    optimized_cost = optimized_preds['random_forest']
    
    # Format return
    savings_dollars = max(0, original_cost - optimized_cost)
    savings_percentage = (savings_dollars / original_cost * 100) if original_cost > 0 else 0
    
    return {
        "original": {
            "cpu": float(cpu),
            "memory": float(memory),
            "storage": float(storage),
            "network": float(network),
            "cost": float(original_cost),
            "lr_cost": float(original_preds['linear_regression'])
        },
        "optimized": {
            "cpu": round(opt_cpu, 2),
            "memory": round(opt_memory, 2),
            "storage": round(opt_storage, 2),
            "network": round(opt_network, 2),
            "cost": float(optimized_cost)
        },
        "savings": {
            "dollars": float(savings_dollars),
            "percentage": float(savings_percentage)
        }
    }
