from agency_swarm import Agency
from agency_swarm.agents.browsing import BrowsingAgent
from agency_swarm.agents.genesis import GenesisCEO, AgentCreator
import os

from agency_swarm.agents.genesis import ToolCreator
from agency_swarm.agents.genesis import OpenAPICreator


class GenesisAgency(Agency):
    def __init__(self, **kwargs):

        if 'agency_chart' not in kwargs:
            agent_creator = AgentCreator()
            genesis_ceo = GenesisCEO()
            tool_creator = ToolCreator()
            openapi_creator = OpenAPICreator()
            browsing_agent = BrowsingAgent()
            kwargs['agency_chart'] = [
                genesis_ceo,
                [genesis_ceo, agent_creator],
                [agent_creator, browsing_agent],
                [agent_creator, openapi_creator],
            ]

        if 'shared_instructions' not in kwargs:
            kwargs['shared_instructions'] = "./manifesto.md"

        if 'shared_files' not in kwargs:
            readme_path = os.path.join(self.get_class_folder_path(), "./files")

            readme_path = os.path.abspath(readme_path)

            kwargs['shared_files'] = [readme_path]

        super().__init__(**kwargs)
