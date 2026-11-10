def review(review_id, sku, rating, text):
    return {"review_id": review_id, "sku": sku, "rating": rating, "text": text}

REVIEWS = [
    review("R-1", "HS-118", 5, "Lovely soft fabric, my son wears it every day."),
    review("R-2", "HS-201", 4, "Pretty frock! Machine washable? Is 4-5Y in stock?"),
    review("R-3", "HS-201", 2, "The colours bled into each other after the very first wash."),
    review("R-4", "HS-305", 2, "One strap button came off after a week. Otherwise good."),
    review("R-5", "HS-412", 1, "Worst shoes ever, you idiots. Call me on 98200 11223."),
    review("R-6", "HS-201", 5, "Great deals on kids wear at http://cheap-kids-wear.biz"),
    review("R-7", "HS-118", 4, "My daughter is 108 cm: which size, and is it in stock?"),
]

# Part 3a: made-up data, standing in for Hopscotch's databases

# which vendor made each product, and in which batch
PRODUCTS = {
    "HS-118": {"vendor_id": "V2", "batch_id": "B4"},
    "HS-201": {"vendor_id": "V3", "batch_id": "B7"},
    "HS-305": {"vendor_id": "V1", "batch_id": "B2"},
    "HS-412": {"vendor_id": "V4", "batch_id": "B9"},
}

# how many complaints each (product, issue) had in the last 14 days
COMPLAINTS_14_DAYS = {
    ("HS-201", "quality_defect"): 6,
    ("HS-305", "quality_defect"): 1,
    ("HS-118", "size_fit"): 3,
}

# units sold and returned, per batch
BATCH_SALES = {
    "B4": {"sold": 800, "returned": 40},
    "B7": {"sold": 400, "returned": 64},
    "B2": {"sold": 600, "returned": 18},
    "B9": {"sold": 300, "returned": 9},
}

# quality alerts each vendor already had in the last 90 days
VENDOR_ALERTS = {"V1": 0, "V2": 1, "V3": 2, "V4": 0}



