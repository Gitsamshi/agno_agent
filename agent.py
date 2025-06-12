from agno.agent import Agent, RunResponse
from agno.models.deepseek import DeepSeek

agent = Agent(model=DeepSeek(id = "deepseek-reasoner"), markdown=True)

agent.print_response("Share a 2 sentence horror story.")

