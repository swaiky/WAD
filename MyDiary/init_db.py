import sqlite3


class Database:
    def __init__(self):
        connection = sqlite3.connect('database.db')
        with open('schema.sql') as f:
            connection.executescript(f.read())
            connection.commit()
            connection.close()
