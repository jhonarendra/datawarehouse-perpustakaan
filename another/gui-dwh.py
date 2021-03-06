# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dwh-gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from queries_etl import *

mysql_check_member = ('''
                    SELECT * FROM history_etl WHERE id_tabel = 5
                    ORDER BY id DESC LIMIT 1
''')
mysql_check_buku = ('''
                    SELECT * FROM history_etl WHERE id_tabel = 1
                    ORDER BY id DESC LIMIT 1
''')
mysql_check_perpustakaan = ('''
                    SELECT * FROM history_etl WHERE id_tabel = 2
                    ORDER BY id DESC LIMIT 1
''')
mysql_check_peminjaman = ('''
                    SELECT * FROM history_etl WHERE id_tabel = 7
                    ORDER BY id DESC LIMIT 1
''')

show_data_tabel_etl = ('''SELECT nama_tabel, start_row, end_row, `status`, tgl_proses FROM history_etl
INNER JOIN tb_tabel ON history_etl.`id_tabel` = tb_tabel.`id`
ORDER BY history_etl.`id` ASC''')

mysql_combobox_perpus = ('''SELECT nama_perpustakaan FROM dim_perpustakaan''')

mysql_combobox_tahun = ('''SELECT tahun FROM fact_peminjaman_bulan GROUP BY tahun''')

