from typing import List

from fastapi import APIRouter
from backend.database.controlers.places import get_all_places_controller

# before each router we have /places
place_router = APIRouter(prefix="/places", tags=["Place"])

# /places
@place_router.get("")
def fetch_places():
    return get_all_places_controller()
