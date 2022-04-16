from openpyxl import load_workbook
import numpy as np
import mysql.connector

# from mysql.....................
db = mysql.connector.connect(user='root', password='1234',
                             host='127.0.0.1', database='new_database')
cur = db.cursor()

#  load excel file................
wb = load_workbook('Data form mySQL.xlsx')

# show data
ws = wb['mysql_data']
m = []
for a in ws.values:
    m.append(a)
print(np.array(m[1:]))

# add data to mysql............
data = m[1:]
stmt = "INSERT INTO customer (ID, Name, age, address) VALUES (%s, %s, %s, %s)"
cur.executemany(stmt, data)
db.commit()
db.close()