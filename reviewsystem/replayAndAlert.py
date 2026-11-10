from reviewsystem.ReviewState import ReviewState

def replay_and_alert(state: ReviewState) -> ReviewState:
    state['reply'] = "Goes live with a reply; alert sent"
    return state