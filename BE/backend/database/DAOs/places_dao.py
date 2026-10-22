import sqlite3
from typing import List, Optional
from backend.database.models import Place
from backend.database.connection import close_connection, connect_to_db
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)



def get_place_by_id(the_place_id: str)->Optional[Place]:
    connection = None
    try:
        connection, cursor = connect_to_db()
        query = """
            SELECT *
            FROM places
            WHERE place_id = ?
        """
        cursor.execute(query, (the_place_id,))
        row = cursor.fetchone()
        if row is None:
            # the following line trows error if there is not such place with specified id!
            raise ValueError(f"Place with id '{the_place_id}' not found")

        return Place(**row)

    except Exception as ex:
        logging.error(ex)
    finally:
        if connection:
            connection.close()



def get_all_places() -> List[Place]:
    connection = None
    try:
        connection, cursor = connect_to_db()
        query = """
            SELECT *
            FROM places
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        result = [dict(row) for row in rows]
        # print(type(result))
        # print(result)

        return rows
    except Exception as e:
        logging.exception(e)

    finally:
        if connection:
            close_connection(connection)


def insert_place(place: Place):
    connection = None
    try:
        connection, cursor = connect_to_db()
        # since the id is auto increment we can omit it, is it incremented automatically without issue.
        query = ("INSERT INTO places ( name, description, floor, section, visited, last_place, place_id) VALUES (?, ?, ?, ?, ?, ?, ?)")
        cursor.execute(query, (place.name, place.description, place.floor, place.section, place.visited, place.last_place, place.place_id))
        # SQLite does NOT save inserts without a commit.
        connection.commit()  # REQUIRED
    except Exception as e:
        logging.exception(e)
    finally:
        if connection:
            close_connection(connection)

