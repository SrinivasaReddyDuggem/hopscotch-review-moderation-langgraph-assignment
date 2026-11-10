
from langgraph.graph import StateGraph, START, END
from reviewsystem.tools import tools
from langgraph.prebuilt import ToolNode, tools_condition
from reviewsystem.ReviewState import ReviewState
from reviewsystem.countComplaints import count_complaints
from reviewsystem.hideReview import hide_review
from reviewsystem.replayAndAlert import replay_and_alert
from reviewsystem.readReview import read_review
from reviewsystem.triage import triage  
from reviewsystem.cleanReview import clean_review
from reviewsystem.getReturnRate import get_return_rate
from reviewsystem.vendorRecord import vendor_record
from reviewsystem.publishReview import publish_review
from reviewsystem.answerAgent import answer_agent


graph = StateGraph(ReviewState)
graph.add_node("clean_review", clean_review)
graph.add_node("read_review", read_review)
graph.add_node("answer_agent", answer_agent)
graph.add_node("tools", ToolNode(tools))
graph.add_node("hide_review", hide_review)
graph.add_node("count_complaints", count_complaints)
graph.add_node("get_return_rate", get_return_rate)
graph.add_node("vendor_record", vendor_record)
graph.add_node("replay_and_alert", replay_and_alert)
graph.add_node("publish_review", publish_review)

graph.add_edge(START, "clean_review")
graph.add_edge("clean_review", "read_review")
graph.add_conditional_edges("read_review", triage)


# Abusive Flow
graph.add_edge("hide_review", END)

# Question Flow
graph.add_conditional_edges("answer_agent", tools_condition)
graph.add_edge("tools", "answer_agent")
graph.add_edge("answer_agent", "publish_review")

# Complain Flow
graph.add_edge("count_complaints", "replay_and_alert")
graph.add_edge("get_return_rate", "replay_and_alert")
graph.add_edge("vendor_record", "replay_and_alert")
graph.add_edge("replay_and_alert", "publish_review")

# Praise Flow
graph.add_edge("publish_review", END)
graph_flow = graph.compile()

input_state_praise = {
    "review": {
        "review_id": "R-1",
        "sku": "HS-118",
        "rating": 5,
        "text": "Lovely soft fabric, my son wears it every day.",
    }
}

final_state_Praise = graph_flow.invoke(input_state_praise)
print("Final Result With Praise == ", final_state_Praise)

input_state_abuse = {
    "review": {
        "review_id": "R-1",
        "sku": "HS-118",
        "rating": 5,
        "text": "Worst shoes ever, you idiots. Call me on 9820011223",
    }
}

final_state_abuse = graph_flow.invoke(input_state_abuse)
print("Final Result With Abuse == ", final_state_abuse)

input_state_complaint = {
    "review": {
        "review_id": "R-1",
        "sku": "HS-201",
        "rating": 5,
        "text": "damaged Goods.",
    }
}

final_state_complaint = graph_flow.invoke(input_state_complaint)
print("Final Result With Complaint == ", final_state_complaint)

input_state_question = {
    "review": {
        "review_id": "R-1",
        "sku": "HS-201",
        "rating": 5,
        "text": "What size chart is available for kids' clothing?",
    }
}

final_state_question = graph_flow.invoke(input_state_question)
print("Final Result With Question == ", final_state_question)




