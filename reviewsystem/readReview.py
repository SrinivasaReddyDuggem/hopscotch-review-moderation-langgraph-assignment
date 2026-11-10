
import re

from reviewsystem.ReviewState import ReviewState

ABUSIVE_LINK_WORDS = {"idiot", "idiots", "stupid", "useless","https","http","www"}
COMPLAINT_WORDS = {"worst", "broken", "bled", "defective", "damaged", "disappointed","bled into each other",
    "button came off", "worst shoes ever"}
QUESTION_WORDS = {"what", "where", "when", "who", "why", "how", "which"}


quality_complain_words = ["bled", "came off", "broke", "defective",
                     "damaged", "poor quality", "worst"]

size_complain_words = ["which size", "what size", "size",
                  "too small", "too big", "too tight", "too loose"]


def read_review(state: ReviewState) -> ReviewState:

    text = state["text"]
    
    words = set(re.findall(r"[a-z]+", text.lower()))
    if words & ABUSIVE_LINK_WORDS:
        kind = "abusiveORLink"
    elif words & COMPLAINT_WORDS:
        kind = "complaint"
        if any(word in text.lower() for word in quality_complain_words):
            state['issue_type'] = 'quality_defect'
        elif any(word in text.lower() for word in size_complain_words):
            state['issue_type'] = 'size_fit'
        else:
            state['issue_type'] = 'other'
                  
    elif words & QUESTION_WORDS:
        kind = "question"
    else:
        kind = "praise"

    state['text'] = text
    state['kind'] = kind
    return state



print(read_review({"text": "This product is the broken."}))
