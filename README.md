# 🧠 SmartShelf AI — Agentic Retail Optimization

An AI-powered multi-agent system that predicts perishable goods spoilage and autonomously takes actions across pricing, logistics, and store operations.

## 🚀 Features

- 📊 Spoilage prediction using inventory + demand signals
- 💸 Dynamic pricing agent for markdown optimization
- 🚚 Logistics agent for inter-store transfers
- 🏪 Store ops agent for shelf optimization
- 🤖 Built using LangGraph (stateful multi-agent system)

## 🧠 Architecture

Inventory → Spoilage Agent → Decision Router → Action Agents → Final Actions

## ⚙️ Tech Stack

- Python
- LangChain + LangGraph
- Pandas
- FastAPI (optional)

## ▶️ Run Project

```bash
pip install -r requirements.txt
python app/main.py
