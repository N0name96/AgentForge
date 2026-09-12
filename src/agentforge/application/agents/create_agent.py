from agentforge.domain.agents.agent import Agent
from agentforge.domain.agents.repository import AgentRepository


class CreateAgentCommand:
    def __init__(self, agent_repository: AgentRepository):
        self.agent_repository = agent_repository

    def execute(self, anget_id: str, name: str, description: str) -> Agent:
        agent = Agent(id=anget_id, name=name, description=description)
        self.agent_repository.save(agent)
        return agent