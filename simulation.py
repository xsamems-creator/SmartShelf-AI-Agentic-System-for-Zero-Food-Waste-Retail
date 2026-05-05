import pandas as pd
from datetime import datetime

TODAY = pd.to_datetime("2026-05-05")

# Load datasets
inventory = pd.read_csv("inventory.csv", parse_dates=["arrival_date", "expiry_date"])
demand = pd.read_csv("demand.csv")

# -------------------------------
# 🧮 Feature Engineering
# -------------------------------
def compute_features(df):
    df["days_to_expiry"] = (df["expiry_date"] - TODAY).dt.days
    df["sales_velocity"] = df["daily_sales_avg"]
    df["stock_cover_days"] = df["quantity"] / (df["sales_velocity"] + 1e-5)

    # Simple spoilage risk score
    df["spoilage_risk"] = df["stock_cover_days"] / (df["days_to_expiry"] + 1e-5)
    return df

inventory = compute_features(inventory)

# -------------------------------
# 🤖 Pricing Agent Logic
# -------------------------------
def pricing_agent(row):
    if row["spoilage_risk"] > 2:
        return ("discount_40%", "High risk - aggressive markdown")
    elif row["spoilage_risk"] > 1:
        return ("discount_20%", "Moderate risk - mild markdown")
    else:
        return ("no_discount", "Low risk")

# -------------------------------
# 🚚 Logistics Agent Logic
# -------------------------------
def logistics_agent(row, demand_df):
    product_demand = demand_df[demand_df["product_id"] == row["product_id"]]

    if len(product_demand) < 2:
        return None

    current_store = row["store_id"]
    best_store = product_demand.sort_values("daily_demand", ascending=False).iloc[0]["store_id"]

    if best_store != current_store and row["spoilage_risk"] > 1:
        return f"transfer_to_{best_store}"
    return None

# -------------------------------
# 🏪 Store Ops Agent Logic
# -------------------------------
def store_ops_agent(row):
    if row["spoilage_risk"] > 1:
        return "move_to_front"
    return "no_action"

# -------------------------------
# 🔄 Run Simulation
# -------------------------------
decisions = []

for _, row in inventory.iterrows():
    pricing_action, pricing_reason = pricing_agent(row)
    logistics_action = logistics_agent(row, demand)
    ops_action = store_ops_agent(row)

    decisions.append({
        "store_id": row["store_id"],
        "product_id": row["product_id"],
        "spoilage_risk": round(row["spoilage_risk"], 2),
        "pricing_action": pricing_action,
        "logistics_action": logistics_action,
        "store_ops_action": ops_action
    })

decisions_df = pd.DataFrame(decisions)
print(decisions_df)

# Save output
decisions_df.to_csv("decisions_output.csv", index=False)
