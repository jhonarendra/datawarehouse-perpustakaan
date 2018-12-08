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
        MainWindow.resize(1149, 809)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconbook/book2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1141, 781))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(20, 180, 1061, 441))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        # self.tableWidget.setRowCount(5)
        # self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.buttonExtract = QtWidgets.QPushButton(self.tab)
        self.buttonExtract.setGeometry(QtCore.QRect(20, 670, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttonExtract.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/iconextract/add-to-database.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.buttonExtract.setIcon(icon1)
        self.buttonExtract.setIconSize(QtCore.QSize(30, 30))
        self.buttonExtract.setCheckable(True)
        self.buttonExtract.setObjectName("buttonExtract")
        self.buttonResetWH = QtWidgets.QPushButton(self.tab)
        self.buttonResetWH.setGeometry(QtCore.QRect(860, 670, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttonResetWH.setFont(font)
        self.buttonResetWH.setAutoFillBackground(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/min/min-sql.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.buttonResetWH.setIcon(icon2)
        self.buttonResetWH.setIconSize(QtCore.QSize(30, 30))
        self.buttonResetWH.setAutoDefault(False)
        self.buttonResetWH.setObjectName("buttonResetWH")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 51, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(90, 130, 191, 31))
        self.comboBox.setTabletTracking(False)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(310, 130, 31, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(350, 130, 191, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(410, 30, 471, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.buttonRefresh = QtWidgets.QPushButton(self.tab)
        self.buttonRefresh.setGeometry(QtCore.QRect(240, 670, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttonRefresh.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/refresh/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.buttonRefresh.setIcon(icon3)
        self.buttonRefresh.setIconSize(QtCore.QSize(30, 30))
        self.buttonRefresh.setObjectName("buttonRefresh")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(350, 20, 51, 71))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/iconbook/book2.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/setting/download (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab, icon4, "")
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
        self.buttonLoad.setGeometry(QtCore.QRect(20, 600, 211, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buttonLoad.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/sql-query/sql_query.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.buttonLoad.setIcon(icon5)
        self.buttonLoad.setIconSize(QtCore.QSize(30, 30))
        self.buttonLoad.setObjectName("buttonLoad")
        self.buttonReset = QtWidgets.QPushButton(self.tab_2)
        self.buttonReset.setGeometry(QtCore.QRect(20, 530, 211, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buttonReset.setFont(font)
        self.buttonReset.setIcon(icon2)
        self.buttonReset.setIconSize(QtCore.QSize(30, 30))
        self.buttonReset.setObjectName("buttonReset")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(380, 10, 541, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_2.setGeometry(QtCore.QRect(250, 70, 831, 581))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 831, 551))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setRowCount(5)
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setObjectName("tableWidget_2")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, item)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/person/grab-vector-graphic-person-icon--imagebasket-13.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget_2.addTab(self.tab_3, icon6, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_3.setGeometry(QtCore.QRect(0, 0, 831, 551))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget_3.setFont(font)
        self.tableWidget_3.setRowCount(5)
        self.tableWidget_3.setColumnCount(5)
        self.tableWidget_3.setObjectName("tableWidget_3")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 0, item)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/book2/book3.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget_2.addTab(self.tab_4, icon7, "")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(50, 90, 171, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(50, 180, 111, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(20, 90, 21, 21))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap(":/date/date.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(20, 180, 21, 21))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap(":/date/date.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.tabWidget_2.raise_()
        self.comboPerpus.raise_()
        self.comboTahun.raise_()
        self.buttonLoad.raise_()
        self.buttonReset.raise_()
        self.label.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/show/images (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab_2, icon8, "")
        self.tabBulan = QtWidgets.QWidget()
        self.tabBulan.setObjectName("tabBulan")
        self.buttonReset_2 = QtWidgets.QPushButton(self.tabBulan)
        self.buttonReset_2.setGeometry(QtCore.QRect(20, 530, 211, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buttonReset_2.setFont(font)
        self.buttonReset_2.setIcon(icon2)
        self.buttonReset_2.setIconSize(QtCore.QSize(30, 30))
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
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tabWidget_3.setFont(font)
        self.tabWidget_3.setAutoFillBackground(False)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidget_4.setGeometry(QtCore.QRect(0, 0, 831, 551))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget_4.setFont(font)
        self.tableWidget_4.setRowCount(5)
        self.tableWidget_4.setColumnCount(5)
        self.tableWidget_4.setObjectName("tableWidget_4")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(0, 0, item)
        self.tabWidget_3.addTab(self.tab_5, icon6, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.tab_6)
        self.tableWidget_5.setGeometry(QtCore.QRect(0, 0, 831, 551))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget_5.setFont(font)
        self.tableWidget_5.setRowCount(5)
        self.tableWidget_5.setColumnCount(5)
        self.tableWidget_5.setObjectName("tableWidget_5")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setItem(0, 0, item)
        self.tabWidget_3.addTab(self.tab_6, icon7, "")
        self.buttonLoad_2 = QtWidgets.QPushButton(self.tabBulan)
        self.buttonLoad_2.setGeometry(QtCore.QRect(20, 600, 211, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buttonLoad_2.setFont(font)
        self.buttonLoad_2.setIcon(icon5)
        self.buttonLoad_2.setIconSize(QtCore.QSize(30, 30))
        self.buttonLoad_2.setObjectName("buttonLoad_2")
        self.label_8 = QtWidgets.QLabel(self.tabBulan)
        self.label_8.setGeometry(QtCore.QRect(50, 90, 171, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tabBulan)
        self.label_9.setGeometry(QtCore.QRect(50, 180, 171, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tabBulan)
        self.label_10.setGeometry(QtCore.QRect(50, 270, 141, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tabBulan)
        self.label_11.setGeometry(QtCore.QRect(380, 10, 521, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tabBulan)
        self.label_12.setGeometry(QtCore.QRect(20, 90, 21, 21))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap(":/date/date.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tabBulan)
        self.label_13.setGeometry(QtCore.QRect(20, 180, 21, 21))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap(":/date/date.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tabBulan)
        self.label_14.setGeometry(QtCore.QRect(20, 270, 21, 21))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap(":/date/date.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.tabWidget.addTab(self.tabBulan, icon8, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1149, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(1)
        self.tabWidget_3.setCurrentIndex(1)

        #Get Data for Select Box
        self.comboboxTahun()
        self.comboboxPerpustaka()
        self.comboboxBulan()
        self.loadData()

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Data Warehouse | Kelompok 3"))
        self.buttonExtract.setText(_translate("MainWindow", "Extract Data"))
        self.buttonResetWH.setText(_translate("MainWindow", "Reset Warehouse"))
        self.label_2.setText(_translate("MainWindow", "FROM"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Perpustakaan"))
        self.label_3.setText(_translate("MainWindow", "TO"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Warehouse"))
        self.label_4.setText(_translate("MainWindow", "WAREHOUSE PERPUSTAKAAN"))
        self.buttonRefresh.setText(_translate("MainWindow", " Refresh"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Database"))
        self.comboPerpus.setCurrentText(_translate("MainWindow", "Perpustakaan Bersama"))
        self.comboPerpus.setItemText(0, _translate("MainWindow", "Perpustakaan Bersama"))
        self.comboPerpus.setItemText(1, _translate("MainWindow", "Perpustakaan Jurusan"))
        self.comboTahun.setCurrentText(_translate("MainWindow", "2017"))
        self.comboTahun.setItemText(0, _translate("MainWindow", "2017"))
        self.comboTahun.setItemText(1, _translate("MainWindow", "2018"))
        self.comboTahun.setItemText(2, _translate("MainWindow", "2019"))
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
        item.setText(_translate("MainWindow", "test"))
        self.tableWidget_3.setSortingEnabled(__sortingEnabled)
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Buku"))
        self.label_6.setText(_translate("MainWindow", "Pilih Perpustakaan"))
        self.label_7.setText(_translate("MainWindow", "Pilih Tahun"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Warehouse Tahun"))
        self.buttonReset_2.setText(_translate("MainWindow", "Reset Data"))
        # self.comboBulan.setCurrentText(_translate("MainWindow", "Januari"))
        # self.comboBulan.setItemText(0, _translate("MainWindow", "Januari"))
        # self.comboBulan.setItemText(1, _translate("MainWindow", "Februari"))
        # self.comboBulan.setItemText(2, _translate("MainWindow", "Maret"))
        # self.comboBulan.setItemText(3, _translate("MainWindow", "April"))
        # self.comboBulan.setItemText(4, _translate("MainWindow", "Mei"))
        # self.comboBulan.setItemText(5, _translate("MainWindow", "Juni"))
        # self.comboBulan.setItemText(6, _translate("MainWindow", "Juli"))
        # self.comboBulan.setItemText(7, _translate("MainWindow", "Agustus"))
        # self.comboBulan.setItemText(8, _translate("MainWindow", "September"))
        # self.comboBulan.setItemText(9, _translate("MainWindow", "Oktober"))
        # self.comboBulan.setItemText(10, _translate("MainWindow", "November"))
        # self.comboBulan.setItemText(11, _translate("MainWindow", "Desember"))
        # self.comboPerpus_2.setCurrentText(_translate("MainWindow", "Perpustakaan Bersama"))
        # self.comboPerpus_2.setItemText(0, _translate("MainWindow", "Perpustakaan Bersama"))
        # self.comboPerpus_2.setItemText(1, _translate("MainWindow", "Perpustakaan Jurusan"))
        # self.comboTahun_2.setCurrentText(_translate("MainWindow", "2017"))
        # self.comboTahun_2.setItemText(0, _translate("MainWindow", "2017"))
        # self.comboTahun_2.setItemText(1, _translate("MainWindow", "2018"))
        # self.comboTahun_2.setItemText(2, _translate("MainWindow", "2019"))
        __sortingEnabled = self.tableWidget_4.isSortingEnabled()
        self.tableWidget_4.setSortingEnabled(False)
        self.tableWidget_4.setSortingEnabled(__sortingEnabled)
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), _translate("MainWindow", "Member"))
        __sortingEnabled = self.tableWidget_5.isSortingEnabled()
        self.tableWidget_5.setSortingEnabled(False)
        item = self.tableWidget_5.item(0, 0)
        item.setText(_translate("MainWindow", "test"))
        self.tableWidget_5.setSortingEnabled(__sortingEnabled)
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), _translate("MainWindow", "Buku"))
        self.buttonLoad_2.setText(_translate("MainWindow", "Load Data"))
        self.label_8.setText(_translate("MainWindow", "Pilih Perpustakaan"))
        self.label_9.setText(_translate("MainWindow", "Pilih Tahun"))
        self.label_10.setText(_translate("MainWindow", "Pilih Bulan"))
        self.label_11.setText(_translate("MainWindow", "WAREHOUSE PEMINJAMAN BULAN"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabBulan), _translate("MainWindow", "Warehouse Bulan"))

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
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                self.tableWidget.setHorizontalHeaderLabels(
                    ['Nama Tabel', 'Data Awal', 'Data Akhir', 'Status', 'Waktu Proses'])
                header = self.tableWidget.horizontalHeader()
                header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
                header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
                header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
                header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
                header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)

    def comboboxPerpustaka(self):
        self.comboPerpus.clear()
        self.comboPerpus_2.clear()
        result = self.queries_etl.mysql_db_etl(mysql_combobox_perpus)
        # print(result)
        for i in range(0, len(result)):
            # print(result[i][0])
            self.comboPerpus.addItem(result[i][0])
            self.comboPerpus_2.addItem(result[i][0])

    def comboboxTahun(self):
        self.comboTahun.clear()
        self.comboTahun_2.clear()
        result = self.queries_etl.mysql_db_etl(mysql_combobox_tahun)
        # print(result)
        for i in range(0, len(result)):
            self.comboTahun.addItem(result[i][0])
            self.comboTahun_2.addItem(result[i][0])

    def comboboxBulan(self):
        self.comboBulan.clear()
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
        print("cek_buku")
        self.queries_etl.check_buku(mysql_check_buku)
        self.queries_etl.check_cabang_perpustakaan(mysql_check_perpustakaan)
        self.queries_etl.check_fact_peminjaman(mysql_check_peminjaman)
        for i in range(0, 100):
            self.tableWidget.removeRow(0)
        self.loadData()
        self.comboboxBulan()
        self.comboboxPerpustaka()
        self.comboboxTahun()

    def selectDataTahun(self):
        for i in range(0, 100):
            self.tableWidget_2.removeRow(0)
            self.tableWidget_2.removeColumn(0)
            self.tableWidget_3.removeRow(0)
            self.tableWidget_3.removeColumn(0)

        value_perpus = self.comboPerpus.currentText()
        value_tahun = self.comboTahun.currentText()

        query_row = (
                    "SELECT nama_member FROM fact_peminjaman_tahun INNER JOIN dim_member ON fact_peminjaman_tahun.`id_dimMember`=dim_member.`id` INNER JOIN dim_perpustakaan ON fact_peminjaman_tahun.`id_dimPerpustakaan`=dim_perpustakaan.`id` WHERE nama_perpustakaan = '" + value_perpus + "' AND tahun = '" + value_tahun + "'  GROUP BY nama_member")
        row_name = self.queries_etl.get_row_column(query_row)

        query_row_book = (
                    "SELECT nama_buku FROM fact_peminjaman_tahun INNER JOIN dim_buku ON fact_peminjaman_tahun.`id_dimBuku`=dim_buku.`id` INNER JOIN dim_perpustakaan ON fact_peminjaman_tahun.`id_dimPerpustakaan`=dim_perpustakaan.`id` WHERE nama_perpustakaan = '" + value_perpus + "' AND tahun = '" + value_tahun + "' GROUP BY nama_buku")
        row_book = self.queries_etl.get_row_column(query_row_book)

        array_row_name = []
        for x, item in enumerate(row_name):
            array_row_name.append(item[0])
        array_row_name.append("Total")

        print(array_row_name)
        for y in range(len(row_name) + 1):
            self.tableWidget_2.insertRow(y)
            self.tableWidget_2.setVerticalHeaderLabels(array_row_name)

        array_row_book = []
        row_min = len(row_book)
        get_row_book = len(row_book) + 1
        for x, item in enumerate(row_book):
            array_row_book.append(item[0])
        array_row_book.append("Total")

        for y in range(get_row_book):
            self.tableWidget_3.insertRow(y)
            self.tableWidget_3.setVerticalHeaderLabels(array_row_book)

        array_column = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'July', 'Agustus', 'September',
                        'Oktober', 'November', 'Desember', 'Total']
        for x in range(13):
            self.tableWidget_3.insertColumn(x)
            self.tableWidget_3.setHorizontalHeaderLabels(array_column)
            # self.tableWidget_3.horizontalHeader()
            self.tableWidget_2.insertColumn(x)
            self.tableWidget_2.setHorizontalHeaderLabels(array_column)
            # self.tableWidget_2.horizontalHeader()
        print("loop berhasil")

        total_data_nama = []
        for i in range(12):
            total_data_nama.append([i, 0])
        print(total_data_nama)
        for y, nama in enumerate(row_name):
            arr_value = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            query_val = (
                        "SELECT nama_member, bulan, SUM(jumlah) AS jumlah FROM fact_peminjaman_tahun INNER JOIN dim_member ON fact_peminjaman_tahun.`id_dimMember`=dim_member.`id` INNER JOIN dim_perpustakaan ON fact_peminjaman_tahun.`id_dimPerpustakaan`=dim_perpustakaan.`id` WHERE nama_member = '" +
                        nama[
                            0] + "' AND tahun = '" + value_tahun + "' AND nama_perpustakaan = '" + value_perpus + "'  GROUP BY bulan")
            row_val = self.queries_etl.get_row_column(query_val)
            # print("isi ;",row_val)

            for x, item in enumerate(row_val):
                if item[1] == "January":
                    arr_value[0] = item[2]
                    total_data_nama[0][1] = total_data_nama[0][1] + item[2]
                if item[1] == "February":
                    arr_value[1] = item[2]
                    total_data_nama[1][1] = total_data_nama[1][1] + item[2]
                if item[1] == "March":
                    arr_value[2] = item[2]
                    total_data_nama[2][1] = total_data_nama[2][1] + item[2]
                if item[1] == "April":
                    arr_value[3] = item[2]
                    total_data_nama[3][1] = total_data_nama[3][1] + item[2]
                if item[1] == "May":
                    arr_value[4] = item[2]
                    total_data_nama[4][1] = total_data_nama[4][1] + item[2]
                if item[1] == "June":
                    arr_value[5] = item[2]
                    total_data_nama[5][1] = total_data_nama[5][1] + item[2]
                if item[1] == "July":
                    arr_value[6] = item[2]
                    total_data_nama[6][1] = total_data_nama[6][1] + item[2]
                if item[1] == "August":
                    arr_value[7] = item[2]
                    total_data_nama[7][1] = total_data_nama[7][1] + item[2]
                if item[1] == "September":
                    arr_value[8] = item[2]
                    total_data_nama[8][1] = total_data_nama[8][1] + item[2]
                if item[1] == "October":
                    arr_value[9] = item[2]
                    total_data_nama[9][1] = total_data_nama[9][1] + item[2]
                if item[1] == "November":
                    arr_value[10] = item[2]
                    total_data_nama[10][1] = total_data_nama[10][1] + item[2]
                if item[1] == "December":
                    arr_value[11] = item[2]
                    total_data_nama[11][1] = total_data_nama[11][1] + item[2]

            total_user = 0
            for i in range(12):
                total_user = total_user + arr_value[i]
            # print(total_user)
            arr_value.append(total_user)
            # print(arr_value)
            for i in range(0, 13):
                self.tableWidget_2.setItem(y, i, QtWidgets.QTableWidgetItem(str(arr_value[i])))

        total = 0
        for y in range(12):
            total = total + total_data_nama[y][1]
        total_data_nama.append([12, total])
        print(total_data_nama)
        for x in range(13):
            self.tableWidget_2.setItem(len(row_name), x, QtWidgets.QTableWidgetItem(str(total_data_nama[x][1])))

        total_data_buku = []
        for i in range(12):
            total_data_buku.append([i, 0])

        for y, buku in enumerate(row_book):
            arr_value = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            query_val = (
                        "SELECT nama_buku, bulan, SUM(jumlah) AS jumlah FROM fact_peminjaman_tahun INNER JOIN dim_buku ON fact_peminjaman_tahun.`id_dimBuku`=dim_buku.`id` INNER JOIN dim_perpustakaan ON fact_peminjaman_tahun.`id_dimPerpustakaan`=dim_perpustakaan.`id` WHERE nama_buku = '" +
                        buku[
                            0] + "' AND tahun = '" + value_tahun + "' AND nama_perpustakaan = '" + value_perpus + "'  GROUP BY bulan")
            row_val = self.queries_etl.get_row_column(query_val)

            for x, item in enumerate(row_val):
                if item[1] == "January":
                    arr_value[0] = item[2]
                    total_data_buku[0][1] = total_data_buku[0][1] + item[2]
                if item[1] == "February":
                    arr_value[1] = item[2]
                    total_data_buku[1][1] = total_data_buku[1][1] + item[2]
                if item[1] == "March":
                    arr_value[2] = item[2]
                    total_data_buku[2][1] = total_data_buku[2][1] + item[2]
                if item[1] == "April":
                    arr_value[3] = item[2]
                    total_data_buku[3][1] = total_data_buku[3][1] + item[2]
                if item[1] == "May":
                    arr_value[4] = item[2]
                    total_data_buku[4][1] = total_data_buku[4][1] + item[2]
                if item[1] == "June":
                    arr_value[5] = item[2]
                    total_data_buku[5][1] = total_data_buku[5][1] + item[2]
                if item[1] == "July":
                    arr_value[6] = item[2]
                    total_data_buku[6][1] = total_data_buku[6][1] + item[2]
                if item[1] == "August":
                    arr_value[7] = item[2]
                    total_data_buku[7][1] = total_data_buku[7][1] + item[2]
                if item[1] == "September":
                    arr_value[8] = item[2]
                    total_data_buku[8][1] = total_data_buku[8][1] + item[2]
                if item[1] == "October":
                    arr_value[9] = item[2]
                    total_data_buku[9][1] = total_data_buku[9][1] + item[2]
                if item[1] == "November":
                    arr_value[10] = item[2]
                    total_data_buku[10][1] = total_data_buku[10][1] + item[2]
                if item[1] == "December":
                    arr_value[11] = item[2]
                    total_data_buku[11][1] = total_data_buku[11][1] + item[2]

            total_buku = 0
            for i in range(12):
                total_buku = total_buku + arr_value[i]

            arr_value.append(total_buku)
            for i in range(0, 13):
                self.tableWidget_3.setItem(y, i, QtWidgets.QTableWidgetItem(str(arr_value[i])))

        total_buku = 0
        for y in range(12):
            total_buku = total_buku + total_data_buku[y][1]
        print(total_buku)
        total_data_buku.append([13, total_buku])
        for x in range(13):
            self.tableWidget_3.setItem(get_row_book - 1, x, QtWidgets.QTableWidgetItem(str(total_data_buku[x][1])))

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

        query_row = (
                    "SELECT nama_member FROM fact_peminjaman_bulan INNER JOIN dim_member ON fact_peminjaman_bulan.`id_dimMember`=dim_member.`id` INNER JOIN dim_perpustakaan ON fact_peminjaman_bulan.`id_dimPerpustakaan`=dim_perpustakaan.`id` WHERE nama_perpustakaan = '" + value_perpus + "' AND tahun = '" + value_tahun + "' AND bulan = '" + value_bulan + "'  GROUP BY nama_member")
        row_name = self.queries_etl.get_row_column(query_row)
        array_row_name = []
        for x, item in enumerate(row_name):
            array_row_name.append(item[0])
        array_row_name.append("Total")
        for x in range(len(row_name) + 1):
            self.tableWidget_4.insertRow(x)
            self.tableWidget_4.setVerticalHeaderLabels(array_row_name)

        query_row_book = (
                    "SELECT nama_buku FROM fact_peminjaman_bulan INNER JOIN dim_buku ON fact_peminjaman_bulan.`id_dimBuku`=dim_buku.`id` INNER JOIN dim_perpustakaan ON fact_peminjaman_bulan.`id_dimPerpustakaan`=dim_perpustakaan.`id` WHERE nama_perpustakaan = '" + value_perpus + "' AND tahun = '" + value_tahun + "' AND bulan = '" + value_bulan + "' GROUP BY nama_buku")
        row_book = self.queries_etl.get_row_column(query_row_book)
        array_row_book = []
        for x, item in enumerate(row_book):
            array_row_book.append(item[0])
        array_row_book.append("Total")
        for x in range(len(row_book) + 1):
            self.tableWidget_5.insertRow(x)
            self.tableWidget_5.setVerticalHeaderLabels(array_row_book)

        array_tanggal = []
        if (value_bulan == 'January') or (value_bulan == 'March') or (value_bulan == 'May') or (
                value_bulan == 'July') or (value_bulan == 'August') or (value_bulan == 'October') or (
                value_bulan == 'December'):
            batas = 32
            for i in range(0, batas):
                if i <= 30:
                    array_tanggal.append(str(i + 1))
                    self.tableWidget_4.insertColumn(i)
                    self.tableWidget_4.setHorizontalHeaderLabels(array_tanggal)
                    self.tableWidget_5.insertColumn(i)
                    self.tableWidget_5.setHorizontalHeaderLabels(array_tanggal)
                else:
                    array_tanggal.append("Total")
                    self.tableWidget_4.insertColumn(i)
                    self.tableWidget_4.setHorizontalHeaderLabels(array_tanggal)
                    self.tableWidget_5.insertColumn(i)
                    self.tableWidget_5.setHorizontalHeaderLabels(array_tanggal)

        elif value_bulan == 'February':
            leap_day = int(float(value_tahun)) % 4
            if leap_day == 0:
                batas = 30
                for i in range(0, batas):
                    array_tanggal.append(str(i + 1))
                    self.tableWidget_4.insertColumn(i)
                    self.tableWidget_4.setHorizontalHeaderLabels(array_tanggal)
                    self.tableWidget_5.insertColumn(i)
                    self.tableWidget_5.setHorizontalHeaderLabels(array_tanggal)
            else:
                batas = 29
                for i in range(0, batas):
                    array_tanggal.append(str(i + 1))
                    self.tableWidget_4.insertColumn(i)
                    self.tableWidget_4.setHorizontalHeaderLabels(array_tanggal)
                    self.tableWidget_5.insertColumn(i)
                    self.tableWidget_5.setHorizontalHeaderLabels(array_tanggal)
        else:
            batas = 31
            for i in range(0, batas):
                array_tanggal.append(str(i + 1))
                self.tableWidget_4.insertColumn(i)
                self.tableWidget_4.setHorizontalHeaderLabels(array_tanggal)
                self.tableWidget_5.insertColumn(i)
                self.tableWidget_5.setHorizontalHeaderLabels(array_tanggal)

        total_data = []
        for i in range(batas - 1):
            total_data.append([str(i + 1), 0])
        # print(total_data)
        for i, nama in enumerate(row_name):
            arr_value = []
            for a in range(0, batas - 1):
                arr_value.append(0)
            # print(len(arr_value))
            query_val = (
                        "SELECT nama_member, tanggal, SUM(jumlah) AS jumlah FROM fact_peminjaman_bulan INNER JOIN dim_member ON fact_peminjaman_bulan.`id_dimMember`=dim_member.`id` INNER JOIN dim_perpustakaan ON fact_peminjaman_bulan.`id_dimPerpustakaan`=dim_perpustakaan.`id` WHERE nama_member = '" +
                        nama[
                            0] + "' AND tahun = '" + value_tahun + "' AND nama_perpustakaan = '" + value_perpus + "' AND bulan = '" + value_bulan + "' GROUP BY tanggal")
            row_val = self.queries_etl.get_row_column(query_val)
            # print("isi", row_val)
            total_user = 0
            for j, item in enumerate(row_val):
                # print(item[1])
                for k in range(0, batas - 1):
                    if item[1] == array_tanggal[k]:
                        arr_value[k] = item[2]
                        total_user = total_user + arr_value[k]
                    if item[1] == total_data[k][0]:
                        total_data[k][1] = total_data[k][1] + item[2]

            arr_value.append(total_user)
            # print(arr_value)
            for l in range(0, batas):
                self.tableWidget_4.setItem(i, l, QtWidgets.QTableWidgetItem(str(arr_value[l])))
            # print(len(arr_value))

        print(total_data)
        total = 0
        for y in range(batas - 1):
            total = total + total_data[y][1]
        total_data.append([str(batas), total])
        for x in range(batas):
            self.tableWidget_4.setItem(len(row_name), x, QtWidgets.QTableWidgetItem(str(total_data[x][1])))

        total_data_buku = []
        for i in range(batas - 1):
            total_data_buku.append([str(i + 1), 0])

        for i, buku in enumerate(row_book):
            arr_value = []
            for a in range(batas - 1):
                arr_value.append(0)
            # print(arr_value)
            query_val = (
                        "SELECT nama_buku, tanggal, SUM(jumlah) AS jumlah FROM fact_peminjaman_bulan INNER JOIN dim_buku ON fact_peminjaman_bulan.`id_dimBuku`=dim_buku.`id` INNER JOIN dim_perpustakaan ON fact_peminjaman_bulan.`id_dimPerpustakaan`=dim_perpustakaan.`id` WHERE nama_buku = '" +
                        buku[
                            0] + "' AND tahun = '" + value_tahun + "' AND nama_perpustakaan = '" + value_perpus + "' AND bulan = '" + value_bulan + "' GROUP BY tanggal")
            row_val = self.queries_etl.get_row_column(query_val)
            # print("isi", row_val)
            total_buku = 0
            for j, item in enumerate(row_val):
                # print(item[1])
                for k in range(0, batas - 1):
                    if item[1] == array_tanggal[k]:
                        arr_value[k] = item[2]
                        total_buku = total_buku + arr_value[k]
                    if item[1] == total_data_buku[k][0]:
                        total_data_buku[k][1] = total_data_buku[k][1] + item[2]

            arr_value.append(total_buku)
            # print(arr_value)
            for l in range(0, batas):
                self.tableWidget_5.setItem(i, l, QtWidgets.QTableWidgetItem(str(arr_value[l])))
        total_buku = 0
        for y in range(batas - 1):
            total_buku = total_buku + total_data_buku[y][1]
        total_data_buku.append([str(batas), total_buku])
        for x in range(batas):
            self.tableWidget_5.setItem(len(row_book), x, QtWidgets.QTableWidgetItem(str(total_data_buku[x][1])))

    def refreshData(self):
        for i in range(0, 100):
            self.tableWidget.removeRow(0)
        self.loadData()

    def resetWarehouse(self):
        self.queries_etl.resetWarehouse()
        self.loadData()


import book_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
