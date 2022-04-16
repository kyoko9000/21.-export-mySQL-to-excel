import mysql.connector
from openpyxl import Workbook

db = mysql.connector.connect(user='root', password='1234',
                             host='127.0.0.1', database='new_database')
cur = db.cursor()

try:
    cur.execute("SELECT * FROM customer;")
    result = cur.fetchall()

    table_name = [i[0] for i in cur.description]
    print(table_name)
    print(result)

    wb = Workbook()
    ws = wb.active
    ws.title = "mysql_data"
    ws.append(table_name)
    for row in result:
        ws.append(row)
    wb.save("Data form mySQL.xlsx")
    db.commit()
except:
    print("some thing wrong")
db.close()