from langchain_core.messages import HumanMessage, SystemMessage
from reviewsystem.ReviewState import ReviewState
from reviewsystem.config import llm as model_with_tools

def answer_agent(state: ReviewState) -> ReviewState:
    system_message = SystemMessage(
        content=(
            "You are a helpful kids' clothing customer support agent. "
            "Use the size chart, care instructions, and stock tools when needed. "
            "Use tool results for factual answers, especially stock. "
            "If you need a product SKU or size to answer, ask the customer."
        )
    )

    response = model_with_tools.invoke(
        [system_message, HumanMessage(content=state["text"])]
    )

    # The response may contain a tool call or a final answer.
    state["messages"] = [response]
    return state

print("Answer: ===", answer_agent({"text": "What size chart is available for kids' clothing?"})["messages"][-1].content)