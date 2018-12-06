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

mysql_combobox_tahun = ('''SELECT tahun FROM fact_peminjaman_tahun GROUP BY tahun''')

mysql_combobox_bulan = ("SELECT bulan FROM fact_peminjaman_bulan GROUP BY bulan ORDER BY id")

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        self.queries_etl = query()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1108, 726)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1111, 781))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(20, 140, 1061, 441))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.buttonExtract = QtWidgets.QPushButton(self.tab)
        self.buttonExtract.setGeometry(QtCore.QRect(20, 610, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttonExtract = QtWidgets.QPushButton(self.tab)
        self.buttonExtract.setGeometry(QtCore.QRect(20, 610, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttonExtract.setFont(font)
        self.buttonExtract.setObjectName("buttonExtract")
        self.buttonResetWH = QtWidgets.QPushButton(self.tab)
        self.buttonResetWH.setGeometry(QtCore.QRect(890, 610, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttonResetWH.setFont(font)
        self.buttonResetWH.setObjectName("buttonResetWH")
        self.buttonRefresh = QtWidgets.QPushButton(self.tab)
        self.buttonRefresh.setGeometry(QtCore.QRect(230, 610, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttonRefresh.setFont(font)
        self.buttonRefresh.setObjectName("buttonRefresh")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 51, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(80, 80, 191, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(310, 80, 31, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(350, 80, 191, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(320, 10, 361, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.comboPerpus = QtWidgets.QComboBox(self.tab_2)
        self.comboPerpus.setGeometry(QtCore.QRect(20, 120, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboPerpus.setFont(font)
        self.comboPerpus.setObjectName("comboPerpus")
        # self.comboPerpus.addItem("")
        # self.comboPerpus.addItem("")
        self.comboTahun = QtWidgets.QComboBox(self.tab_2)
        self.comboTahun.setGeometry(QtCore.QRect(20, 210, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboTahun.setFont(font)
        self.comboTahun.setObjectName("comboTahun")
        # self.comboTahun.addItem("")
        # self.comboTahun.addItem("")
        # self.comboTahun.addItem("")
        self.buttonLoad = QtWidgets.QPushButton(self.tab_2)
        self.buttonLoad.setGeometry(QtCore.QRect(20, 610, 211, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buttonLoad.setFont(font)
        self.buttonLoad.setObjectName("buttonLoad")
        self.buttonReset = QtWidgets.QPushButton(self.tab_2)
        self.buttonReset.setGeometry(QtCore.QRect(20, 540, 211, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buttonReset.setFont(font)
        self.buttonReset.setObjectName("buttonReset")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(370, 0, 421, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_2.setGeometry(QtCore.QRect(250, 70, 831, 581))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 831, 551))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setColumnCount(12)
        self.tableWidget_2.setObjectName("tableWidget_2")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, item)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_3.setGeometry(QtCore.QRect(0, 0, 831, 551))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget_3.setFont(font)
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_3.setColumnCount(12)
        self.tableWidget_3.setObjectName("tableWidget_3")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 0, item)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(20, 90, 211, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(20, 180, 211, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.tabWidget_2.raise_()
        self.comboPerpus.raise_()
        self.comboTahun.raise_()
        self.buttonLoad.raise_()
        self.buttonReset.raise_()
        self.label.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.tabBulan = QtWidgets.QWidget()
        self.tabBulan.setObjectName("tabBulan")
        self.buttonReset_2 = QtWidgets.QPushButton(self.tabBulan)
        self.buttonReset_2.setGeometry(QtCore.QRect(20, 540, 211, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buttonReset_2.setFont(font)
        self.buttonReset_2.setObjectName("buttonReset_2")
        self.comboBulan = QtWidgets.QComboBox(self.tabBulan)
        self.comboBulan.setGeometry(QtCore.QRect(20, 300, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBulan.setFont(font)
        self.comboBulan.setObjectName("comboBulan")
        # self.comboBulan.addItem("")
        # self.comboBulan.addItem("")
        # self.comboBulan.addItem("")
        # self.comboBulan.addItem("")
        # self.comboBulan.addItem("")
        # self.comboBulan.addItem("")
        # self.comboBulan.addItem("")
        # self.comboBulan.addItem("")
        # self.comboBulan.addItem("")
        # self.comboBulan.addItem("")
        # self.comboBulan.addItem("")
        # self.comboBulan.addItem("")
        self.comboPerpus_2 = QtWidgets.QComboBox(self.tabBulan)
        self.comboPerpus_2.setGeometry(QtCore.QRect(20, 120, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboPerpus_2.setFont(font)
        self.comboPerpus_2.setObjectName("comboPerpus_2")
        # self.comboPerpus_2.addItem("")
        # self.comboPerpus_2.addItem("")
        self.comboTahun_2 = QtWidgets.QComboBox(self.tabBulan)
        self.comboTahun_2.setGeometry(QtCore.QRect(20, 210, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboTahun_2.setFont(font)
        self.comboTahun_2.setObjectName("comboTahun_2")
        # self.comboTahun_2.addItem("")
        # self.comboTahun_2.addItem("")
        # self.comboTahun_2.addItem("")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tabBulan)
        self.tabWidget_3.setGeometry(QtCore.QRect(250, 70, 831, 581))
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidget_4.setGeometry(QtCore.QRect(0, 0, 831, 551))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget_4.setFont(font)
        self.tableWidget_4.setRowCount(0)
        self.tableWidget_4.setColumnCount(0)
        self.tableWidget_4.setObjectName("tableWidget_4")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(0, 0, item)
        self.tabWidget_3.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.tab_6)
        self.tableWidget_5.setGeometry(QtCore.QRect(0, 0, 831, 551))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget_5.setFont(font)
        self.tableWidget_5.setRowCount(0)
        self.tableWidget_5.setColumnCount(31)
        self.tableWidget_5.setObjectName("tableWidget_5")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setItem(0, 0, item)
        self.tabWidget_3.addTab(self.tab_6, "")
        self.buttonLoad_2 = QtWidgets.QPushButton(self.tabBulan)
        self.buttonLoad_2.setGeometry(QtCore.QRect(20, 610, 211, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buttonLoad_2.setFont(font)
        self.buttonLoad_2.setObjectName("buttonLoad_2")
        self.label_5 = QtWidgets.QLabel(self.tabBulan)
        self.label_5.setGeometry(QtCore.QRect(490, 0, 221, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self.tabBulan)
        self.label_8.setGeometry(QtCore.QRect(20, 90, 211, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tabBulan)
        self.label_9.setGeometry(QtCore.QRect(20, 180, 211, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tabBulan)
        self.label_10.setGeometry(QtCore.QRect(20, 270, 211, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tabBulan)
        self.label_11.setGeometry(QtCore.QRect(370, 0, 421, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.tabWidget.addTab(self.tabBulan, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1108, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #Get Data for Select Box
        self.comboboxPerpustaka()
        self.comboboxTahun()
        self.comboboxBulan()
        self.loadData()

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Warehouse Perpustakaan"))
        self.buttonExtract.setText(_translate("MainWindow", "Extract Data"))
        self.buttonResetWH.setText(_translate("MainWindow", "Reset Warehouse"))
        self.buttonRefresh.setText(_translate("MainWindow", "Refresh"))
        self.label_2.setText(_translate("MainWindow", "FROM"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Perpustakaan"))
        self.label_3.setText(_translate("MainWindow", "TO"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Warehouse"))
        self.label_4.setText(_translate("MainWindow", "WAREHOUSE PERPUSTAKAAN"))
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
        self.label.setText(_translate("MainWindow", "WAREHOUSE PEMINJAMAN TAHUN"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Member"))
        __sortingEnabled = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        item = self.tableWidget_3.item(0, 0)
        self.tableWidget_3.setSortingEnabled(__sortingEnabled)
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Buku"))
        self.label_6.setText(_translate("MainWindow", "Pilih Perpustakaan"))
        self.label_7.setText(_translate("MainWindow", "Pilih Tahun"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "DWH Tahun"))
        self.buttonReset_2.setText(_translate("MainWindow", "Reset Data"))
        __sortingEnabled = self.tableWidget_4.isSortingEnabled()
        self.tableWidget_4.setSortingEnabled(False)
        self.tableWidget_4.setSortingEnabled(__sortingEnabled)
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), _translate("MainWindow", "Member"))
        __sortingEnabled = self.tableWidget_5.isSortingEnabled()
        self.tableWidget_5.setSortingEnabled(False)
        item = self.tableWidget_5.item(0, 0)
        self.tableWidget_5.setSortingEnabled(__sortingEnabled)
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), _translate("MainWindow", "Buku"))
        self.buttonLoad_2.setText(_translate("MainWindow", "Load Data"))
        self.label_11.setText(_translate("MainWindow", "WAREHOUSE PEMINJAMAN BULAN"))
        self.label_8.setText(_translate("MainWindow", "Pilih Perpustakaan"))
        self.label_9.setText(_translate("MainWindow", "Pilih Tahun"))
        self.label_10.setText(_translate("MainWindow", "Pilih Bulan"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabBulan), _translate("MainWindow", "DWH Bulan"))

        self.buttonExtract.clicked.connect(self.extractData)
        self.buttonLoad.clicked.connect(self.selectDataTahun)
        self.buttonReset.clicked.connect(self.resetData)
        self.buttonRefresh.clicked.connect(self.refreshData)
        self.buttonLoad_2.clicked.connect(self.selectDataBulan)
        self.buttonResetWH.clicked.connect(self.resetWarehouse)


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
        self.comboboxTahun()
        self.comboboxPerpustaka()
        self.comboboxBulan()

    def comboboxPerpustaka(self):
        result = self.queries_etl.mysql_db_etl(mysql_combobox_perpus)
        # print(result)
        for i in range(0, len(result)):
            # print(result[i][0])
            self.comboPerpus.addItem(result[i][0])
            self.comboPerpus_2.addItem(result[i][0])

    def comboboxTahun(self):
        result = self.queries_etl.mysql_db_etl(mysql_combobox_tahun)
        # print(result)
        for i in range(0, len(result)):
            self.comboTahun.addItem(result[i][0])
            self.comboTahun_2.addItem(result[i][0])

    def comboboxBulan(self):
        result = self.queries_etl.mysql_db_etl(mysql_combobox_bulan)
        for i in range(0, len(result)):
            self.comboBulan.addItem(result[i][0])

    def resetData(self):
        # query_row = ("SELECT nama_member FROM fact_peminjaman_bulan INNER JOIN dim_member ON fact_peminjaman_bulan.`id_dimMember`=dim_member.`id` GROUP BY nama_member")
        # row_name = self.queries_etl.get_row_column(query_row)
        #
        # length = len(row_name)
        for i in range(0, 100):
            self.tableWidget_3.removeRow(0)
            self.tableWidget_2.removeRow(0)

    def extractData(self):
        self.queries_etl.check_member(mysql_check_member)
        self.queries_etl.check_buku(mysql_check_buku)
        self.queries_etl.check_cabang_perpustakaan(mysql_check_perpustakaan)
        self.queries_etl.check_fact_peminjaman(mysql_check_peminjaman)
        for i in range(0, 100):
            self.tableWidget.removeRow(0)
        self.loadData()

    def selectDataTahun(self):
        for i in range(0, 100):
            self.tableWidget_3.removeRow(0)
            self.tableWidget_2.removeRow(0)

        value_perpus = self.comboPerpus.currentText()
        print(value_perpus)
        value_tahun = self.comboTahun.currentText()

        query_row = ("SELECT nama_member FROM fact_peminjaman_tahun INNER JOIN dim_member ON fact_peminjaman_tahun.`id_dimMember`=dim_member.`id` INNER JOIN dim_perpustakaan ON fact_peminjaman_tahun.`id_dimPerpustakaan`=dim_perpustakaan.`id` WHERE nama_perpustakaan = '"+value_perpus+"' AND tahun = '"+value_tahun+"'  GROUP BY nama_member")
        row_name = self.queries_etl.get_row_column(query_row)

        query_row_book = ("SELECT nama_buku FROM fact_peminjaman_tahun INNER JOIN dim_buku ON fact_peminjaman_tahun.`id_dimBuku`=dim_buku.`id` INNER JOIN dim_perpustakaan ON fact_peminjaman_tahun.`id_dimPerpustakaan`=dim_perpustakaan.`id` WHERE nama_perpustakaan = '"+value_perpus+"' AND tahun = '"+value_tahun+"' GROUP BY nama_buku")
        row_book = self.queries_etl.get_row_column(query_row_book)

        array_row_name = []
        for x , item in enumerate(row_name):
            array_row_name.append(item[0])
            self.tableWidget_2.insertRow(x)
            self.tableWidget_2.setVerticalHeaderLabels(array_row_name)
            # print(x)
        self.tableWidget_2.setHorizontalHeaderLabels(['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'July', 'Agustus', 'September', 'Oktober', 'November', 'Desember'])
        self.tableWidget_2.horizontalHeader()

        array_row_book = []
        for x , item in enumerate(row_book):
            array_row_book.append(item[0])
            self.tableWidget_3.insertRow(x)
            self.tableWidget_3.setVerticalHeaderLabels(array_row_book)
        self.tableWidget_3.setHorizontalHeaderLabels(['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'July', 'Agustus', 'September', 'Oktober', 'November', 'Desember'])
        self.tableWidget_3.horizontalHeader()
        print("loop berhasil")

        for y, nama in enumerate(row_name):
            arr_value = [0,0,0,0,0,0,0,0,0,0,0,0]
            query_val = ("SELECT nama_member, bulan, COUNT(*) AS jumlah_peminjaman FROM fact_peminjaman_tahun INNER JOIN dim_member ON fact_peminjaman_tahun.`id_dimMember`=dim_member.`id` INNER JOIN dim_perpustakaan ON fact_peminjaman_tahun.`id_dimPerpustakaan`=dim_perpustakaan.`id` WHERE nama_member = '"+nama[0]+"' AND tahun = '"+value_tahun+"' AND nama_perpustakaan = '"+value_perpus+"'  GROUP BY bulan")
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

        for y, buku in enumerate(row_book):
            arr_value = [0,0,0,0,0,0,0,0,0,0,0,0]
            query_val = ("SELECT nama_buku, bulan, COUNT(*) AS jumlah_peminjaman FROM fact_peminjaman_tahun INNER JOIN dim_buku ON fact_peminjaman_tahun.`id_dimBuku`=dim_buku.`id` INNER JOIN dim_perpustakaan ON fact_peminjaman_tahun.`id_dimPerpustakaan`=dim_perpustakaan.`id` WHERE nama_buku = '"+buku[0]+"' AND tahun = '"+value_tahun+"' AND nama_perpustakaan = '"+value_perpus+"'  GROUP BY bulan")
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
            print("loop selesai")

            for i in range(0,12):
                self.tableWidget_3.setItem(y, i, QtWidgets.QTableWidgetItem(str(arr_value[i])))
            print("penamaan selesai")
            self.comboboxBulan()
            self.comboboxPerpustaka()
            self.comboboxTahun()

    def selectDataBulan(self):
        for i in range(0, 100):
            self.tableWidget_4.removeRow(0)
            self.tableWidget_4.removeColumn(0)
            self.tableWidget_5.removeRow(0)
            self.tableWidget_5.removeColumn(0)

        value_perpus = self.comboPerpus_2.currentText()
        print(value_perpus)
        value_tahun = self.comboTahun_2.currentText()
        value_bulan = self.comboBulan.currentText()

        query_row = ("SELECT nama_member FROM fact_peminjaman_bulan INNER JOIN dim_member ON fact_peminjaman_bulan.`id_dimMember`=dim_member.`id` INNER JOIN dim_perpustakaan ON fact_peminjaman_bulan.`id_dimPerpustakaan`=dim_perpustakaan.`id` WHERE nama_perpustakaan = '"+value_perpus+"' AND tahun = '"+value_tahun+"' AND bulan = '"+value_bulan+"'  GROUP BY nama_member")
        row_name = self.queries_etl.get_row_column(query_row)
        array_row_name = []
        for x, item in enumerate(row_name):
            array_row_name.append(item[0])
            self.tableWidget_4.insertRow(x)
            self.tableWidget_4.setVerticalHeaderLabels(array_row_name)

        query_row_book = ("SELECT nama_buku FROM fact_peminjaman_bulan INNER JOIN dim_buku ON fact_peminjaman_bulan.`id_dimBuku`=dim_buku.`id` INNER JOIN dim_perpustakaan ON fact_peminjaman_bulan.`id_dimPerpustakaan`=dim_perpustakaan.`id` WHERE nama_perpustakaan = '"+value_perpus+"' AND tahun = '"+value_tahun+"' AND bulan = '"+value_bulan+"' GROUP BY nama_buku")
        row_book = self.queries_etl.get_row_column(query_row_book)
        array_row_book = []
        for x , item in enumerate(row_book):
            array_row_book.append(item[0])
            self.tableWidget_5.insertRow(x)
            self.tableWidget_5.setVerticalHeaderLabels(array_row_book)

        batas = 0
        array_tanggal = []
        if (value_bulan == 'January') or (value_bulan == 'March') or (value_bulan == 'May') or (value_bulan == 'July') or  (value_bulan == 'August') or (value_bulan == 'October') or  (value_bulan =='December'):
            batas = 31
            for i in range(0,31):
                array_tanggal.append(str(i+1))
                self.tableWidget_4.insertColumn(i)
                self.tableWidget_4.setHorizontalHeaderLabels(array_tanggal)
                self.tableWidget_5.insertColumn(i)
                self.tableWidget_5.setHorizontalHeaderLabels(array_tanggal)
        elif value_bulan == 'February':
            leap_day = int(float(value_tahun))%4
            if leap_day == 0:
                batas = 29
                for i in range(0, 29):
                    array_tanggal.append(str(i + 1))
                    self.tableWidget_4.insertColumn(i)
                    self.tableWidget_4.setHorizontalHeaderLabels(array_tanggal)
                    self.tableWidget_5.insertColumn(i)
                    self.tableWidget_5.setHorizontalHeaderLabels(array_tanggal)
            else:
                batas = 28
                for i in range(0, 28):
                    array_tanggal.append(str(i + 1))
                    self.tableWidget_4.insertColumn(i)
                    self.tableWidget_4.setHorizontalHeaderLabels(array_tanggal)
                    self.tableWidget_5.insertColumn(i)
                    self.tableWidget_5.setHorizontalHeaderLabels(array_tanggal)
        else:
            batas = 30
            for i in range(0, 30):
                array_tanggal.append(str(i + 1))
                self.tableWidget_4.insertColumn(i)
                self.tableWidget_4.setHorizontalHeaderLabels(array_tanggal)
                self.tableWidget_5.insertColumn(i)
                self.tableWidget_5.setHorizontalHeaderLabels(array_tanggal)

        for i, nama in enumerate(row_name):
            arr_value = []
            for a in enumerate(array_tanggal):
                arr_value.append(0)
            # print(arr_value)
            query_val = ("SELECT nama_member, tanggal, COUNT(*) AS jumlah_peminjaman FROM fact_peminjaman_bulan INNER JOIN dim_member ON fact_peminjaman_bulan.`id_dimMember`=dim_member.`id` INNER JOIN dim_perpustakaan ON fact_peminjaman_bulan.`id_dimPerpustakaan`=dim_perpustakaan.`id` WHERE nama_member = '"+nama[0]+"' AND tahun = '"+value_tahun+"' AND nama_perpustakaan = '"+value_perpus+"' AND bulan = '"+value_bulan+"' GROUP BY tanggal")
            row_val = self.queries_etl.get_row_column(query_val)
            print("isi", row_val)
            for j, item in enumerate(row_val):
                print(item[1])
                for k in range(0, batas):
                    if item[1] == array_tanggal[k]:
                        arr_value[k] = item[2]
            print(arr_value)

            for l in range(0, batas):
                self.tableWidget_4.setItem(i, l, QtWidgets.QTableWidgetItem(str(arr_value[l])))

        for i, buku in enumerate(row_book):
            arr_value = []
            for a in enumerate(array_tanggal):
                arr_value.append(0)
            # print(arr_value)
            query_val = ("SELECT nama_buku, tanggal, COUNT(*) AS jumlah_peminjaman FROM fact_peminjaman_bulan INNER JOIN dim_buku ON fact_peminjaman_bulan.`id_dimBuku`=dim_buku.`id` INNER JOIN dim_perpustakaan ON fact_peminjaman_bulan.`id_dimPerpustakaan`=dim_perpustakaan.`id` WHERE nama_buku = '"+buku[0]+"' AND tahun = '"+value_tahun+"' AND nama_perpustakaan = '"+value_perpus+"' AND bulan = '"+value_bulan+"' GROUP BY tanggal")
            row_val = self.queries_etl.get_row_column(query_val)
            print("isi", row_val)
            for j, item in enumerate(row_val):
                print(item[1])
                for k in range(0, batas):
                    if item[1] == array_tanggal[k]:
                        arr_value[k] = item[2]
            print(arr_value)

            for l in range(0, batas):
                self.tableWidget_5.setItem(i, l, QtWidgets.QTableWidgetItem(str(arr_value[l])))

    def refreshData(self):
        for i in range(0, 100):
            self.tableWidget.removeRow(0)
        self.loadData()

    def resetWarehouse(self):
        self.queries_etl.resetWarehouse()
        self.loadData()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())