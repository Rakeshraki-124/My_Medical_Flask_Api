import sqlite3 
from DB.readOpration import dict_factory


def user_auth(email, password):
    conn = sqlite3.connect("my_medicalshop.db")
    conn.row_factory = dict_factory

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Users WHERE email=? AND password=?",(email, password))
    user =cursor.fetchone()
        
    conn.close()
    return user