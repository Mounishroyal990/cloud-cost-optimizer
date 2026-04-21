# AI-Based Cloud Cost Optimization Framework

Provides a dynamic and explainable system to optimize cloud computing footprints. Built using Python, Flask, Scikit-Learn, and Ollama integration.

## Project Description
This framework predicts potential cloud computing costs using machine-learning (Random Forest & Linear Regression). It dynamically suggests reduced hardware configurations ("rightsizing"), and connects to a localized Llama-3 installation to generate user-friendly explanations of the savings.

## File Structure

```
cloud-cost-optimizer/
├── data/
│   ├── raw/
│   └── processed/
├── models/
├── src/
│   ├── generate_data.py
│   ├── data_preprocessing.py
│   ├── train_model.py
│   ├── predict.py
│   ├── optimize.py
│   ├── ollama_explainer.py
│   └── utils.py
├── app/
│   ├── app.py
│   ├── routes.py
│   └── templates/
│       └── index.html
├── notebooks/
│   └── experimentation.ipynb
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

## Installation Steps
1. Navigate to the project directory:
   `cd cloud-cost-optimizer`
2. Create a virtual environment (optional but recommended):
   `python -m venv venv`
   `source venv/bin/activate`  # Windows: `venv\Scripts\activate`
3. Install Dependencies:
   `pip install -r requirements.txt`
4. Setup **Ollama** (Required for Explainability feature):
   - Install Ollama from [ollama.com](https://ollama.com/)
   - Pull the model: `ollama run llama3`

## How to Run Project

### 1. Data Prep and Training Pipeline
Run the following scripts systematically to build datasets and models.
```bash
python src/generate_data.py
python src/data_preprocessing.py
python src/train_model.py
```

### 2. Start the Server
Start the Flask application.
```bash
python run.py
```

### 3. Open Web UI
Point your browser to `http://localhost:5000` to interact with the modern HTML optimization dashboard.

## API Usage
You can hit the optimization API directly via POST.

**Endpoint:** `POST /api/optimize`
**Example Payload:**
```json
{
  "cpu": 85,
  "memory": 64,
  "storage": 1000,
  "network": 250
}
```

**Example Response (abridged):**
```json
{
  "ai_explanation": "By derechosizing your high CPU and memory levels, we successfully lowered projected spending. This approach safely avoids overallocating limits.",
  "optimized_cost": 72.3,
  "predicted_cost": 86.5,
  "savings_dollars": 14.2,
  "savings_percentage": 16.4,
  "optimized_resources": { ... }
}
```

## Future Improvements
- Multi-cloud architecture support (AWS, AZURE, GCP dynamic prices)
- Prometheus metrics ingestion integration
- Dockerization of application layers
