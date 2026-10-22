from typing import List

from backend.database.models import Neighbor
from backend.database.connection import close_connection, connect_to_db

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def get_all_neighbors() -> List[Neighbor]:
    connection = None
    try:
        connection, cursor = connect_to_db()
        query = """
            SELECT *
            FROM neighbors
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        result = [dict(row) for row in rows]
        print(type(result))
        print(result)

        return rows
    except Exception as e:
        logging.exception(e)

    finally:
        if connection:
            close_connection(connection)



def insert_neighbor(neighbor: Neighbor):
    connection = None
    try:
        connection, cursor = connect_to_db()
        # since the id is auto increment we can omit it, is it incremented automatically without issue.
        query = ("INSERT INTO neighbors ( first_node, second_node, distance, bidirectional ) VALUES (?, ?, ?, ?)")
        cursor.execute(query, (neighbor.first_node, neighbor.second_node, neighbor.distance, neighbor.bidirectional))
        # SQLite does NOT save inserts without a commit.
        connection.commit()  # REQUIRED
    except Exception as e:
        logging.exception(e)
    finally:
        if connection:
            close_connection(connection)

def get_distance_between_neighbors(first_place_id:str, second_place_id:str):
    connection = None
    try:
        connection, cursor = connect_to_db()
        # since the id is auto increment we can omit it, is it incremented automatically without issue.
        query = ("SELECT FROM neighbors ( first_node, second_node, distance, bidirectional ) VALUES (?, ?)")
        cursor.execute(query, (first_place_id, second_place_id))
        # SQLite does NOT save inserts without a commit.
        connection.commit()  # REQUIRED
    except Exception as e:
        logging.exception(e)
    finally:
        if connection:
            close_connection(connection)
