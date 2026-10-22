import sqlite3
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def connect_to_db(db_file="database.db"):
    # Connect to (or create) a database file
    connection = sqlite3.connect(db_file)
    # we need to have this line because when db returns a raw of table it will be key:value that key is column name and value is actual value.
    # example [{"id":1,"name":"wc_0"},...], without following line it will be [[1,"wc_0"],...]
    connection.row_factory = sqlite3.Row

    # Create a cursor
    # A cursor is an object that lets your program talk to the database by:
    # Sending SQL commands
    # Receiving query results
    # Iterating over rows returned by a query
    # Think of it as a remote control or pointer to the database.
    cursor = connection.cursor()

    logging.info("Connected to SQLite")

    return connection, cursor

def close_connection(connection):

    # Always close when done
    connection.close()
    logging.info("Connection to closed!")
