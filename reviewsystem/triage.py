
from typing import Literal

from reviewsystem.ReviewState import ReviewState

def triage(state : ReviewState):
    
    kind = state["kind"]

    if kind == "complaint":
        return ["count_complaints", "get_return_rate", "vendor_record"]
    elif kind == "praise":
        return "publish_review"
    elif kind == "question":
        return "answer_agent"
    else:  # abusiveORLink
        print("Triage == Hiding abusive or link review")
        return "hide_review"