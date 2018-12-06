import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "db_klinik"
)
mydb2 = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "dwh_klinik"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM tb_pasien")
myresult = mycursor.fetchall()
mycursor2 = mydb2.cursor()

for x in myresult:
    etl = "INSERT INTO tb_dim_pasien (id_pasien_oltp, nama_pasien, tempat_lahir, tgl_lahir, jk, alamat, telp) VALUES(%d, '%s', '%s', '%s', '%s','%s','%s')" % (x[0],x[1], x[2],x[3], x[4], x[5],x[6])
    mycursor2.execute(etl)
    mydb2.commit()

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM tb_diagnosa")
myresult = mycursor.fetchall()
mycursor2 = mydb2.cursor()

for x in myresult:
    etl = "INSERT INTO tb_dim_diagnosa (id_diagnosa_oltp, nama_diagnosa) VALUES (%d,'%s')" % (x[0],x[1])
    mycursor2.execute(etl)
    mydb2.commit()

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM tb_poli")
myresult = mycursor.fetchall()
mycursor2 = mydb2.cursor()
for x in myresult:
    etl = "INSERT INTO tb_dim_poli (id_poli_oltp, nama_poli) VALUES (%d,'%s')" % (x[0],x[1])
    mycursor2.execute(etl)
    mydb2.commit()

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM tb_obat")
myresult = mycursor.fetchall()
mycursor2 = mydb2.cursor()
for x in myresult:
    etl = "INSERT INTO tb_dim_obat (id_obat_oltp, nama_obat, satuan, harga_satuan) VALUES (%d,'%s','%s',%d)" % (x[0],x[1],x[2],x[3])
    mycursor2.execute(etl)
    mydb2.commit()

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM tb_dokter")
myresult = mycursor.fetchall()
mycursor2 = mydb2.cursor()
for x in myresult:
    etl = "INSERT INTO tb_dim_dokter (id_dokter_oltp, nama_dokter) VALUES (%d,'%s')" % (x[0],x[1])
    mycursor2.execute(etl)
    mydb2.commit()

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM tb_jadwal")
myresult = mycursor.fetchall()
mycursor2 = mydb2.cursor()
for x in myresult:
    etl = "INSERT INTO tb_dim_jadwal (id_jadwal_oltp, hari, jam) VALUES (%d,'%s', '%s')" % (x[0],x[1],x[2])
    mycursor2.execute(etl)
    mydb2.commit()

print()