from database import *
from datetime import datetime




mysql_extract_member = ('''SELECT * FROM member''')



def select_tabel(query,mysql_db):
    cursor = mysql_db.cursor()
    cursor.exucate(query)
    result = cursor.fetchall()

    return(result)

def inser_tabel(query,mysql_db2):
    cursor2 = mysql_db2.cursor()
    cursor2.execute(query)
    query.commit()

def check_dim_member_etl(data):
    if len(data) == 0:
        print("masuk pak eko")
    else:
        print("yayay")
