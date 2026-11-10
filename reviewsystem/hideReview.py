from reviewsystem.ReviewState import ReviewState

def hide_review(state: ReviewState) -> ReviewState:
    state['status'] = "abusiveORLink : HeldBack"
    return state