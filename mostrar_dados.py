import sqlite3
import time
import datetime

connection = sqlite3.connect("DinalvaCabelereira.db")
c = connection.cursor()

c.execute("SELECT * FROM dados")

for linha in c.fetchall():
    print(linha)
    time.sleep(1)
    