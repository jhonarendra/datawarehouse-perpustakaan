from database import *
from datetime import datetime

now = datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')


#  SELECT TABEL
mysql_select_member = ('''SELECT * FROM member''')
mysql_select_buku = ('''SELECT buku.id, buku.nama_buku , pengarang.nama_pengarang, penerbit.nama_penerbit FROM buku 
                    INNER JOIN pengarang ON buku.id_pengarang= pengarang.id 
                    INNER JOIN penerbit ON buku.id_penerbit = penerbit.id
                    ORDER BY buku.id ASC''')
mysql_select_perpustakaan = ('''SELECT * FROM cb_perpustakaan''')
mysql_select_peminjaman = ('''
SELECT buku.`id`, member.`id`, cb_perpustakaan.id, YEAR(peminjaman.`tgl_pinjam`) AS tahun, MONTHNAME(peminjaman.`tgl_pinjam`) AS bulan, 
                    COUNT(id_buku) AS jumlah
                    FROM detail_peminjaman
                    INNER JOIN peminjaman ON detail_peminjaman.`id_peminjaman`=peminjaman.`id`
                    INNER JOIN detail_buku ON detail_peminjaman.`id_detil_buku`=detail_buku.`id`
                    INNER JOIN member ON peminjaman.`id_member`=member.`id`
                    INNER JOIN buku ON detail_buku.`id_buku`=buku.`id`
                    INNER JOIN cb_perpustakaan ON peminjaman.`id_perpustakaan`=cb_perpustakaan.`id`
                    GROUP BY nama_member, bulan, nama_buku
                    ORDER BY MONTH(peminjaman.`tgl_pinjam`);''')

######################################################
#######################################################
mysql_cek_etl_member =('''
        SELECT history_etl.`end_row` FROM history_etl WHERE id_tabel = 5
        ORDER BY id DESC
        LIMIT 1;
''')
mysql_cek_etl_buku = ('''
        SELECT history_etl.`end_row` FROM history_etl WHERE id_tabel = 1
        ORDER BY id DESC
        LIMIT 1;
''')
mysql_cek_etl_perpustakaan = ('''
        SELECT history_etl.`end_row` FROM history_etl WHERE id_tabel = 2
        ORDER BY id DESC
        LIMIT 1;
''')
mysql_cek_etl_peminjaman = ('''
        SELECT history_etl.`end_row` FROM history_etl WHERE id_tabel = 7
        ORDER BY id DESC
        LIMIT 1;
''')

############################################################
############################################################

# khusus untuk fakta peminjaman
mysql_extract_peminjaman = ('''SELECT * FROM peminjaman''')
##################################

# inisialisasi cursor database perpustakaan
cursor = mysql_db.cursor()
# inisialisasi cursor warehouse perpustaakan
cursor2 = mysql_db2.cursor()

