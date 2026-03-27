import streamlit as st
import pandas as pd
import time
import os
from groq import Groq

# -----------------------------
# Load API Key
# -----------------------------
api_key = st.text_input("Enter GROQ API Key", type="password")

if api_key:
    client = Groq(api_key=api_key)

    # -----------------------------
    # Functions
    # -----------------------------
    def call_groq(prompt):
        start = time.time()

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        end = time.time()

        return {
            "model": "Groq",
            "prompt": prompt,
            "response": response.choices[0].message.content,
            "latency": round(end - start, 2),
            "tokens": response.usage.total_tokens
        }

    def estimate_cost(tokens):
        price_per_token = 0.000001
        return round(tokens * price_per_token, 6)

    def score_quality(response, criteria):
        score = 0

        if "accuracy" in criteria and len(response) > 30:
            score += 3

        if "brevity" in criteria and len(response.split()) < 100:
            score += 3

        if "tone" in criteria:
            if any(word in response.lower() for word in ["thank", "please", "happy"]):
                score += 4

        return score

    # -----------------------------
    # UI Inputs
    # -----------------------------
    st.title("LLM Benchmark Dashboard")

    user_prompts = st.text_area(
        "Enter prompts (one per line)",
        "Explain refund policy\nWrite a professional email\nWhat is AI?"
    )

    criteria = st.multiselect(
        "Select Evaluation Criteria",
        ["accuracy", "brevity", "tone"],
        default=["accuracy", "brevity", "tone"]
    )

    if st.button("Run Benchmark"):
        prompts = user_prompts.split("\n")
        results = []

        with st.spinner("Running benchmark..."):
            for p in prompts:
                res = call_groq(p)
                res["cost"] = estimate_cost(res["tokens"])
                res["quality"] = score_quality(res["response"], criteria)
                results.append(res)

        df = pd.DataFrame(results)

        st.success("Benchmark Completed!")
        st.dataframe(df)

        # Show detailed responses
        st.subheader("Model Responses")
        for r in results:
            st.markdown(f"**Prompt:** {r['prompt']}")
            st.markdown(f"**Response:** {r['response']}")
            st.markdown("---")