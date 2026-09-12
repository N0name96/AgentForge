from typing import Protocol

from agentforge.domain.agents.agent import Agent


class AgentRepository(Protocol):

    def save(self, agent: Agent) -> None:
        ...

    def get(self, agent_id: str) -> Agent | None:
        ...

    def get_all(self) -> list[Agent]:
        ...