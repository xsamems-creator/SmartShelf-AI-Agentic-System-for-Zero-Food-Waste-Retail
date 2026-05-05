def logistics_agent(state):
    if state["spoilage_risk"] > 1:
        action = "transfer_to_high_demand_store"
    else:
        action = "no_transfer"

    state["actions"].append({"agent": "logistics", "decision": action})
    return state
