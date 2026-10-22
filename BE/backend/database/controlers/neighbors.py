from backend.database.DAOs.neighbos_dao import insert_neighbor, get_all_neighbors
from backend.database.models import Neighbor


def get_all_neighbors_controller():
    return get_all_neighbors()


def insert_neighbor_controller():
    # # n0 = Neighbor(first_node="id_0", second_node="id_1", distance=1)
    # # n1 = Neighbor(first_node="id_0", second_node="id_2", distance=2)
    # # n2 = Neighbor(first_node="id_1", second_node="id_2", distance=2)
    # # n3 = Neighbor(first_node="id_1", second_node="id_4", distance=3)
    # # n4 = Neighbor(first_node="id_2", second_node="id_3", distance=2)
    # # n5 = Neighbor(first_node="id_3", second_node="id_4", distance=1)
    # #
    # # insert_neighbor(n0)
    # # insert_neighbor(n1)
    # # insert_neighbor(n2)
    # # insert_neighbor(n3)
    # # insert_neighbor(n4)
    # # insert_neighbor(n5)
    #
    # n1 = Neighbor(first_node="id_0", second_node="id_1", distance=1)
    # n2 = Neighbor(first_node="id_0", second_node="id_6", distance=2)
    # n3 = Neighbor(first_node="id_1", second_node="id_4", distance=1)
    # n4 = Neighbor(first_node="id_1", second_node="id_5", distance=1)
    # n5 = Neighbor(first_node="id_1", second_node="id_6", distance=4)
    # n6 = Neighbor(first_node="id_4", second_node="id_5", distance=3)
    # n7 = Neighbor(first_node="id_4", second_node="id_2", distance=1)
    # n8 = Neighbor(first_node="id_5", second_node="id_2", distance=2)
    # n9 = Neighbor(first_node="id_2", second_node="id_3", distance=3)
    # n10 = Neighbor(first_node="id_5", second_node="id_3", distance=2)
    # n11 = Neighbor(first_node="id_3", second_node="id_6", distance=1)
    # n12 = Neighbor(first_node="id_5", second_node="id_6", distance=3)
    #
    #
    # insert_neighbor(n1)
    # insert_neighbor(n2)
    # insert_neighbor(n3)
    # insert_neighbor(n4)
    # insert_neighbor(n5)
    # insert_neighbor(n6)
    # insert_neighbor(n7)
    # insert_neighbor(n8)
    # insert_neighbor(n9)
    # insert_neighbor(n10)
    # insert_neighbor(n11)
    # insert_neighbor(n12)
    ns = [
        # ==========================================
        # Floor 0 Connections
        # ==========================================
        {"first_node": "id_0", "second_node": "id_1", "distance": 2, "bidirectional": 1},
        {"first_node": "id_1", "second_node": "id_2", "distance": 3, "bidirectional": 1},
        {"first_node": "id_2", "second_node": "id_3", "distance": 4, "bidirectional": 1},
        {"first_node": "id_2", "second_node": "id_4", "distance": 6, "bidirectional": 1},
        {"first_node": "id_4", "second_node": "id_5", "distance": 2, "bidirectional": 1},
        {"first_node": "id_3", "second_node": "id_6", "distance": 3, "bidirectional": 1},


        {"first_node": "id_2", "second_node": "id_7", "distance": 8, "bidirectional": 1},
        {"first_node": "id_2", "second_node": "id_8", "distance": 5, "bidirectional": 1},
        {"first_node": "id_1", "second_node": "id_9", "distance": 6, "bidirectional": 1},

        # ==========================================
        # Floor 1 Connections
        # ==========================================
        {"first_node": "id_10", "second_node": "id_15", "distance": 4, "bidirectional": 1},
        {"first_node": "id_11", "second_node": "id_15", "distance": 5, "bidirectional": 1},
        {"first_node": "id_15", "second_node": "id_12", "distance": 3, "bidirectional": 1},
        {"first_node": "id_12", "second_node": "id_13", "distance": 2, "bidirectional": 1},
        {"first_node": "id_12", "second_node": "id_14", "distance": 2, "bidirectional": 1},
        {"first_node": "id_15", "second_node": "id_16", "distance": 4, "bidirectional": 1},
        {"first_node": "id_15", "second_node": "id_17", "distance": 3, "bidirectional": 1},
        {"first_node": "id_16", "second_node": "id_19", "distance": 6, "bidirectional": 1},
        {"first_node": "id_19", "second_node": "id_18", "distance": 2, "bidirectional": 1},

        # ==========================================
        # Floor 2 Connections
        # ==========================================
        {"first_node": "id_20", "second_node": "id_22", "distance": 3, "bidirectional": 1},
        {"first_node": "id_21", "second_node": "id_22", "distance": 4, "bidirectional": 1},
        {"first_node": "id_22", "second_node": "id_23", "distance": 8, "bidirectional": 1},
        {"first_node": "id_22", "second_node": "id_24", "distance": 5, "bidirectional": 1},
        {"first_node": "id_22", "second_node": "id_25", "distance": 4, "bidirectional": 1},
        {"first_node": "id_25", "second_node": "id_26", "distance": 2, "bidirectional": 1},
        {"first_node": "id_25", "second_node": "id_27", "distance": 2, "bidirectional": 1},
        {"first_node": "id_24", "second_node": "id_28", "distance": 4, "bidirectional": 1},
        {"first_node": "id_22", "second_node": "id_29", "distance": 3, "bidirectional": 1},

        # ==========================================
        # Inter-Floor Connections
        # ==========================================
        {"first_node": "id_8", "second_node": "id_10", "distance": 10, "bidirectional": 1},
        {"first_node": "id_10", "second_node": "id_20", "distance": 10, "bidirectional": 1},
        {"first_node": "id_9", "second_node": "id_11", "distance": 15, "bidirectional": 1},
        {"first_node": "id_11", "second_node": "id_21", "distance": 15, "bidirectional": 1}
    ]
    for x in ns:
        insert_neighbor(Neighbor(**x))
