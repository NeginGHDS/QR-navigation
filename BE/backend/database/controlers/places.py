from typing import List, Optional
from backend.database.models import Place
from backend.database.DAOs.places_dao import get_all_places, insert_place, get_place_by_id




def get_all_places_controller() -> List[Place]:
    return get_all_places()

def get_place_by_id_controller(place_id: str) -> Optional[Place]:
    return get_place_by_id(place_id)

def insert_place_controller():
    # for i in range(5):
    #     p = Place(name=f"wc_{i}", description=f"here you can pee_{i}", place_id=f"id_{i}")
    #     insert_place(p)

    # p = Place(name=f"Entrance", description=f"here is main entry", place_id=f"id_0", section="Entrance")
    # insert_place(p)
    #
    # p = Place(name=f"Book Shop", description=f"Here you can find interesting books", place_id=f"id_1", section="Section1")
    # insert_place(p)
    #
    # p = Place(name=f"Print", description=f"Here you can print your documents", place_id=f"id_2", section="Section1")
    # insert_place(p)
    #
    #
    # p = Place(name=f"Market", description=f"Here you can buy whatever you want for your house", place_id=f"id_3", section="Section2")
    # insert_place(p)
    #
    # p = Place(name=f"Restaurant", description=f"Here you can have your lunch and dinner", place_id=f"id_4", section="Section2")
    # insert_place(p)
    #
    # p = Place(name=f"Toilet", description=f"Here you can rest", place_id=f"id_5", section="Section3")
    # insert_place(p)
    #
    # p = Place(name=f"Exit", description=f"Here you can exit", place_id=f"id_6", section="Exit")
    # insert_place(p)

    places = [
        # ==========================================
        # FLOOR 0: Ground Floor
        # ==========================================
        {
            "name": "Entrance",
            "description": "Main building entry point located at the south plaza. Look for the large glass revolving doors. This is your starting point if arriving from the street.",
            "floor": 0, "section": "Lobby", "place_id": "id_0", "visited": 0, "last_place": 0
        },
        {
            "name": "Security Desk",
            "description": "Mandatory check-in counter located straight ahead from the main entrance. Features a curved wooden desk where all visitors must present ID and obtain a visitor badge.",
            "floor": 0, "section": "Lobby", "place_id": "id_1", "visited": 0, "last_place": 0
        },
        {
            "name": "Info Desk",
            "description": "General help desk located just past security in the center of the main atrium. Look for the large blue overhead 'Information' sign. Staff here can provide building maps.",
            "floor": 0, "section": "Lobby", "place_id": "id_2", "visited": 0, "last_place": 0
        },
        {
            "name": "Waiting Lounge",
            "description": "Spacious public seating area on the east side of the lobby. It features comfortable leather sofas, low tables, and mobile charging stations.",
            "floor": 0, "section": "Lobby", "place_id": "id_3", "visited": 0, "last_place": 0
        },
        {
            "name": "Cafe",
            "description": "The 'Atrium Cafe' located in the west wing of the ground floor. It serves coffee and pastries. You can easily spot it by the green awning and the smell of roasted coffee.",
            "floor": 0, "section": "Amenities", "place_id": "id_4", "visited": 0, "last_place": 0
        },
        {
            "name": "Gift Shop",
            "description": "A small retail store directly adjacent to the cafe, selling books, souvenirs, and snacks. Look for the brightly lit glass display windows.",
            "floor": 0, "section": "Amenities", "place_id": "id_5", "visited": 0, "last_place": 0
        },
        {
            "name": "Restroom G",
            "description": "Ground floor public restrooms located down the corridor to the right of the waiting lounge. Look for the standard gender-neutral navigational signage on the wall.",
            "floor": 0, "section": "Amenities", "place_id": "id_6", "visited": 0, "last_place": 0
        },
        {
            "name": "Mail Room",
            "description": "Shipping and receiving center located in the rear service corridor behind the Info Desk. The door is solid metal and marked 'Staff/Deliveries Only'.",
            "floor": 0, "section": "Services", "place_id": "id_7", "visited": 0, "last_place": 0
        },
        {
            "name": "Elevator G",
            "description": "Main ground floor elevator bank located in the central core of the building. It features four polished steel elevator doors and digital floor indicators.",
            "floor": 0, "section": "Transport", "place_id": "id_8", "visited": 0, "last_place": 0
        },
        {
            "name": "Stairs G",
            "description": "Main structural stairwell located right next to the elevator bank. Look for the heavy red fire doors marked 'Stairs - Access to All Floors'.",
            "floor": 0, "section": "Transport", "place_id": "id_9", "visited": 0, "last_place": 0
        },
    # ==========================================
        # FLOOR 2: Executive & Admin
        # ==========================================
        {
            "name": "Elevator F2",
            "description": "Second floor elevator lobby. Exiting here, you will step onto thick carpeted floors and see wood-paneled walls indicating the executive suite.",
            "floor": 2, "section": "Transport", "place_id": "id_20", "visited": 0, "last_place": 0
        },
        {
            "name": "Stairs F2",
            "description": "Second floor stairwell landing, located to the immediate right of the elevator bank behind the heavy wooden fire doors.",
            "floor": 2, "section": "Transport", "place_id": "id_21", "visited": 0, "last_place": 0
        },
        {
            "name": "Reception F2",
            "description": "Executive reception desk directly facing the elevators. Staffed by an administrative assistant to check in VIP guests and direct executive traffic.",
            "floor": 2, "section": "Admin", "place_id": "id_22", "visited": 0, "last_place": 0
        },
        {
            "name": "Director's Office",
            "description": "The primary executive suite for the building director, located at the far end of the north corridor. Distinctive double oak doors and a small waiting foyer mark the entrance.",
            "floor": 2, "section": "Admin", "place_id": "id_23", "visited": 0, "last_place": 0
        },
        {
            "name": "HR Department",
            "description": "Human Resources wing. Take the corridor to the left of the reception desk; the department is enclosed by frosted glass walls for privacy.",
            "floor": 2, "section": "Admin", "place_id": "id_24", "visited": 0, "last_place": 0
        },
        {
            "name": "Main Conference",
            "description": "Large boardroom used for major meetings and presentations. Located immediately behind the reception desk through the large glass double doors.",
            "floor": 2, "section": "Admin", "place_id": "id_25", "visited": 0, "last_place": 0
        },
        {
            "name": "Meeting Room A",
            "description": "Smaller breakout room located inside the Main Conference suite. Enter the boardroom area and it is the first door on the left side.",
            "floor": 2, "section": "Admin", "place_id": "id_26", "visited": 0, "last_place": 0
        },
        {
            "name": "Meeting Room B",
            "description": "Medium-sized meeting room located inside the Main Conference suite. Enter the boardroom area and it is the first door on the right side.",
            "floor": 2, "section": "Admin", "place_id": "id_27", "visited": 0, "last_place": 0
        },
        {
            "name": "Legal Department",
            "description": "Legal and compliance office located down the hall past the HR department. The entrance requires keycard access and features a small bronze plaque.",
            "floor": 2, "section": "Admin", "place_id": "id_28", "visited": 0, "last_place": 0
        },
        {
            "name": "Restroom F2",
            "description": "Executive restrooms located down the short, carpeted hallway to the right of the reception desk.",
            "floor": 2, "section": "Amenities", "place_id": "id_29", "visited": 0, "last_place": 0
        }
    ]

    for x in places:
        insert_place(Place(**x))