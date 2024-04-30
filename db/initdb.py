import os
import sqlite3

SQLITE_DB = os.environ['SQLITE_DB']

query = "CREATE TABLE GamePlayers(" + \
        "USERNAME varchar(12) primary key," + \
        "EMAIL varchar(24) not null," + \
        "WINS integer," + \
        "TOTAL_PLAYED integer," + \
        "SECRET_ID varchar(12)" + \
        ");"


def init_db():
    conn = None
    cur = None
    try:
        conn = sqlite3.connect(SQLITE_DB)
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
    init_db()
