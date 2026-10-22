import logging
from backend.database.connection import connect_to_db, close_connection


def create_places_table():
    conn = None
    try:
        conn, cursor = connect_to_db()
        query = """
            CREATE TABLE IF NOT EXISTS places (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                place_id TEXT NOT NULL UNIQUE,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                floor INTEGER,
                section TEXT,
                visited INTEGER DEFAULT 0,
                last_place INTEGER
            );
        """
        cursor.execute(query)
    except Exception as e:
        logging.error(e)
    finally:
        if conn is not None:
            close_connection(conn)


def create_neighbors_table():
    conn = None
    try:
        conn, cursor = connect_to_db()
        query = """
            CREATE TABLE IF NOT EXISTS neighbors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_node TEXT NOT NULL,
                second_node TEXT NOT NULL,
                distance INTEGER DEFAULT 1,
                bidirectional INTEGER DEFAULT 1
            );
        """
        cursor.execute(query)
    except Exception as e:
        logging.error(e)
    finally:
        if conn is not None:
            close_connection(conn)

