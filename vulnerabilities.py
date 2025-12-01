import sqlite3
import os

def get_user(username):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

def delete_file(filename):
    os.system(f"rm -rf {filename}")