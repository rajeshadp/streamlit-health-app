# streamlit-health-app
Excel Dashboard Generator using Groq API (Python)
This project provides a Python-based data processing and dashboard generation tool that works with Excel files and uses the Groq API for fast LLM-powered analysis. The script reads one or more Excel sheets, summarizes data, generates insights, and produces a structured dashboard output (text, JSON, or Markdown) that can be used for reports, applications, or documentation.

What This Project Does

Reads Excel Files
Supports .xlsx and .xls files
Automatically detects sheets
Converts data into Pandas DataFrames
Cleans & Preprocesses Data
Handles missing values
Normalizes column names
Infers basic data types
Sends Relevant Data to Groq LLM
Chunk-safe prompts so large spreadsheets are handled properly

Uses Groq’s hosted Llama 3 models for:
Data summaries
Insights
Patterns
Anomaly detection
Natural-language dashboard creation
