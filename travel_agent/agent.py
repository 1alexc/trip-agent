from google.adk.agents import Agent

root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
    instruction=(
        "You are a helpful travel assistant. "
        "You can help with general travel advice based on your knowledge."
    ),
)
