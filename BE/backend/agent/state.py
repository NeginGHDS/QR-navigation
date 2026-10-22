from typing import List, Annotated, Dict, Any
from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages
from backend.database.models import Place
from pydantic import BaseModel, Field


class AgentState(BaseModel):
    all_messages: Annotated[List[AnyMessage], add_messages] = Field(default_factory=list, description="List of all messages")
    departure: Place = Field(..., description="Departure place")
    destination: Place = Field(..., description="Destination place")
    current_place: Place = Field(..., description="Destination place")
    summary: str = Field(default="", description="Agent summary")
    traversed_places: List[Place] = Field(default_factory=list, description="Places visited by agent")
    places_in_shortest_path: List[Place] = Field(default_factory=list, description="Places visited by agent")
    shortest_path: List[Dict[str, Any]] = Field(default_factory=list, description="Shortest path from departure to destination")
