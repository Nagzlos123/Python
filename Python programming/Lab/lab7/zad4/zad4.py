#!/usr/bin/env python
import wx
from wx import grid
import matplotlib.pyplot as plt

class WindowApp(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Aplikacja do przetwarzania danych')
        self.InitUi()
    
    def InitUi(self):
        mygrid = grid.Grid(self)
        mygrid.CreateGrid(20, 23)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(mygrid, 0, wx.ALL |  wx.EXPAND,5)
        lab_pol = wx.StaticText(self, label="Numer pola ")
        sizer.Add(lab_pol, 0, wx.ALL | wx.CENTER, 5)
        self.SetSizer(sizer)
        self.SetDimensions(0, 0, 640, 680)
        self.Centre()
        mygrid.Bind(wx.grid.EVT_GRID_SELECT_CELL, self.pojedyncza_pozycja)

    def pojedyncza_pozycja(self, event):
        print ("Wybrane pole  Row %s, Col %s" % (event.GetRow(), event.GetCol()))
        event.Skip()

    def rysuj_wykres(self):
        plt.show()

if __name__ ==  "__main__" :
    app = wx.App()
    win = WindowApp()
    win.Show()
    app.MainLoop()
