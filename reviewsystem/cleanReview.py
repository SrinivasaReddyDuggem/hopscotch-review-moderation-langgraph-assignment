
import re
from reviewsystem.ReviewState import ReviewState

def clean_review(state: ReviewState) -> ReviewState:
    text = state["review"]["text"]
    text = re.sub(r"(?<!\d)\d(?:[\s.-]*\d){9}(?!\d)", "[PHONE]", text)
    text = re.sub(r"[^\s@]+@[^\s@]+\.[^\s@]+", "[EMAIL]", text)
    state['text'] = text
    return state

print(clean_review({"review": {"text": "Worst shoes ever, you idiots. Call me on 9820011223"}}))