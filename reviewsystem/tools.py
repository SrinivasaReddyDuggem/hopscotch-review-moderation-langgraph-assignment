
from langchain_core.tools import tool
from langgraph.graph import StateGraph, START
from langgraph.prebuilt import ToolNode, tools_condition

from reviewsystem.ReviewState import ReviewState
from reviewsystem.config import llm  # Adjust this import to your project


@tool
def get_size_chart(category: str) -> str:
    """Return the size chart for a kids' clothing category."""
    # Example data; replace with your assignment's actual size chart.
    return (
        f"Size chart for {category}: "
        "2-3Y: 92-98 cm, 3-4Y: 98-104 cm, "
        "4-5Y: 104-110 cm, 5-6Y: 110-116 cm."
    )


@tool
def get_care_instructions(product_category: str) -> str:
    """Return care and washing instructions for a product category."""
    # Example data; replace with your assignment's actual instructions.
    return (
        f"Care instructions for {product_category}: "
        "Machine wash cold with similar colors. Do not bleach. "
        "Air dry when possible."
    )


@tool
def check_stock(sku: str, size: str) -> str:
    """Check whether a product is in stock for the requested size."""
    # Example inventory; replace with a real inventory lookup.
    inventory = {
        ("HS-201", "4-5Y"): 8,
        ("HS-201", "5-6Y"): 0,
    }

    quantity = inventory.get((sku, size), 0)
    if quantity > 0:
        return f"{sku}, size {size}: in stock ({quantity} available)."

    return f"{sku}, size {size}: currently out of stock."


tools = [get_size_chart, get_care_instructions, check_stock]
model_with_tools = llm.bind_tools(tools)