
from reviewsystem.ReviewState import ReviewState
from reviewsystem.data import PRODUCTS
from reviewsystem.data import VENDOR_ALERTS

def vendor_record(state: ReviewState) -> dict:
    sku = state.get("review", {}).get("sku", "unknown")
    product = PRODUCTS.get(sku, {})
    vendorID = product.get("vendor_id", "unknown")
    alert = VENDOR_ALERTS.get(vendorID, {})
    return {"vendor_alerts": alert}

print(vendor_record({"kind": "review", "review": {"sku": "HS-201"}}))