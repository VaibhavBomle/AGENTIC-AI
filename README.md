# AGENTIC-AI-1
# 🚀 Financial AI Agents  

This project demonstrates the power of AI in financial data analysis using the **phi framework** and **Groq LLM**. The system comprises intelligent agents designed to search the web, analyze stock data, and collaborate effectively for better insights.  

## 🛠️ Features  
1. **Web Search Agent**  
   - Retrieves information from the web using DuckDuckGo.  
   - Always includes sources for reliability.  

2. **Financial AI Agent**  
   - Fetches stock prices, analyst recommendations, company news, and financial fundamentals via YFinance.  
   - Presents insights in a structured table format.  

3. **Multi-AI Agent**  
   - Combines the Web Search and Financial AI Agents for seamless collaboration.  
   - Summarizes complex financial insights interactively.  

---

## 🏗️ Steps and Process  

### 1️⃣ **Clone the Repository**  
```bash
git clone <repository-url>
cd <repository-folder>

## Setup environment
```bash
pip install -r requirements.txt

## Setup .env file
```bash
PHIDATA_API_KEY = '<Your PHIData API Key>'
GROQ_API_KEY = '<Your Groq API Key>'

## Run the Agent
```bash
python financial_agents.py



