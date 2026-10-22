import qrcode
import json
from pydantic import BaseModel

class Place(BaseModel):
    id: int = -1
    name: str
    description: str
    floor: int = 0
    section: str = ""
    visited: int = 0
    last_place: int = 0
    place_id: str


def generate_qr_code(data):
    qr_data = json.dumps(data)
    try:
        Place.model_validate_json(qr_data)

        img = qrcode.make(qr_data)
        img.save(f"{data['name']}_{data['place_id']}.png")
    except Exception as e:
        print(e)
# _data = {
#     "id": 5,
#     "name": "Restaurant",
#     "description": "Here you can have your lunch and dinner",
#     "distance": 0,
#     "floor": 0,
#     "last_place": 0,
#     "llm_output": False,
#     "place_id": "id_4",
#     "section": "Section2",
#     "visited": 0
# }
_data = {   "id":0,
            "name": "Entrance",
            "description": "Main building entry point located at the south plaza. Look for the large glass revolving doors. This is your starting point if arriving from the street.",
            "floor": 0,
            "section": "Lobby",
            "place_id": "id_0",
            "visited": 0,
            "last_place": 0
        }
generate_qr_code(data = _data)

# print(_data)
# print(type(_data))
# print(json.dumps(_data))
# print(type(json.dumps(_data)))