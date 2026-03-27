# 🚀 LLM Benchmark Dashboard (Groq API)

## 📌 Overview

This project is a **benchmarking dashboard** designed to evaluate Large Language Models (LLMs) based on real-world performance metrics such as **latency, cost, and response quality**.

It helps developers and startups make informed decisions when choosing an LLM for applications like customer support bots.

---

## 🎯 Features

* ✅ Multi-prompt evaluation
* ⚡ Real-time response generation using Groq API
* ⏱ Latency tracking (response time measurement)
* 💰 Token-based cost estimation
* 🧠 Rule-based quality scoring (accuracy, brevity, tone)
* 📊 Interactive dashboard using Streamlit
* 📋 Tabular comparison of results

---

## 🧠 How It Works

1. User enters multiple prompts
2. Each prompt is sent to the LLM via API
3. System captures:

   * Response
   * Latency
   * Token usage
4. Calculates:

   * Estimated cost
   * Quality score
5. Displays results in a structured comparison table

---

## 🛠️ Tech Stack

* **Language:** Python
* **UI:** Streamlit
* **LLM API:** Groq
* **Data Handling:** Pandas

---

## 📂 Project Structure

```
llm-benchmark-dashboard/
│
├── app.py              # Streamlit dashboard
├── requirements.txt   # Dependencies
├── README.md          # Project documentation
└── screenshots/       # (Optional) UI images
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/llm-benchmark-dashboard.git
cd llm-benchmark-dashboard
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```
streamlit run app.py
```

---

## 🔑 API Key Setup

* Get your API key from Groq
* Enter it in the Streamlit UI when prompted

---

## 📊 Example Output

| Model | Prompt                | Latency | Tokens | Cost     | Quality |
| ----- | --------------------- | ------- | ------ | -------- | ------- |
| Groq  | Explain refund policy | 1.8s    | 766    | 0.000766 | 7       |

---

## 🧪 Evaluation Metrics

### ⏱ Latency

* Measures response time of the model

### 💰 Cost

* Estimated using token usage

### 🧠 Quality Score

Rule-based scoring based on:

* **Accuracy** → Response length & completeness
* **Brevity** → Short and concise answers
* **Tone** → Politeness and friendliness

---

## ⚖️ Trade-off Analysis

This project highlights real-world trade-offs:

* Faster models may have lower quality
* Higher quality models may cost more
* Helps choose optimal balance for production systems

---


* Groq API for fast LLM inference
* Streamlit for rapid UI development

---
