from langgraph.graph import StateGraph, END
from langgraph_config import LANGSMITH_API_KEY
import os

# Define the state schema
class State(dict):
    pass

# Set LangSmith configuration
os.environ["LANGSMITH_API_KEY"] = LANGSMITH_API_KEY
os.environ["LANGSMITH_PROJECT"] = "my-langgraph-project"
os.environ["LANGSMITH_TAGS"] = "development"

# Node 1: Input processor
def input_node(state):
    user_input = state.get("input")
    return {"message": f"You said: {user_input}"}

# Node 2: Final response
def output_node(state):
    return {"output": state.get("message")}

# Build the graph
graph = StateGraph(State)
graph.add_node("input_processor", input_node)
graph.add_node("output", output_node)

# Define flow
graph.set_entry_point("input_processor")
graph.add_edge("input_processor", "output")
graph.add_edge("output", END)

# Compile the graph with LangSmith enabled (env handles API key)
builder = graph.compile(
    checkpointer=None  # Set to None or use SqliteSaver if needed
)