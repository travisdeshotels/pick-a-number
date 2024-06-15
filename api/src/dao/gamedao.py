import os
import sqlite3
import uuid

SQLITE_DB = os.environ['SQLITE_DB']


def get_player_info_by_secret_id(secret_id):
    username_query = "SELECT USERNAME FROM GamePlayers WHERE SECRET_ID = ?"
    total_played_query = "SELECT COUNT(*) FROM PlayerGuesses G INNER JOIN GamePlayers P ON G.USERNAME = P.USERNAME" \
                         " WHERE P.SECRET_ID=?"
    total_wins_query = "SELECT COUNT(*) FROM PlayerGuesses G INNER JOIN GamePlayers P ON G.USERNAME = P.USERNAME" \
                       " WHERE G.WIN=1 AND P.SECRET_ID=?"
    most_used_guess_query = "SELECT GUESS FROM (SELECT G.guess, COUNT(G.guess) as `num`" + \
                            " FROM PlayerGuesses G INNER JOIN GamePlayers P ON G.USERNAME = P.USERNAME" + \
                            " WHERE P.SECRET_ID = ?" + \
                            " GROUP BY G.GUESS" + \
                            " ORDER BY `num` DESC" + \
                            " LIMIT 1)"

    conn = None
    cur = None
    try:
        query = "SELECT ( " + total_played_query + "), (" + total_wins_query + "), " + \
                "(" + most_used_guess_query + "), (" + username_query + ");"
        conn = sqlite3.connect(SQLITE_DB)
        cur = conn.cursor()
        cur.execute(query, (secret_id, secret_id, secret_id, secret_id))
        data = cur.fetchone()
        return {
            'username': data[3],
            'stats': {
                'total': data[0],
                'wins': data[1],
                'mostGuessed': data[2]
            }
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
        query = "SELECT USERNAME, COUNT(WIN) AS `WINS` FROM PlayerGuesses WHERE WIN = 1 " + \
                "GROUP BY WIN, USERNAME ORDER BY `WINS` DESC;"
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
        query = "INSERT INTO GamePlayers(USERNAME, EMAIL, SECRET_ID)" + \
                "VALUES(?, ?, '" + secret_id + "');"
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


def add_play_result(secret_id, guess, result):
    conn = None
    cur = None
    try:
        query = "INSERT INTO PlayerGuesses(USERNAME, GUESS, WIN) " + \
                "VALUES(" + \
                "(SELECT USERNAME FROM GamePlayers WHERE SECRET_ID = ?)" + \
                ", ?" + \
                ", ?);"
        conn = sqlite3.connect(SQLITE_DB)
        cur = conn.cursor()
        cur.execute(query, (secret_id, guess, 1 if result else 0))
        conn.commit()
        return get_player_info_by_secret_id(secret_id)
    except Exception as e:
        print(e)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
