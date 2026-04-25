from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="travel_agent",
    model="gemini-2.5-flash",
    tools=[google_search],
    instruction="""You are a travel agent.
Your job is to help the user plan a trip.
You have access to a search engine.
If you don't know the answer, you can use the search engine.
When you are done, reply with "DONE".""",
)