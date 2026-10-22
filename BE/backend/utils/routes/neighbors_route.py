from typing import List
from backend.utils.graph import Graph
from fastapi import APIRouter
from backend.database.controlers.neighbors import get_all_neighbors_controller
from backend.database.models import Neighbor
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# before each router we have /neighbors
neighbors_router = APIRouter(prefix="/neighbors", tags=["Neighbors"])

# /neighbors/all
@neighbors_router.get("/all")
def fetch_neighbors_router():
    return get_all_neighbors_controller()

# we use Query Parameters
# here is the link: https://fastapi.tiangolo.com/tutorial/query-params/?h=parameters
# curl "http://127.0.0.1:8000/neighbors/?current_node=id_2&target_node=id_4"
@neighbors_router.get("/")
def fetch_neighbors_router(current_node: str, target_node: str):
    logging.info(f"From {current_node} to {target_node}")
    all_info = get_all_neighbors_controller()
    graph = Graph(all_info)
    path = graph.dijkstra(current_node, target_node)
    logging.info(f"Dijkstra: {path}")
    return path

# https://fastapi.tiangolo.com/tutorial/query-params/?h=query#optional-parameters
@neighbors_router.get("/{current_place_id}/{target_place_id}")
def fetch_neighbors_router(current_place_id: str, target_place_id:str):
    logging.info(f"looking neighbors for {current_place_id}")
    all_info = get_all_neighbors_controller()
    graph = Graph(all_info)
    neighbors = graph.neighbors(current_place_id)
    all_available_paths = graph.find_all_simple_paths(current_place_id, target_place_id) # example output if we are in id_2 and target is id_3 : [{'path': ['id_2', 'id_0', 'id_1', 'id_4', 'id_3'], 'distance': 7}, {'path': ['id_2', 'id_1', 'id_4', 'id_3'], 'distance': 6}, {'path': ['id_2', 'id_3'], 'distance': 2}]
    logging.info(f"all_available_paths are: {all_available_paths}")
    result = list(map(lambda neighbor: neighbor[0], neighbors))
    logging.info(f"neighbors for {current_place_id}: {neighbors}")
    return all_available_paths

# https://fastapi.tiangolo.com/tutorial/query-params/?h=query#optional-parameters
@neighbors_router.get("/distance/{first_place_id}/{second_place_id}")
def get_distance_between_neighbors_router(first_place_id: str, second_place_id:str):
    all_info = get_all_neighbors_controller()
    graph = Graph(all_info)
    neighbors = graph.neighbors(first_place_id) # [(place_id, distance),...]
    target_neighbor = list(filter(lambda neighbor: neighbor[0] == second_place_id, neighbors)) # [(place_id, distance),...]
    distance = target_neighbor[0][1]
    return distance


