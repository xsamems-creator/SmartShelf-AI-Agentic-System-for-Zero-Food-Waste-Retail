def route_decision(state):
    if state["spoilage_risk"] > 1:
        return ["pricing", "logistics", "store_ops"]
    return ["pricing"]
