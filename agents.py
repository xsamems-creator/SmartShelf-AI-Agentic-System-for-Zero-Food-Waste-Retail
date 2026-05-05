from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
import pandas as pd

# Load data
inventory = pd.read_csv("inventory.csv")
demand = pd.read_csv("demand.csv")

# -------------------------------
# 🧮 Tool: Spoilage Analysis
# -------------------------------
def analyze_spoilage(product_id: str):
    df = inventory[inventory["product_id"] == product_id]
    return df.to_dict(orient="records")

# -------------------------------
# 💸 Tool: Pricing Decision
# -------------------------------
def pricing_decision(product_id: str):
    df = inventory[inventory["product_id"] == product_id]
    avg_qty = df["quantity"].mean()

    if avg_qty > 50:
        return "Apply 30% discount"
    return "No discount"

# -------------------------------
# 🚚 Tool: Logistics Decision
# -------------------------------
def logistics_decision(product_id: str):
    df = demand[demand["product_id"] == product_id]
    best_store = df.sort_values("daily_demand", ascending=False).iloc[0]["store_id"]
    return f"Move stock to {best_store}"

# -------------------------------
# 🛠️ Register Tools
# -------------------------------
tools = [
    Tool(
        name="Spoilage Analyzer",
        func=analyze_spoilage,
        description="Analyze spoilage risk for a product"
    ),
    Tool(
        name="Pricing Agent",
        func=pricing_decision,
        description="Recommend pricing strategy"
    ),
    Tool(
        name="Logistics Agent",
        func=logistics_decision,
        description="Recommend stock transfer"
    ),
]

# -------------------------------
# 🧠 LLM Setup
# -------------------------------
llm = ChatOpenAI(temperature=0)

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# -------------------------------
# 🚀 Run Agent
# -------------------------------
query = "Analyze milk inventory and suggest actions"
response = agent.run(query)

print(response)
