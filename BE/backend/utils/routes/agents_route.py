from typing import List
from backend.database.models import AgentPayload
from fastapi import APIRouter
from backend.agent.graph import CustomAgent
from backend.database.controlers.places import get_all_places_controller

# before each router we have /places
agent_router = APIRouter(prefix="/agent", tags=["Agent"])


@agent_router.post("/call")
def call_agent(payload:AgentPayload):
    # print("here is payload", payload)
    graph = CustomAgent()
    print("payload", dict(payload))
    response = graph.invoke_graph(dict(payload))
    return response

    # return get_all_places_controller()