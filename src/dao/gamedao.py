import os
import sqlite3
import uuid

SQLITE_DB = os.environ['SQLITE_DB']


def get_player_info_by_secret_id(secret_id):
    conn = None
    cur = None
    try:
        query = "SELECT USERNAME, WINS, TOTAL_PLAYED FROM GamePlayers WHERE SECRET_ID = ?;"
        conn = sqlite3.connect(SQLITE_DB)
        cur = conn.cursor()
        cur.execute(query, (secret_id,))
        data = cur.fetchone()
        return {
            "user": data[0],
            "wins": data[1],
            "total": data[2]
        }
    except Exception as e:
        print(e)
        return None
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()


def get_scoreboard():
    conn = None
    cur = None
    try:
        query = "SELECT USERNAME, WINS FROM GamePlayers ORDER BY WINS DESC;"
        conn = sqlite3.connect(SQLITE_DB)
        cur = conn.cursor()
        cur.execute(query)
        return cur.fetchall()
    except Exception as e:
        print(e)
        return []
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()


def add_player(username, email):
    conn = None
    cur = None
    try:
        secret_id = str(uuid.uuid4())[:8]
        query = "INSERT INTO GamePlayers(USERNAME, EMAIL, WINS, TOTAL_PLAYED, SECRET_ID)" + \
                "VALUES(?, ?, 0, 0, '" + secret_id + "');"
        conn = sqlite3.connect(SQLITE_DB)
        cur = conn.cursor()
        cur.execute(query, (username, email))
        conn.commit()
        return secret_id
    except Exception as e:
        print(e)
        return None
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()


def add_result(secret_id, result):
    conn = None
    cur = None
    try:
        query = "UPDATE GamePlayers SET TOTAL_PLAYED = TOTAL_PLAYED + 1 "
        query += ', WINS = WINS + 1 ' if result else ''
        query += "WHERE SECRET_ID = ?;"
        conn = sqlite3.connect(SQLITE_DB)
        cur = conn.cursor()
        cur.execute(query, (secret_id,))
        conn.commit()
        return get_player_info_by_secret_id(secret_id)
    except Exception as e:
        print(e)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
