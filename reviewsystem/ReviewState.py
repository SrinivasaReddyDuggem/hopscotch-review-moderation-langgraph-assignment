# Part 1a: the state
import operator
from typing import Annotated, Literal, TypedDict

class ReviewState(TypedDict):
    review: dict          # the input: review_id, sku, rating, text
    # the spine (Part 1)
    text: str             # the text, with phone numbers and emails hidden
    kind: str             # praise, question, complaint or abusive
    issue_type: str       # what a complaint is about
    # the complaint lane (Parts 3 and 4)
    complaint_count: int
    return_rate: float
    vendor_alerts: int
    reply: str
    # the question lane (Part 6)
    messages: Annotated[list, operator.add]
    trips: int
    answer: str
    # the outcome (Part 2)
    status: str
     