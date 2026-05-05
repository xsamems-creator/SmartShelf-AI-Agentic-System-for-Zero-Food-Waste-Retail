def spoilage_agent(state):
    stock_cover = state["quantity"] / (state["daily_sales_avg"] + 1e-5)
    risk = stock_cover / (state["days_to_expiry"] + 1e-5)

    state["spoilage_risk"] = round(risk, 2)
    return state
