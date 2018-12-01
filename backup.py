# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview
from database import *
from queries_etl import *

###########################################################################
## Class MainFrame
###########################################################################

#
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
mysql_check_peminjaman =('''
                    SELECT * FROM history_etl WHERE id_tabel = 7
                    ORDER BY id DESC LIMIT 1
''')

show_data_tabel_etl = ('''SELECT nama_tabel, start_row, end_row, `status`, tgl_proses FROM history_etl
INNER JOIN tb_tabel ON history_etl.`id_tabel` = tb_tabel.`id`
ORDER BY history_etl.`id` ASC''')


#
class MainFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Data Warehouse", pos=wx.DefaultPosition,
                          size=wx.Size(1107, 640), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_notebook = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_panel_database = wx.Panel(self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                         wx.TAB_TRAVERSAL)
        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticTextJudul = wx.StaticText(self.m_panel_database, wx.ID_ANY, u"PERPUSTAKAAN", wx.DefaultPosition,
                                               wx.Size(-1, 80), 0)
        self.m_staticTextJudul.Wrap(-1)
        self.m_staticTextJudul.SetFont(wx.Font(18, 70, 90, 90, False, "Roboto Bk"))

        bSizer2.Add(self.m_staticTextJudul, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        gSizer1 = wx.GridSizer(1, 2, 0, 0)

        gSizer2 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText3 = wx.StaticText(self.m_panel_database, wx.ID_ANY, u"Database :", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        gSizer2.Add(self.m_staticText3, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_textCtrl4 = wx.TextCtrl(self.m_panel_database, wx.ID_ANY, u"Perpustakaan", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        gSizer2.Add(self.m_textCtrl4, 0, wx.ALL, 5)

        gSizer1.Add(gSizer2, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gSizer4 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText41 = wx.StaticText(self.m_panel_database, wx.ID_ANY, u"Database :", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText41.Wrap(-1)
        gSizer4.Add(self.m_staticText41, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_textCtrl5 = wx.TextCtrl(self.m_panel_database, wx.ID_ANY, u"warehouse", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        gSizer4.Add(self.m_textCtrl5, 0, wx.ALL, 5)

        gSizer1.Add(gSizer4, 1, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer2.Add(gSizer1, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)
        # datate = [1, "tet", "tet", "tet", "tet", "tet"]

        self.m_dataViewListCtrl1 = wx.dataview.DataViewListCtrl(self.m_panel_database, wx.ID_ANY, wx.DefaultPosition,
                                                                wx.Size(800, 300), 0)
        self.m_dataViewListColumnNo = self.m_dataViewListCtrl1.AppendTextColumn(u"No")
        self.m_dataViewListColumnTabel = self.m_dataViewListCtrl1.AppendTextColumn(u"Tabel")
        self.m_dataViewListColumnStart = self.m_dataViewListCtrl1.AppendTextColumn(u"Start Row")
        self.m_dataViewListColumnEnd = self.m_dataViewListCtrl1.AppendTextColumn(u"End Row")
        self.m_dataViewListColumnStatus = self.m_dataViewListCtrl1.AppendTextColumn(u"Status")
        self.m_dataViewListColumnDate = self.m_dataViewListCtrl1.AppendTextColumn(u"Tanggal Proses")
        bSizer2.Add(self.m_dataViewListCtrl1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        # self.m_dataViewListCtrl1.AppendItem(datate)

        self.m_buttonExtract = wx.Button(self.m_panel_database, wx.ID_ANY, u"Extract", wx.DefaultPosition,
                                         wx.Size(180, 50), 0)
        self.m_buttonExtract.SetFont(wx.Font(12, 74, 90, 90, False, "Arial"))
        self.m_buttonExtract.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
        self.m_buttonExtract.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        bSizer2.Add(self.m_buttonExtract, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticTextOuput = wx.StaticText(self.m_panel_database, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.m_staticTextOuput.Wrap(-1)
        bSizer2.Add(self.m_staticTextOuput, 0, wx.ALL, 5)

        self.m_panel_database.SetSizer(bSizer2)
        self.m_panel_database.Layout()
        bSizer2.Fit(self.m_panel_database)
        self.m_notebook.AddPage(self.m_panel_database, u"Database", True)
        self.m_panel_dwh = wx.Panel(self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel_dwh.SetFont(wx.Font(16, 70, 90, 90, False, "Roboto Bk"))

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText6 = wx.StaticText(self.m_panel_dwh, wx.ID_ANY, u"Data Warehouse", wx.DefaultPosition,
                                           wx.Size(-1, 100), 0)
        self.m_staticText6.Wrap(-1)
        bSizer6.Add(self.m_staticText6, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gSizer5 = wx.GridSizer(0, 2, 0, 0)

        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        m_comboBox2Choices = []
        self.m_comboBox2 = wx.ComboBox(self.m_panel_dwh, wx.ID_ANY, u"Pilih Perpustakaan\n", wx.DefaultPosition,
                                       wx.Size(200, 120), m_comboBox2Choices, 0)
        self.m_comboBox2.SetFont(wx.Font(11, 74, 90, 90, False, "Arial Rounded MT Bold"))

        bSizer8.Add(self.m_comboBox2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        m_comboBox21Choices = []
        self.m_comboBox21 = wx.ComboBox(self.m_panel_dwh, wx.ID_ANY, u"Pilih Tahun\n", wx.DefaultPosition,
                                        wx.Size(200, -1), m_comboBox21Choices, 0)
        self.m_comboBox21.SetFont(wx.Font(11, 74, 90, 90, False, "Arial Rounded MT Bold"))

        bSizer8.Add(self.m_comboBox21, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gSizer5.Add(bSizer8, 0, wx.EXPAND, 5)

        bSizer11 = wx.BoxSizer(wx.VERTICAL)

        self.m_dataViewListCtrl2 = wx.dataview.DataViewListCtrl(self.m_panel_dwh, wx.ID_ANY, wx.DefaultPosition,
                                                                wx.Size(520, 400), 0)
        self.m_dataViewListCtrl2.SetFont(wx.Font(12, 74, 90, 90, False, "Arial Rounded MT Bold"))

        self.m_dataViewListColumn11 = self.m_dataViewListCtrl2.AppendTextColumn(u"No")
        self.m_dataViewListColumn111 = self.m_dataViewListCtrl2.AppendTextColumn(u"No")
        self.m_dataViewListColumn112 = self.m_dataViewListCtrl2.AppendTextColumn(u"No")
        self.m_dataViewListColumn113 = self.m_dataViewListCtrl2.AppendTextColumn(u"No")
        bSizer11.Add(self.m_dataViewListCtrl2, 0, wx.ALL, 5)


        gSizer5.Add(bSizer11, 1, wx.EXPAND, 5)

        bSizer6.Add(gSizer5, 1, 0, 5)

        bSizer3.Add(bSizer6, 1, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel_dwh.SetSizer(bSizer3)
        self.m_panel_dwh.Layout()
        bSizer3.Fit(self.m_panel_dwh)
        self.m_notebook.AddPage(self.m_panel_dwh, u"DWH", False)

        bSizer1.Add(self.m_notebook, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        self.queries_etl = query()

        self.m_buttonExtract.Bind(wx.EVT_BUTTON, self.menuUtama)

    def __del__(self):
        pass

    def menuUtama(self, event):
        self.queries_etl.check_member(mysql_check_member)
        self.queries_etl.check_buku(mysql_check_buku)
        self.queries_etl.check_cabang_perpustakaan(mysql_check_perpustakaan)
        self.queries_etl.check_fact_peminjaman_bulan(mysql_check_peminjaman)

        historis = self.queries_etl.show_etl(show_data_tabel_etl)
        for x , item in enumerate(historis, start=1):
            list_item = list(item)
            list_item.insert(0,x)
            print(list_item)
            self.m_dataViewListCtrl1.AppendItem(list_item)

app = wx.App(False)
frame = MainFrame(None)
frame.Show(True)
app.MainLoop()