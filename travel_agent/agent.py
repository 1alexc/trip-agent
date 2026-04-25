from google.adk.agents import Agent
from datetime import datetime

def now() -> dict:
    """Returns the current date and time."""
    my_datetime = datetime.now()
    return {
        "status": "success",
        "current_time": str(my_datetime)
    }

root_agent = Agent(
    name="travel_basic",
    model="gemini-2.5-flash",
    instruction="You are a helpful travel assistant."
    + " You can help with general travel advice based on your knowledge.",
    tools=[now]
)