# LLM-Benchmark-Dashboard-Groq-API-

📌 Overview

This project is a benchmarking dashboard to evaluate Large Language Models (LLMs) based on:

Latency (response time)
Cost (token-based estimation)
Quality (accuracy, brevity, tone)
⚙️ Features
Multi-prompt evaluation
Real-time LLM responses using Groq API
Latency tracking
Token usage tracking
Cost estimation
Rule-based quality scoring
Interactive Streamlit UI
🧠 How It Works
User inputs multiple prompts
Each prompt is sent to the LLM
System collects:
Response
Latency
Tokens
Calculates:
Cost
Quality Score
Displays results in a comparison table
🛠️ Tech Stack
Python
Streamlit
Groq API
Pandas
🚀 Run Locally
pip install -r requirements.txt
streamlit run app.py
📊 Example Output
Prompt	Latency	Tokens	Cost	Quality
Explain refund policy	1.8s	766	0.000766	7
