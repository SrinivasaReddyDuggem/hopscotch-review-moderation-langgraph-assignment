
from reviewsystem.ReviewState import ReviewState
from reviewsystem.data import COMPLAINTS_14_DAYS

def count_complaints(state: ReviewState) -> dict:
    if state['kind'] == 'complaint':
        sku = state.get("review", {}).get("sku", "unknown")
        complainType = state["issue_type"]
        print(sku, complainType)
       
        count = COMPLAINTS_14_DAYS.get((sku, complainType), 0)
    return {"complaint_count": count}

print(count_complaints({"kind": "complaint", "issue_type": "quality_defect", "review": {"sku": "HS-201"}}))