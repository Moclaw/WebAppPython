import sqlite3

conn = sqlite3.connect('WebAppPython/account.db')

cur = conn.cursor()

def add_data(arg):
    email = arg['email']
    name = arg['lastName'] + ' ' + arg['firstName']
    password = arg['password1']

    conn.execute(f"INSERT INTO user VALUES ('{name}','{password}','{email}'')")

def delete_data():
    conn.execute("DELETE FROM user WHERE name = 'Do HUY'")

delete_data()

conn.commit()
conn.close()
