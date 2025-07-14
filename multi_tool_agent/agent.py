from google.adk.agents import Agent

root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.0-flash",
    description="Agent to suggest meals and generate grocery lists based on preferences.",
    instruction="You help users plan meals based on their preferences and create efficient grocery lists, if there is no suggestion, provide an alternative meal plan that is similiar to the requsted meal"
)
