import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from groq import Groq

# Initialize Groq client (free API)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("🏥 HealthCare Data Integration + AI Q&A (Groq)")

# --- Folder Selection ---
folder = st.text_input("Enter folder path containing Excel files:")

dataframes = {}

if folder:
    if os.path.isdir(folder):
        excel_files = [f for f in os.listdir(folder) if f.endswith(".xlsx")]
        st.write("Found Excel files:", excel_files)

        for f in excel_files:
            try:
                df = pd.read_excel(os.path.join(folder, f))
                dataframes[f] = df
            except Exception as e:
                st.error(f"Failed to read {f}: {e}")

    else:
        st.error("Invalid folder path. Please check and try again.")

# --- Dashboard Section ---
if dataframes:
    st.header("📊 Dashboard")

    # Combine all Excel data into one DataFrame (if compatible)
    try:
        combined_df = pd.concat(dataframes.values(), ignore_index=True)
        st.write("Combined Data:", combined_df)

        # If columns exist
        if "heart_rate" in combined_df.columns:
            fig, ax = plt.subplots()
            combined_df["heart_rate"].plot(ax=ax, linewidth=2)
            st.pyplot(fig)
    except:
        st.warning("Could not create unified dashboard due to mismatched columns.")

# --- AI Q&A Section ---
st.header("🤖 Ask AI (Groq – FREE)")

user_question = st.text_input("Ask a medical question about the loaded patient data:")

if st.button("Ask"):
    if not dataframes:
        st.error("Please load Excel files first.")
    else:
        # Convert all dataframes to text for context
        context = ""
        for name, df in dataframes.items():
            context += f"\n\nFile: {name}\n"
            context += df.to_string()

        prompt = f"""
You are an expert medical assistant. Use the provided patient health data to answer questions.

Patient Data:
{context}

Question:
{user_question}

Give a detailed medical explanation in simple language.
"""

        with st.spinner("Groq AI thinking..."):
            try:
                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",   # Groq's FREE ultra-fast model
                    messages=[{"role": "user", "content": prompt}]
                )

                answer = response.choices[0].message.content
                st.success(answer)

            except Exception as e:
                st.error(f"Groq API Error: {e}")
