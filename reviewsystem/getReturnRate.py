

from reviewsystem.ReviewState import ReviewState

from reviewsystem.data import PRODUCTS, BATCH_SALES

def get_return_rate(state: ReviewState) -> dict:
    sku = state.get("review", {}).get("sku", "unknown")
    product = PRODUCTS.get(sku, {})
    batchID = product.get("batch_id", 0)
    print("BatchID" , batchID)
    batch_sales = BATCH_SALES.get(batchID, {})
    returned = batch_sales.get("returned", 0)
    return {"return_rate": returned}

print(get_return_rate({"kind": "review", "review": {"sku": "HS-201"}}))