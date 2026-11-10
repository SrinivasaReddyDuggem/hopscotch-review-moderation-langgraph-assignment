
from reviewsystem.ReviewState import ReviewState

def publish_review(state: ReviewState) -> ReviewState:

    print("Publish Running")

    if state['kind'] == 'praise':
        state['status'] = "GoLive : Praise"
    elif state['kind'] == 'complaint':
        state['status'] = "Goes live with a reply; alert sent :- Complaint"
    elif state['kind'] == 'abusiveORLink':
        state['status'] = "BackHeld :- Abusive or Link"
    elif state['kind'] == 'question':
        state['status'] = "Goes live with an answer :- Question"
        
        
    return state