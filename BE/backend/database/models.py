from typing import List

from pydantic import BaseModel


class Place(BaseModel):
    id: int = None
    name: str
    description: str
    floor: int = 0
    section: str = ""
    visited: int = 0
    last_place: int = 0
    place_id: str

class ShortestPathInfo(BaseModel):
    path: List[str]
    distance: int

class AgentPayload(BaseModel):
    shortest_paths: ShortestPathInfo
    traversed_places: List[Place] = []
    places_in_shortest_path: List[Place] = []
    current_place: Place
    destination: Place
    departure: Place


class Neighbor(BaseModel):
    id: int = None
    first_node: str
    second_node: str
    distance: int = 1
    bidirectional: int = 1

