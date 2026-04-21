from fpdf import FPDF
import os

# Configuration
OUTPUT_FILE = "AI_Cloud_Cost_Optimizer_Presentation.pdf"
IMAGE_PATH = r"C:\Users\Mounish Royal\.gemini\antigravity\brain\eda395ff-2c9d-4486-a05e-00348456908c\cloud_cost_architecture_1776581173359.png"

class PDF(FPDF):
    def header(self):
        # Arial bold 15
        self.set_font('helvetica', 'B', 15)
        # Move to the right
        # self.cell(80)
        # Title
        # self.cell(30, 10, 'Title', 1, 0, 'C')
        # Line break
        # self.ln(10)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('helvetica', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

def create_pdf():
    # Landscape orientation, A4 size
    pdf = PDF(orientation='L', unit='mm', format='A4')
    pdf.alias_nb_pages()
    
    # --- DATA & SLIDES ---
    slides = [
        {
            "title": "AI-Based Cloud Cost Optimizer",
            "content": [
                "Final Year Project Viva Presentation",
                "Presented by: [Your Name]",
                "Roll No: [Your ID]",
                "Guided by: [Advisor Name]",
                "Department: Computer Science"
            ],
            "is_title": True
        },
        {
            "title": "Introduction",
            "content": [
                "- Rapid growth of Cloud Computing services (AWS, Azure, GCP).",
                "- Organizations face 'Cloud Sprawl' and uncontrolled resource scaling.",
                "- Cloud bill management is becoming a critical business challenge.",
                "- Need for an automated, AI-driven solution to optimize spending without impacting performance."
            ]
        },
        {
            "title": "Motivation",
            "content": [
                "- Financial Impact: Businesses lose up to 30% of cloud spend on idle resources.",
                "- Complexity: Multi-cloud pricing models are opaque and hard to track.",
                "- Scalability: Manual rightsizing cannot keep up with dynamic workloads.",
                "- Predictive Insights: Traditional tools are reactive, not proactive."
            ]
        },
        {
            "title": "Problem Statement",
            "content": [
                "- Identify and analyze the inefficiencies in cloud resource allocation.",
                "- Inability of existing tools to provide human-readable explanations for cost changes.",
                "- Developing a system that not only predicts costs but also optimizes them using rightsizing heuristics.",
                "- Bridging the gap between raw data metrics and actionable cost-saving decisions."
            ]
        },
        {
            "title": "Project Objectives",
            "content": [
                "- Develop a Machine Learning model to predict cloud costs based on resource usage.",
                "- Implement a 'Rightsizing' engine to suggest optimal resource configurations.",
                "- Integrate Explainable AI (XAI) using LLMs for natural language reasoning.",
                "- Build a user-friendly dashboard for real-time monitoring and optimization."
            ]
        },
        {
            "title": "Scope of the Project",
            "content": [
                "- Focus Area: Compute (CPU), Memory (RAM), Storage, and Network I/O.",
                "- Platforms: Generic cloud resource modeling (applicable to AWS/Azure/GCP).",
                "- Target: SME's and Developers looking for cost transparency.",
                "- Technologies: Python, Scikit-Learn, Flask, Ollama/Llama-3."
            ]
        },
        {
            "title": "Literature Review",
            "content": [
                "- CloudHealth & Flexera: Enterprise-grade but high entry cost.",
                "- AWS Cost Explorer: Platform-specific and misses third-party integrations.",
                "- Research Papers: Focus on VM scheduling and load balancing but lack user-centric explainability.",
                "- Our approach combines ML prediction + Dynamic Rightsizing + LLM explanations."
            ]
        },
        {
            "title": "Gap Analysis",
            "content": [
                "- Lack of real-time predictive modeling in standard cloud dashboards.",
                "- Absence of 'Why': Tools tell you cost went up, but not the narrative behind it.",
                "- Dependency on static thresholds rather than dynamic workload patterns.",
                "- The need for a localized AI solution (Ollama) to keep financial data private."
            ]
        },
        {
            "title": "Proposed Methodology",
            "content": [
                "- Phase 1: Synthetic/Real Workload Data Generation.",
                "- Phase 2: Data Preprocessing & Feature Engineering.",
                "- Phase 3: Training Regressive ML Models (Linear vs. Random Forest).",
                "- Phase 4: Optimization Engine development (Rightsizing Heuristics).",
                "- Phase 5: XAI Integration with Llama-3.",
                "- Phase 6: Web Dashboard Integration."
            ]
        },
        {
            "title": "System Architecture",
            "content": [],
            "image": IMAGE_PATH
        },
        {
            "title": "Dataset and Attributes",
            "content": [
                "- Features (X): CPU Usage (%), Memory Usage (GB), Storage (GB), Network Traffic (GB).",
                "- Target (y): Hourly Cloud Hosting Cost ($).",
                "- Dataset Source: Simulated cloud provider logs covering diversos workload scenarios.",
                "- Scaling: Standardized scaling for distance-based ML algorithms."
            ]
        },
        {
            "title": "Data Preprocessing",
            "content": [
                "- Cleaning: Handling missing values and removing noise.",
                "- Normalization: Scaling features to [0,1] range for better model convergence.",
                "- Splitting: 80% Training set, 20% Testing set.",
                "- Validation: Using Mean Absolute Error (MAE) and R-squared metrics."
            ]
        },
        {
            "title": "Machine Learning: Linear Regression",
            "content": [
                "- Utilized as a baseline model for project evaluation.",
                "- Captures linear trends between resource growth and cost escalation.",
                "- Pros: Interpretable, fast, low computational overhead.",
                "- Cons: Struggles with non-linear pricing jumps (e.g., tiered storage costs)."
            ]
        },
        {
            "title": "Machine Learning: Random Forest",
            "content": [
                "- Ensemble learning method using multiple Decision Trees.",
                "- Handles complex, non-linear relationships in cloud billing data.",
                "- Reduces overfitting through bagging and feature randomness.",
                "- Hyperparameters: 100 Estimators, Random State 42 for reproducibility."
            ]
        },
                {
            "title": "Optimization Logic (Rightsizing)",
            "content": [
                "- Rightsizing: Matching instance size to actual performance requirements.",
                "- Heuristic logic: Scale down resources by 20-30% if utilization is low (<50%).",
                "- Lower Bounds: Ensuring system stability by maintaining minimum resource floors.",
                "- Cost Savings: Predicted via the Random Forest model on 'optimized' features."
            ]
        },
        {
            "title": "Explainable AI (XAI) with Ollama",
            "content": [
                "- Powered by Llama-3 (localized installation via Ollama).",
                "- Input: Original cost, Optimized cost, and Savings percentage.",
                "- Output: 2-3 sentence executive summary explaining the ROI.",
                "- Benefit: Increases user trust and transparency in AI recommendations."
            ]
        },
        {
            "title": "Implementation Environment",
            "content": [
                "- Backend: Python 3.10+, Flask 3.0.",
                "- Frontend: HTML5, CSS3, Jinja2 Templates.",
                "- ML: Scikit-Learn, Pandas, NumPy.",
                "- LLM Host: Ollama (running Llama-3 model).",
                "- Monitoring: Python 'Logging' module for system health tracking."
            ]
        },
        {
            "title": "Results - Model Performance",
            "content": [
                "- Linear Regression MAE: $9.16",
                "- Random Forest MAE: $6.64 (Chosen Model)",
                "- Random Forest improved accuracy by ~27% over Linear Regression.",
                "- The model accurately reflects the variance in cloud resource costs."
            ]
        },
        {
            "title": "Results - Cost Savings",
            "content": [
                "- Average identified savings: 15% - 25% per environment.",
                "- High Savings Case: Over-provisioned databases (>80% savings identified).",
                "- Stable Performance: Optimized resources remain above safety thresholds.",
                "- Real-time ROI calculation for stakeholders."
            ]
        },
        {
            "title": "Software Demonstration",
            "content": [
                "- Key Screens: Input Dashboard, Prediction Graphs, Optimization Summary.",
                "- API Integration: RESTful endpoints for external consumption.",
                "- AI Chat: Interactive explanations generated on-the-fly.",
                "- Responsiveness: Modern UI accessible from multiple devices."
            ]
        },
        {
            "title": "Conclusion",
            "content": [
                "- Successfully developed an AI-driven framework for cloud cost reduction.",
                "- Demonstrated that Random Forest is highly effective for cost prediction.",
                "- LLM integration (Ollama) effectively bridges the gap between data and human understanding.",
                "- Proposed system provides a blueprint for private, localized cloud optimization."
            ]
        },
        {
            "title": "Future Scope & References",
            "content": [
                "- Multi-cloud Support: Ingesting AWS/Azure pricing SDKs directly.",
                "- Auto-Scaling: Automated API triggers to shut down idle resources.",
                "- Container Analysis: K8s resource optimization focus.",
                "- References: [1] Cloud FinOps (O'Reilly), [2] Scikit-Learn Docs, [3] Ollama API Spec."
            ]
        }
    ]

    for slide in slides:
        pdf.add_page()
        
        # Draw background rectangle for header
        pdf.set_fill_color(30, 60, 100) # Dark Blue
        pdf.rect(0, 0, 297, 30, 'F')
        
        # Set Title
        pdf.set_font('helvetica', 'B', 24)
        pdf.set_text_color(255, 255, 255) # White
        pdf.set_xy(10, 10)
        pdf.cell(0, 10, slide["title"], ln=True)
        
        pdf.set_text_color(0, 0, 0) # Black
        pdf.set_font('helvetica', '', 16)
        pdf.set_y(40)
        
        if slide.get("is_title"):
            pdf.set_font('helvetica', 'B', 32)
            pdf.set_y(80)
            for line in slide["content"]:
                pdf.cell(0, 15, line, ln=True, align='C')
        elif slide.get("image"):
            if os.path.exists(slide["image"]):
                pdf.image(slide["image"], x=50, y=40, w=200)
            else:
                pdf.set_font('helvetica', 'I', 12)
                pdf.cell(0, 10, "[Architecture Diagram Image Not Found]", ln=True)
        else:
            for line in slide["content"]:
                pdf.multi_cell(0, 12, line)
                pdf.ln(2)

    pdf.output(OUTPUT_FILE)
    print(f"PDF saved as {OUTPUT_FILE}")

if __name__ == "__main__":
    create_pdf()
