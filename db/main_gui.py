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
import wx.grid
from queries_etl import *

###########################################################################
## Class MainFrame
###########################################################################


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

        self.m_dataViewListCtrl1 = wx.dataview.DataViewListCtrl(self.m_panel_database, wx.ID_ANY, wx.DefaultPosition,
                                                                wx.Size(800, 300), 0)
        self.m_dataViewListColumnNo = self.m_dataViewListCtrl1.AppendTextColumn(u"No")
        self.m_dataViewListColumnTabel = self.m_dataViewListCtrl1.AppendTextColumn(u"Tabel")
        self.m_dataViewListColumnStart = self.m_dataViewListCtrl1.AppendTextColumn(u"Start Row")
        self.m_dataViewListColumnEnd = self.m_dataViewListCtrl1.AppendTextColumn(u"End Row")
        self.m_dataViewListColumnStatus = self.m_dataViewListCtrl1.AppendTextColumn(u"Status")
        self.m_dataViewListColumnDate = self.m_dataViewListCtrl1.AppendTextColumn(u"Tanggal Proses")
        bSizer2.Add(self.m_dataViewListCtrl1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

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
        self.m_notebook.AddPage(self.m_panel_database, u"Database", False)
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

        m_comboBox22Choices = [u"deva", u"agus", u"anang"]
        self.m_comboBox22 = wx.ComboBox(self.m_panel_dwh, wx.ID_ANY, u"Pilih Member\n", wx.DefaultPosition,
                                        wx.Size(200, 120), m_comboBox22Choices, 0)
        self.m_comboBox22.SetFont(wx.Font(11, 74, 90, 90, False, "Arial Rounded MT Bold"))

        bSizer8.Add(self.m_comboBox22, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        m_comboBox221Choices = []
        self.m_comboBox221 = wx.ComboBox(self.m_panel_dwh, wx.ID_ANY, u"Pilih Tahun", wx.DefaultPosition,
                                         wx.Size(200, 120), m_comboBox221Choices, 0)
        self.m_comboBox221.SetFont(wx.Font(11, 74, 90, 90, False, "Arial Rounded MT Bold"))

        bSizer8.Add(self.m_comboBox221, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button5 = wx.Button(self.m_panel_dwh, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button5.SetFont(wx.Font(9, 74, 90, 90, False, "Arial"))

        bSizer8.Add(self.m_button5, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gSizer5.Add(bSizer8, 0, wx.EXPAND, 5)

        bSizer11 = wx.BoxSizer(wx.VERTICAL)

        self.m_grid3 = wx.grid.Grid(self.m_panel_dwh, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid3.CreateGrid(0, 0)
        self.m_grid3.EnableEditing(True)
        self.m_grid3.EnableGridLines(True)
        self.m_grid3.EnableDragGridSize(False)
        self.m_grid3.SetMargins(0, 0)

        # Columns
        self.m_grid3.EnableDragColMove(False)
        self.m_grid3.EnableDragColSize(True)
        self.m_grid3.SetColLabelSize(30)
        self.m_grid3.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.m_grid3.EnableDragRowSize(True)
        self.m_grid3.SetRowLabelSize(80)
        self.m_grid3.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.m_grid3.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer11.Add(self.m_grid3, 0, wx.ALL, 5)

        gSizer5.Add(bSizer11, 1, wx.EXPAND, 5)

        bSizer6.Add(gSizer5, 1, 0, 5)

        bSizer3.Add(bSizer6, 1, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel_dwh.SetSizer(bSizer3)
        self.m_panel_dwh.Layout()
        bSizer3.Fit(self.m_panel_dwh)
        self.m_notebook.AddPage(self.m_panel_dwh, u"DWH", True)

        bSizer1.Add(self.m_notebook, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)
        self.queries_etl = query()

        self.m_button5.Bind(wx.EVT_BUTTON, self.loadData)



    def __del__(self):
        pass

    def loadData(self,event):
        member = self.m_comboBox22.GetStringSelection()
        get_book_name = ("SELECT nama_buku FROM dim_member INNER JOIN fact_peminjaman_bulan ON dim_member.`id` = fact_peminjaman_bulan.`id_dimMember` INNER JOIN dim_buku ON fact_peminjaman_bulan.`id_dimBuku` = dim_buku.`id` WHERE nama_member = '"+member+"' AND tahun = '2018' GROUP BY nama_buku;")
        column_name = self.queries_etl.get_row_column(get_book_name)

        get_month = ("SELECT bulan FROM dim_member INNER JOIN fact_peminjaman_bulan ON dim_member.`id` = fact_peminjaman_bulan.`id_dimMember` INNER JOIN dim_buku ON fact_peminjaman_bulan.`id_dimBuku` = dim_buku.`id` WHERE nama_member = '"+member+"' AND tahun = '2018' GROUP BY bulan;")
        row_name = self.queries_etl.get_row_column(get_month)

        length_column = len(column_name)
        length_row = len(row_name)


        for x , item in enumerate(column_name):
            self.m_grid3.AppendCols(1)
            list_book = list(item)
            list_book.insert(0,x)
            print(list_book[1])
            # self.m_grid3.ClearGrid()
            self.m_grid3.SetColLabelValue(x,list_book[1])

        for x , item in enumerate(row_name):
            self.m_grid3.AppendRows(x)
            list_item = list(item)
            list_item.insert(0,x)
            print(list_item[1])
            # self.m_grid3.ClearGrid()
            self.m_grid3.SetRowLabelValue(x,list_item[1])

app = wx.App(False)
frame = MainFrame(None)
frame.Show(True)
app.MainLoop()
