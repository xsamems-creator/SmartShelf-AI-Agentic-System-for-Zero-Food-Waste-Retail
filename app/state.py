from typing import TypedDict, List, Dict

class RetailState(TypedDict):
    product_id: str
    store_id: str
    quantity: int
    days_to_expiry: int
    daily_sales_avg: float
    spoilage_risk: float
    actions: List[Dict]
