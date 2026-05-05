def pricing_agent(state):
    risk = state["spoilage_risk"]

    if risk > 2:
        action = "discount_40%"
    elif risk > 1:
        action = "discount_20%"
    else:
        action = "no_discount"

    state["actions"].append({"agent": "pricing", "decision": action})
    return state
