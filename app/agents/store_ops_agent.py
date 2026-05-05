def store_ops_agent(state):
    if state["spoilage_risk"] > 1:
        action = "move_to_front"
    else:
        action = "no_action"

    state["actions"].append({"agent": "store_ops", "decision": action})
    return state
