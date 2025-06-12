from agno.agent import Agent, RunResponse
from agno.models.deepseek import DeepSeek

api_key = "sk-087c2d0e8af14432bdb0e7d06a15ac78"
agent = Agent(model=DeepSeek(id = "deepseek-reasoner"), markdown=True)

agent.print_response("Share a 2 sentence horror story.")

