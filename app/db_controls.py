import sqlite3
from flask import g
from app import app

def add_new_article(title, intro, text):
    # request = 

    msg = ""
    try:
        with sqlite3.connect("app.db") as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO article (title, intro, text) VALUES (?, ?, ?)", (title, intro, text))
            connection.commit()
            msg="Sucssesfuly added"


    except Exception as e:
        connection.rollback()
        msg=str(e)
        

    finally:
        connection.close()
        return msg

def add_updates(title, intro, text, id=None):
    # request = 

    msg = ""
    try:
        with sqlite3.connect("app.db") as connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE article SET title = ?, intro = ?, text = ? WHERE id=?", (title, intro, text, id))
            connection.commit()
            msg="Sucssesfuly added"


    except Exception as e:
        connection.rollback()
        msg=str(e)
        

    finally:
        connection.close()
        return msg







def get_db(id=None):
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect("app.db")
        cursor = db.cursor()
        cursor.execute(f"select * from article")
        all_data = cursor.fetchall()
        all_data = [list(i) for i in all_data]
        if id is not None:
            all_data = all_data[id-1]
            return all_data
        return all_data



@app.teardown_appcontext
def close_connection(ex):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()
        