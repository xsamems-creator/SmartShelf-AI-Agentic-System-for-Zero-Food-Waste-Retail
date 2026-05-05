from langgraph.graph import StateGraph, END

from app.state import RetailState
from app.agents.spoilage_agent import spoilage_agent
from app.agents.pricing_agent import pricing_agent
from app.agents.logistics_agent import logistics_agent
from app.agents.store_ops_agent import store_ops_agent
from app.graph.router import route_decision

builder = StateGraph(RetailState)

builder.add_node("spoilage", spoilage_agent)
builder.add_node("pricing", pricing_agent)
builder.add_node("logistics", logistics_agent)
builder.add_node("store_ops", store_ops_agent)

builder.set_entry_point("spoilage")

builder.add_conditional_edges(
    "spoilage",
    route_decision,
    {
        "pricing": "pricing",
        "logistics": "logistics",
        "store_ops": "store_ops"
    }
)

builder.add_edge("pricing", END)
builder.add_edge("logistics", END)
builder.add_edge("store_ops", END)

graph = builder.compile()
