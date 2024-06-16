import os
import sqlite3


queries = [
    "CREATE TABLE GamePlayers(" +
    "USERNAME varchar(12) primary key," +
    "EMAIL varchar(24) not null," +
    "SECRET_ID varchar(12)" +
    ");",
    "--pragma foreign_keys = ON;",
    "CREATE TABLE PlayerGuesses(" +
    "ID integer primary key autoincrement," +
    "USERNAME varchar(12) not null," +
    "GUESS integer not null," +
    "WIN integer," +
    "foreign key (USERNAME)" +
    "references GamePlayers(USERNAME)" +
    ");"
]


def init_db(game_db):
    cur = None
    conn = None
    for query in queries:
        try:
            conn = sqlite3.connect(game_db)
            cur = conn.cursor()
            cur.execute(query)
            conn.commit()
        except Exception as e:
            print(e)
            return 0
        finally:
            if cur is not None:
                cur.close()
            if cur is not None:
                conn.close()


if __name__ == '__main__':
    import sys
    print(f'Filename provided was: {sys.argv[1]}')
    init_db(sys.argv[1])