class Ui_MainWindow(object):
    def loadData(self):
        result = self.queries_etl.mysql_db_etl(show_data_tabel_etl)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number, QtWidgets.QTableWidgetItem(str(data)))
                self.tableWidget.setHorizontalHeaderLabels(['Nama Tabel', 'Data Awal', 'Data Akhir', 'Status', 'Waktu Proses'])
                header = self.tableWidget.horizontalHeader()
                header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
                header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
                header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
                header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
                header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
    def comboboxPerpustaka(self):
        result = self.queries_etl.mysql_db_etl(mysql_combobox_perpus)
        # print(result)
        for i in range(0, len(result)):
            # print(result[i][0])
            self.comboPerpus.addItem(result[i][0])

    def comboboxTahun(self):
        result = self.queries_etl.mysql_db_etl(mysql_combobox_tahun)
        # print(result)
        for i in range(0, len(result)):
            self.comboTahun.addItem(result[i][0])

    def setupUi(self, MainWindow):
        # conect file queries_etl
        self.queries_etl = query()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1110, 812)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1101, 781))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 1081, 441))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.buttonExtract = QtWidgets.QPushButton(self.tab)
        self.buttonExtract.setGeometry(QtCore.QRect(10, 550, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttonExtract.setFont(font)
        self.buttonExtract.setObjectName("buttonExtract")
        # definisi button
        self.buttonExtract.clicked.connect(self.extractData)
        self.loadData()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(260, 150, 811, 531))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget_2.setFont(font)
        # self.tableWidget_2.setRowCount(5)
        self.tableWidget_2.setColumnCount(12)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.comboPerpus = QtWidgets.QComboBox(self.tab_2)
        self.comboPerpus.setGeometry(QtCore.QRect(50, 160, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboPerpus.setFont(font)
        self.comboPerpus.setObjectName("comboPerpus")
        self.comboboxPerpustaka()
        # self.comboPerpus.addItem("")
        # self.comboPerpus.addItem("")
        self.comboTahun = QtWidgets.QComboBox(self.tab_2)
        self.comboTahun.setGeometry(QtCore.QRect(50, 250, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboTahun.setFont(font)
        self.comboTahun.setObjectName("comboTahun")
        self.comboboxTahun()
        # self.comboTahun.addItem("")
        # self.comboTahun.addItem("")
        # self.comboTahun.addItem("")
        self.buttonLoad = QtWidgets.QPushButton(self.tab_2)
        self.buttonLoad.setGeometry(QtCore.QRect(60, 640, 151, 41))
        self.buttonLoad.setObjectName("buttonLoad")
        self.buttonReset = QtWidgets.QPushButton(self.tab_2)
        self.buttonReset.setGeometry(QtCore.QRect(60, 570, 151, 41))
        self.buttonReset.setObjectName("buttonReset")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(460, 40, 221, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1110, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonExtract.setText(_translate("MainWindow", "Extract Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Database"))
        # self.comboPerpus.setCurrentText(_translate("MainWindow", "Perpustakaan Bersama"))
        # self.comboPerpus.setItemText(0, _translate("MainWindow", "Perpustakaan Bersama"))
        # self.comboPerpus.setItemText(1, _translate("MainWindow", "Perpustakaan Jurusan"))
        # self.comboTahun.setCurrentText(_translate("MainWindow", "2017"))
        # self.comboTahun.setItemText(0, _translate("MainWindow", "2017"))
        # self.comboTahun.setItemText(1, _translate("MainWindow", "2018"))
        # self.comboTahun.setItemText(2, _translate("MainWindow", "2019"))
        self.buttonLoad.setText(_translate("MainWindow", "Load Data"))
        self.buttonReset.setText(_translate("MainWindow", "Reset Data"))
        self.label.setText(_translate("MainWindow", "PEMINJAMAN"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Data Warehouse"))

        self.buttonLoad.clicked.connect(self.selectData)

    def extractData(self):
        self.queries_etl.check_member(mysql_check_member)
        self.queries_etl.check_buku(mysql_check_buku)
        self.queries_etl.check_cabang_perpustakaan(mysql_check_perpustakaan)
        self.queries_etl.check_fact_peminjaman_bulan(mysql_check_peminjaman)
    def selectData(self):
        value_perpus = self.comboPerpus.currentIndex()
        value_perpus += 1
        value_tahun = self.comboTahun.currentText()

        query_row = ("SELECT nama_member FROM fact_peminjaman_bulan INNER JOIN dim_member ON fact_peminjaman_bulan.`id_dimMember`=dim_member.`id` GROUP BY nama_member")
        row_name = self.queries_etl.get_row_column(query_row)

        array_row_name = []
        for x , item in enumerate(row_name):
            array_row_name.append(item[0])
            self.tableWidget_2.insertRow(x)
            self.tableWidget_2.setVerticalHeaderLabels(array_row_name)
        self.tableWidget_2.setHorizontalHeaderLabels(['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'July', 'Agustus', 'September', 'Oktober', 'November', 'Desember'])
        self.tableWidget_2.horizontalHeader()

        for y, nama in enumerate(row_name):
            arr_value = [0,0,0,0,0,0,0,0,0,0,0,0]
            query_val = ("SELECT nama_member, bulan, COUNT(*) AS jumlah_peminjaman FROM fact_peminjaman_bulan INNER JOIN dim_member ON fact_peminjaman_bulan.`id_dimMember`=dim_member.`id` WHERE nama_member = '"+nama[0]+"' AND tahun = 2018 GROUP BY bulan")
            row_val = self.queries_etl.get_row_column(query_val)
            # print("isi ;",row_val)

            for x, item in enumerate(row_val):
                if item[1] == "January":
                    arr_value[0] = item[2]
                if item[1] == "February":
                    arr_value[1] = item[2]
                if item[1] == "March":
                    arr_value[2] = item[2]
                if item[1] == "April":
                    arr_value[3] = item[2]
                if item[1] == "May":
                    arr_value[4] = item[2]
                if item[1] == "June":
                    arr_value[5] = item[2]
                if item[1] == "July":
                    arr_value[6] = item[2]
                if item[1] == "August":
                    arr_value[7] = item[2]
                if item[1] == "September":
                    arr_value[8] = item[2]
                if item[1] == "October":
                    arr_value[9] = item[2]
                if item[1] == "November":
                    arr_value[10] = item[2]
                if item[1] == "December":
                    arr_value[11] = item[2]

            # print(arr_value)
            # arr_value = []
            # for x, item in enumerate(row_name):
            #     query_val = ("SELECT COUNT(*) AS jumlah_peminjaman FROM fact_peminjaman_bulan INNER JOIN dim_member ON fact_peminjaman_bulan.`id_dimMember`=dim_member.`id` WHERE nama_member = '"+item[0]+"' AND tahun = 2018 AND bulan = 'januari' GROUP BY bulan")
            #     row_val = self.queries_etl.get_row_column(query_val)
            #     arr_value.append(row_val)
            # print(arr_value)

            for i in range(0,12):
                self.tableWidget_2.setItem(y, i, QtWidgets.QTableWidgetItem(str(arr_value[i])))



        # query_value =



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())