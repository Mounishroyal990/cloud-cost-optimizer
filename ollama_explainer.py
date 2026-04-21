import requests
import json
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config
from src.utils import logger

def explain_optimization(optimization_results):
    """
    Connects to local Ollama API to generate a human-readable explanation
    of the optimization results in simple language.
    """
    try:
        orig = optimization_results['original']
        opt = optimization_results['optimized']
        sav = optimization_results['savings']
        
        prompt = f"""
        You are a Cloud Cost Optimization Expert. Explain the following resource optimization to a client in 2-3 short, clear sentences. 
        Focus on the savings and the main reductions. Don't be overly technical.
        
        Original Usage: CPU {orig['cpu']}%, Memory {orig['memory']}GB, Storage {orig['storage']}GB, Network {orig['network']}GB. Cost: ${orig['cost']:.2f}.
        Optimized Usage: CPU {opt['cpu']}%, Memory {opt['memory']}GB, Storage {opt['storage']}GB, Network {opt['network']}GB. Cost: ${opt['cost']:.2f}.
        Savings: ${sav['dollars']:.2f} ({sav['percentage']:.1f}%).
        """
        
        payload = {
            "model": Config.OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        }
        
        logger.info(f"Sending prompt to Ollama model {Config.OLLAMA_MODEL}...")
        response = requests.post(Config.OLLAMA_API_URL, json=payload, timeout=15)
        
        if response.status_code == 200:
            data = response.json()
            return data.get("response", "Could not parse response from Ollama.")
            
        else:
             logger.warning(f"Ollama returned status code {response.status_code}")
             return f"Optimization achieved a {sav['percentage']:.1f}% cost reduction! (Note: Local Ollama AI explanation is currently offline. Status: {response.status_code})"

    except requests.exceptions.RequestException as e:
        logger.warning(f"Failed to connect to Ollama: {e}")
        return f"By rightsizing your resources, we've successfully reduced your projected cloud bill by {sav['percentage']:.1f}%. (Fallback explanation: AI generation service is offline)."
    except Exception as e:
        logger.error(f"Error generating explanation: {e}")
        return "Explanation could not be generated at this time."

if __name__ == "__main__":
    test_data = {
        "original": {"cpu": 80, "memory": 64, "storage": 1000, "network": 200, "cost": 150.0},
        "optimized": {"cpu": 56, "memory": 51, "storage": 850, "network": 160, "cost": 110.0},
        "savings": {"dollars": 40.0, "percentage": 26.6}
    }
    explanation = explain_optimization(test_data)
    print("\n--- AI Explanation ---")
    print(explanation)
