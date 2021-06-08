import sqlite3

CREATE_TABLE_PWS = "CREATE TABLE IF NOT EXISTS pws (titel TEXT PRIMARY KEY, benutzername TEXT, pw TEXT);"
INSERT_PW = "INSERT INTO pws (titel, benutzername, pw) VALUES (?, ?, ?);"
GET_ALL_PW = "SELECT * FROM pws;"
DELETE_PW = "DELETE FROM pws WHERE titel = ?;"

#verbinde und erstelle tabelle
def connect():
    return sqlite3.connect("eintrag.db")

#erstelle passwort tabelle
def create_tables(connection):
    with connection:
        connection.execute(CREATE_TABLE_PWS)

def add_pw(connection, titel, benutzername, pw,):
    with connection:
        connection.execute(INSERT_PW, (titel, benutzername, pw))

def get_all_pw(connection):
    with connection:
        return connection.execute(GET_ALL_PW).fetchall()

def delete(connection, titel):
    with connection:
        return connection.execute(DELETE_PW, (titel,)).fetchall()