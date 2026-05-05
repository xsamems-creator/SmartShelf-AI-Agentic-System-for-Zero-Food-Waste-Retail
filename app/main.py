from app.graph.workflow import graph

def run_demo():
    input_state = {
        "product_id": "P101",
        "store_id": "S1",
        "quantity": 80,
        "days_to_expiry": 2,
        "daily_sales_avg": 20,
        "spoilage_risk": 0,
        "actions": []
    }

    result = graph.invoke(input_state)

    print("\n🚀 Final Decision Output:\n")
    print(result)


if __name__ == "__main__":
    run_demo()