class query:

    def get_row_column(self, data):
        cursor2.execute(data)
        result = cursor2.fetchall()

        return (result)

    def mysql_db_etl(self,data):
        cursor2.execute(data)
        result = cursor2.fetchall()

        return (result)
    # def comboPerpus(self,data):

    def check_member(self, data):
        cursor2.execute(data)
        result = cursor2.fetchall()
        # print(len(result))
        if len(result) ==  0 :
            print("error")
            # insert ke tabel dimensi member di database Datawarehouse
            cursor.execute(mysql_select_member)
            get_data = cursor.fetchall()
            print(get_data)
            lenght_add_member = len(get_data)
            # print(lenght_add_member)
            end_row_add_member = get_data[lenght_add_member-1][0]
            # print(end_row_add_member)
            start_row_add_member = get_data[0][0]
            # print(start_row_add_member)
            for i in get_data:
                mysql_insert = ("INSERT INTO dim_member(id, nama_member, jenis_kelamin, alamat) VALUES (%d,'%s','%s','%s')" % (i[0], i[1], i[2], i[3]))
                cursor2.execute(mysql_insert)
                mysql_db2.commit()
            print("Dim Member Behasil Dibuat")
            # insert ke tabel histori etl di database Datawarehouse untuk merekap nilainny
            #
            mysql_insert = (
                        "INSERT INTO history_etl(id_tabel,start_row,end_row, status, tgl_proses) VALUES (%d,'%s','%s','%s','%s')" % (5, start_row_add_member, end_row_add_member, 1, formatted_date))
            cursor2.execute(mysql_insert)
            mysql_db2.commit()
            print("data sudah masuk ke histori")

        else:
            print("kode eror")
            cursor2.execute(mysql_cek_etl_member)
            count_end_row = cursor2.fetchall()
            end_row_member = count_end_row[0][0]
            mysql_cek_db_member = ("SELECT * FROM member WHERE id > %d" % (end_row_member))
            cursor.execute(mysql_cek_db_member)
            get_data = cursor.fetchall()
            print(get_data)
            lenght_add_member = len(get_data)
            if lenght_add_member == 0 :
                print("Tidak ada data baru")
            else :
                end_row_add_member = get_data[lenght_add_member-1][0]
                start_row_add_member = get_data[0][0]
                print(end_row_add_member,start_row_add_member)


                for i in get_data:
                    mysql_insert = ("INSERT INTO dim_member(id, nama_member, jenis_kelamin, alamat) VALUES (%d,'%s','%s','%s')" % (i[0], i[1], i[2], i[3]))
                    cursor2.execute(mysql_insert)
                    mysql_db2.commit()
                print("nambah data di dim member sukses")

                mysql_insert = (
                            "INSERT INTO history_etl(id_tabel,start_row,end_row, status, tgl_proses) VALUES (%d,'%s','%s','%s','%s')" % (5, start_row_add_member, end_row_add_member, 1, formatted_date))

                cursor2.execute(mysql_insert)
                mysql_db2.commit()
                print("data sudah masuk ke histori")

    def check_buku(self,data):
        cursor2.execute(data)
        result = cursor2.fetchall()
        if len(result) == 0:
            print("Data Kosong")
            cursor.execute(mysql_select_buku)
            get_data = cursor.fetchall()
            print(get_data)
            lenght_add_buku = len(get_data)
            # print(lenght_add_member)
            end_row_add_buku = get_data[lenght_add_buku - 1][0]
            # print(end_row_add_member)
            start_row_add_buku = get_data[0][0]
            # print(start_row_add_member)
            print("APA ISISNYA",start_row_add_buku, end_row_add_buku)
            for i in get_data:
                mysql_insert = (
                            "INSERT INTO dim_buku(id, nama_buku, nama_pengarang, nama_penerbit) VALUES (%d,'%s','%s','%s')" % (
                    i[0], i[1], i[2], i[3]))
                cursor2.execute(mysql_insert)
                mysql_db2.commit()
            print("Dim Buku Behasil Dibuat")
            # insert ke tabel histori etl di database Datawarehouse untuk merekap nilainny
            #
            mysql_insert = (
                    "INSERT INTO history_etl(id_tabel,start_row,end_row, status, tgl_proses) VALUES (%d,'%s','%s','%s','%s')" % (
            1, start_row_add_buku, end_row_add_buku, 1, formatted_date))
            cursor2.execute(mysql_insert)
            mysql_db2.commit()

        else:
            print("Siap untuk diisi data")
            cursor2.execute(mysql_cek_etl_buku)
            count_end_row = cursor2.fetchall()
            end_row_member = count_end_row[0][0]
            print(end_row_member)
            mysql_cek_db_member = ("SELECT buku.id, buku.nama_buku , pengarang.nama_pengarang, penerbit.nama_penerbit "
                                   "FROM buku INNER JOIN pengarang ON buku.id_pengarang= pengarang.id INNER JOIN penerbit ON buku.id_penerbit = penerbit.id WHERE buku.id > %d" % (end_row_member))
            cursor.execute(mysql_cek_db_member)
            get_data = cursor.fetchall()
            print(get_data)
            lenght_add_buku = len(get_data)
            if lenght_add_buku == 0:
                print("Tidak ada data baru")
            else:
                end_row_add_buku = get_data[lenght_add_buku - 1][0]
                start_row_add_buku = get_data[0][0]
                print(start_row_add_buku, end_row_add_buku)

                for i in get_data:
                    mysql_insert = (
                                "INSERT INTO dim_buku(id, nama_buku, nama_pengarang, nama_penerbit) VALUES (%d,'%s','%s','%s')" % (
                        i[0], i[1], i[2], i[3]))
                    cursor2.execute(mysql_insert)
                    mysql_db2.commit()
                print("nambah data di dim buku sukses")

                mysql_insert = (
                        "INSERT INTO history_etl(id_tabel,start_row,end_row, status, tgl_proses) VALUES (%d,'%s','%s','%s','%s')" % (
                1, start_row_add_buku, end_row_add_buku, 1, formatted_date))

                cursor2.execute(mysql_insert)
                mysql_db2.commit()
                print("data sudah masuk ke histori")
    def check_cabang_perpustakaan(self,data):
        cursor2.execute(data)
        result = cursor2.fetchall()
        if len(result) == 0:
            print("Data Kosong")
            cursor.execute(mysql_select_perpustakaan)
            get_data = cursor.fetchall()
            print(get_data)
            lenght_add_perpustakaan = len(get_data)
            # print(lenght_add_member)
            end_row_add_perpustakaan = get_data[lenght_add_perpustakaan - 1][0]
            # print(end_row_add_member)
            start_row_add_perpustakan = get_data[0][0]
            # print(start_row_add_member)
            for i in get_data:
                mysql_insert = (
                        "INSERT INTO dim_perpustakaan(id, nama_perpustakaan, alamat) VALUES (%d,'%s','%s')" % (
                    i[0], i[1], i[2]))
                cursor2.execute(mysql_insert)
                mysql_db2.commit()
            print("Dim Perpustakaan Behasil Dibuat")
            # insert ke tabel histori etl di database Datawarehouse untuk merekap nilainny
            #
            mysql_insert = (
                    "INSERT INTO history_etl(id_tabel,start_row,end_row, status, tgl_proses) VALUES (%d,'%s','%s','%s','%s')" % (
                2, start_row_add_perpustakan, end_row_add_perpustakaan, 1, formatted_date))
            cursor2.execute(mysql_insert)
            mysql_db2.commit()

        else:
            print("Siap untuk diisi data")
            cursor2.execute(mysql_cek_etl_perpustakaan)
            count_end_row = cursor2.fetchall()
            end_row_perpustakaan = count_end_row[0][0]
            mysql_cek_db_perpustakaan = ("SELECT * FROM cb_perpustakaan WHERE id > %d" % (end_row_perpustakaan))
            cursor.execute(mysql_cek_db_perpustakaan)
            get_data = cursor.fetchall()
            print(get_data)
            lenght_add_perpustakaan = len(get_data)
            if lenght_add_perpustakaan == 0:
                print("Tidak ada data baru")
            else:
                end_row_add_perpustakaan = get_data[lenght_add_perpustakaan - 1][0]
                start_row_add_perpustakan = get_data[0][0]
                print(end_row_add_perpustakaan, start_row_add_perpustakan)

                for i in get_data:
                    mysql_insert = (
                            "INSERT INTO dim_perpustakaan(id, nama_perpustakaan, alamat) VALUES (%d,'%s','%s')" % (
                        i[0], i[1], i[2]))
                    cursor2.execute(mysql_insert)
                    mysql_db2.commit()
                print("nambah data di dim perpustakaan sukses")

                mysql_insert = (
                        "INSERT INTO history_etl(id_tabel,start_row,end_row, status, tgl_proses) VALUES (%d,'%s','%s','%s','%s')" % (
                    2, start_row_add_perpustakan, end_row_add_perpustakaan, 1, formatted_date))

                cursor2.execute(mysql_insert)
                mysql_db2.commit()
                print("data sudah masuk ke histori")
    def check_fact_peminjaman_bulan(self,data):
        cursor2.execute(data)
        result = cursor2.fetchall()
        if len(result) == 0:
            print("Data Kosong")
            cursor.execute(mysql_select_peminjaman)
            get_data = cursor.fetchall() #mengambil data peminjaman yang akan di ETL
            print(get_data)

            cursor.execute(mysql_extract_peminjaman)
            length_peminjaman = cursor.fetchall() #mengetahui awal dan akhir data peminjaman
            lenght_add_peminjaman = len(length_peminjaman)
            # print(lenght_add_peminjaman)
            end_row_add_peminjaman = length_peminjaman[lenght_add_peminjaman - 1][0]
            # print(end_row_add_peminjaman)
            start_row_add_peminjaman = length_peminjaman[0][0]
            # print(start_row_add_peminjaman)
            for i in get_data:
                mysql_insert = ("INSERT INTO fact_peminjaman_bulan(id_dimBuku,id_dimMember,id_dimPerpustakaan,tahun,bulan,jumlah) "
                                "VALUES (%d,%d,%d,'%s','%s',%d)" % (i[0],i[1],i[2],i[3],i[4],i[5],))
                cursor2.execute(mysql_insert)
                mysql_db2.commit()
            print("Fact Peminjaman Behasil Dibuat")
            # insert ke tabel histori etl di database Datawarehouse untuk merekap nilainny
            #
            mysql_insert = (
                    "INSERT INTO history_etl(id_tabel,start_row,end_row, status, tgl_proses) VALUES (%d,'%s','%s','%s','%s')" % (
                7, start_row_add_peminjaman, end_row_add_peminjaman, 1, formatted_date))
            cursor2.execute(mysql_insert)
            mysql_db2.commit()

        else:
            cursor2.execute(mysql_cek_etl_peminjaman)
            count_end_row = cursor2.fetchall()
            end_row_etl_peminjaman = count_end_row[0][0]
            mysql_cek_db_peminjaman = ("SELECT * FROM peminjaman WHERE id > %d" % (end_row_etl_peminjaman))
            cursor.execute(mysql_cek_db_peminjaman)
            get_lenght = cursor.fetchall() #mengambil panjang data peminjaman
            # print(get_lenght)
            lenght_add_peminjaman = len(get_lenght)
            if lenght_add_peminjaman == 0:
                print("Tidak ada data baru")
            else:
                end_row_peminjaman = get_lenght[lenght_add_peminjaman - 1][0]
                start_row_peminjaman = get_lenght[0][0]
                print(end_row_peminjaman, start_row_peminjaman)

                mysql_get_peminjaman = ("SELECT buku.`id`, member.`id`, cb_perpustakaan.id, YEAR(peminjaman.`tgl_pinjam`) AS tahun, MONTHNAME(peminjaman.`tgl_pinjam`) AS bulan, COUNT(id_buku) AS jumlah FROM detail_peminjaman INNER JOIN peminjaman ON detail_peminjaman.`id_peminjaman`=peminjaman.`id` INNER JOIN detail_buku ON detail_peminjaman.`id_detil_buku`=detail_buku.`id`INNER JOIN member ON peminjaman.`id_member`=member.`id` INNER JOIN buku ON detail_buku.`id_buku`=buku.`id` INNER JOIN cb_perpustakaan ON peminjaman.`id_perpustakaan`=cb_perpustakaan.`id` WHERE peminjaman.`id` > "+str(end_row_etl_peminjaman)+" GROUP BY nama_member, bulan, nama_buku ORDER BY MONTH(peminjaman.`tgl_pinjam`)")
                cursor.execute(mysql_get_peminjaman)
                get_data = cursor.fetchall()
                print(get_data)
                for i in get_data:
                    mysql_insert = (
                            "INSERT INTO fact_peminjaman_bulan(id_dimBuku,id_dimMember,id_dimPerpustakaan,tahun,bulan,jumlah) "
                                "VALUES (%d,%d,%d,'%s','%s',%d)" % (i[0],i[1],i[2],i[3],i[4],i[5],))
                    cursor2.execute(mysql_insert)
                    mysql_db2.commit()
                print("nambah data di dim perpustakaan sukses")

                mysql_insert = (
                        "INSERT INTO history_etl(id_tabel,start_row,end_row, status, tgl_proses) VALUES (%d,'%s','%s','%s','%s')" % (
                    7, start_row_peminjaman, end_row_peminjaman, 1, formatted_date))

                cursor2.execute(mysql_insert)
                mysql_db2.commit()
                print("data sudah masuk ke histori")