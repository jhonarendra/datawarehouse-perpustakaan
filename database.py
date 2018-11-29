import mysql.connector
from mysql.connector import Error

try:
    mysql_db = mysql.connector.connect(
        host = "localhost",
        database="perpustakaan",
        user = "root",
        password = "",

    )
    mysql_db2 = mysql.connector.connect(
        host = "localhost",
        database="warehouse",
        user = "root",
        password = ""

    )
    if mysql_db.is_connected() and mysql_db2.is_connected():
        print("Connected database MySQL !!!")
        print("")

except Error as e:
    print(e)
# finally:
#     mysql_db.close()
#     mysql_db2.close()


