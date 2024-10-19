#!/usr/bin/env python3
import wx
def example1():
    """
    przyklad tworzy proste okno z tytulem Hello World
    Zmienilem tytul
    """
    app = wx.App()
    frame = wx.Frame(parent=None, title='Przyklad 1')
    frame.Show()
    app.MainLoop()

def example2():
    """
    przyklad tworzy proste okno o rozmiarze 640x480 i tytulem Hello  World 
    Zmienilem rozmiar okna i jego polozenie 
    """
    app = wx.App()
    frame = wx.Frame(parent=None, title='przyklad 2')
    frame.SetDimensions(0,0,1000,800)
    frame.Show()
    app.MainLoop()

def example3():
    """
    przyklad  tworzy proste okno za pomoca wlasnej klasy MyFrame
    Zmienilem rozmiar okna
    """
    class MyFrame(wx.Frame):     
        def __init__(self):  
            super().__init__(parent=None, title='Przklad 3')
            self.SetDimensions(0,0,500,200)
            self.Show()
    app = wx.App()   
    frame = MyFrame() 
    app.MainLoop()

def example4():
    """
    przyklad tworzy proste okno z polem tekstowym i przyciskiem
    Dodalem dwa pole tekstowe i zmienilem rozmiar okna
    """
    class MyFrame(wx.Frame): 
       def __init__(self):
            super().__init__(parent=None, title='przyklad 4') 
            self.SetDimensions(0,0,300,200)
            panel = wx.Panel(self)  
            self.text_ctrl = wx.TextCtrl(panel, pos=(5, 1))  
            self.text_ctrl2 = wx.TextCtrl(panel, pos=(5,40))
            self.text_ctrl3 = wx.TextCtrl(panel, pos=(5,80))
            my_btn = wx.Button(panel, label='Press Me', pos=(5, 120))   
            self.Show()
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()


def example5():
    """
    przyklad tworzy proste okno z przyciskiem ktory po kliknieciu wyswietla napis w terminalu
    Dodalem przycisk z funkcja ktore wykonuje po wcisnieciu
    """
    def onButton(event):  
        print ("Nie")
    def button_2(event):
        print("Tak")
    app = wx.App()
    frame = wx.Frame(None, -1, 'win.py')
    frame.SetSize(0,0,200,200)
    panel = wx.Panel(frame, wx.ID_ANY)
    button = wx.Button(panel, wx.ID_ANY, 'przycisk1', (10, 10))
    button.Bind(wx.EVT_BUTTON, onButton)
    button2 = wx.Button(panel, wx.ID_ANY, 'przycisk2', (10, 50))
    button2.Bind(wx.EVT_BUTTON, button_2)
    frame.Show()
    frame.Centre()
    app.MainLoop()

def example6():
    """
    przyklad tworzy proste okno z polem i przyciskiem ktory po kliknieciu 
    wyswietla napis wraz z rozmiarem pola w terminalu i przypisuje wartosc do pola
    Dodalem  przycisk 
    """
    class MyFrame(wx.Frame):
        def __init__(self):
            super().__init__(parent=None, title='Hello World')  
            panel = wx.Panel(self)
            self.text_ctrl = wx.TextCtrl(panel, pos=(5, 5),size=(200, 33)) 
            self.my_btn = wx.Button(panel, label='Press Me', pos=(5, 100)) 
            self.my_btn = wx.Button(panel, label='WWW', pos=(5, 150)) 

            def onButton(event):  
                print ("Button pressed") 
                print (self.text_ctrl.GetSize())      
                self.text_ctrl.AppendText("Button pressed\n")   
            self.my_btn.Bind(wx.EVT_BUTTON, onButton)  
            self.Show()
    if __name__ == '__main__':
        app = wx.App()
        frame = MyFrame()  
        app.MainLoop()

def example7():
    """
    przyklad tworzy okno z kontenerem BoxSizer w ktorym znajduje sie przycisk i pole tekstowe
    Dodalem przycisk
    """
    class MyFrame(wx.Frame):
        def __init__(self):    
            super().__init__(parent=None, title='Hello World') 
            panel = wx.Panel(self)   
            my_sizer = wx.BoxSizer(wx.VERTICAL)  
            self.text_ctrl = wx.TextCtrl(panel)   
            my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)
            my_btn = wx.Button(panel, label='Press Me')   
            my_btn2 = wx.Button(panel, label='Press')   
            my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)    
            my_sizer.Add(my_btn2, 0, wx.ALL | wx.CENTER, 5)    
            panel.SetSizer(my_sizer)
            self.Show()
    if __name__ == '__main__': 
        app = wx.App() 
        frame = MyFrame()      
        app.MainLoop()

def example8():
    """
    przyklad tworzy okno z wykorzystaniem kontenera BoxSizer w ktory znajduje sie dwa pola tekstowe i
    przycisk. Zawartosc z pierwszego pola tekstowego jest wprowadzana do pola drugiego po kliknieciu
    przycisku 
    Dodalem przycisk 
    """
    class MyFrame(wx.Frame):   
        def __init__(self): 
            super().__init__(parent=None, title='Hello World')
            panel = wx.Panel(self) 
            my_sizer = wx.BoxSizer(wx.VERTICAL)   
            self.text_ctrl = wx.TextCtrl(panel)    
            my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)   
            
            my_btn = wx.Button(panel, label='Press 1')   
            my_btn.Bind(wx.EVT_BUTTON, self.on_press) 
            my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)  
            self.text_ctrl_out = wx.TextCtrl(panel)  
            
            my_btn2 = wx.Button(panel, label='Press 2')   
            my_btn2.Bind(wx.EVT_BUTTON, self.on_press2) 
            my_sizer.Add(my_btn2, 0, wx.ALL | wx.CENTER, 10)  
            
            my_sizer.Add(self.text_ctrl_out, 0, wx.ALL | wx.EXPAND, 5)  
            panel.SetSizer(my_sizer)
            self.Show()  
        def on_press(self, event):   
            value = self.text_ctrl.GetValue()    
            if not value:     
                print("You didn't enter anything!") 
            else:   
                print("You typed: {}",format(value))   
                self.text_ctrl_out.AppendText(value)
        
        def on_press2(self, event):   
            value = self.text_ctrl.GetValue()    
            if not value:     
                print("Nie wprowadziles zadnch wartosc") 
            else:   
                print("Wprowadzona wartosc: {}",format(value))   
                self.text_ctrl_out.AppendText(value)
                
    if __name__ == '__main__': 
        app = wx.App()
        frame = MyFrame()   
        app.MainLoop()

def example9():
    """
    przyklad tworzy okno w ktorym znajduje sie prosta linia 
    Dodalem druga linie
    """
    class Example(wx.Frame): 
        def __init__(self, *args, **kw):   
            super(Example, self).__init__(*args, **kw)  
            self.InitUI() 
        
        def InitUI(self): 
            wx.CallLater(2000, self.DrawLine)   
            wx.CallLater(3000, self.DrawLine2)   
            self.SetTitle("Przyklad 9") 
            self.Centre()  
        
        def DrawLine(self):   
            dc = wx.ClientDC(self) 
            dc.DrawLine(50, 60, 190, 60)
        
        def DrawLine2(self):   
            dc = wx.ClientDC(self) 
            dc.DrawLine(60, 70, 200, 70)
    
    def main():  
        app = wx.App() 
        example = Example(None) 
        example.Show() 
        app.MainLoop()
    main()

def example10():
    """
    przyklad tworzy okno w ktorym znajduje sie dziewiec kwadratow o roznym kolorze
    """
    class Example(wx.Frame): 
        def __init__(self, *args, **kw):  
            super(Example, self).__init__(*args, **kw)     
            self.InitUI()   
        
        def InitUI(self):
            self.Bind(wx.EVT_PAINT, self.OnPaint)  
            self.SetTitle("Przyklad 10")  
            self.SetDimensions(0,0,400,420)
            self.Centre()  
        
        def OnPaint(self, e):  
            dc = wx.PaintDC(self)    
            dc.SetPen(wx.Pen('#d4d4d4'))    
            dc.SetBrush(wx.Brush('#c56c00'))   
            dc.DrawRectangle(10, 15, 90, 60)   
            dc.SetBrush(wx.Brush('#1ac500'))   
            dc.DrawRectangle(130, 15, 90, 60)
            dc.SetBrush(wx.Brush('#539e47'))
            dc.DrawRectangle(250, 15, 90, 60)
            dc.SetBrush(wx.Brush('#004fc5')) 
            dc.DrawRectangle(10, 105, 90, 60)
            dc.SetBrush(wx.Brush('#c50024'))
            dc.DrawRectangle(130, 105, 90, 60)
            dc.SetBrush(wx.Brush('#9e4757'))
            dc.DrawRectangle(250, 105, 90, 60)
            dc.SetBrush(wx.Brush('#5f3b00'))
            dc.DrawRectangle(10, 195, 90, 60)
            dc.SetBrush(wx.Brush('#4c4c4c'))
            dc.DrawRectangle(130, 195, 90, 60) 
            dc.SetBrush(wx.Brush('#785f36')) 
            dc.DrawRectangle(250, 195, 90, 60)
            dc.SetBrush(wx.Brush('#785f77')) 
            dc.DrawRectangle(250, 275, 90, 60)
            dc.SetBrush(wx.Brush('#805f33')) 
            dc.DrawRectangle(10, 275, 90, 60)
            dc.SetBrush(wx.Brush('#781f36')) 
            dc.DrawRectangle(130, 275, 90, 60)
    
    def main():
        app = wx.App() 
        ex = Example(None) 
        ex.Show()
        app.MainLoop()
    if __name__ == '__main__': 
        main()

def example11():
    """
    przyklad tworzy okno w ktorym znajduje sie kolo o kolorze czerwonym , linie i kwadrat  
    Dodalem drugi kwadraw
    """
    class Mywin(wx.Frame): 
       def __init__(self, parent, title):  
           super(Mywin, self).__init__(parent, title = title,size = (500,300))  
           self.InitUI() 
       def InitUI(self):
            self.Bind(wx.EVT_PAINT, self.OnPaint)  
            self.Centre() 
            self.Show(True)  

       def OnPaint(self, e):  
            dc = wx.PaintDC(self) 
            brush = wx.Brush("white")
            dc.SetBackground(brush)
            dc.Clear()   
            #dc.DrawBitmap(wx.Bitmap("python.jpg"),10,10,True) 
            color = wx.Colour(255,0,0) 
            b = wx.Brush(color) 
            dc.SetBrush(b)  
            dc.DrawCircle(300,125,50)  
            dc.SetBrush(wx.Brush(wx.Colour(255,255,255)))
            dc.DrawCircle(300,125,30)
            font = wx.Font(18, wx.ROMAN, wx.ITALIC, wx.NORMAL) 
            dc.SetFont(font)
            dc.DrawText("Hello wxPython",200,10)  
            pen = wx.Pen(wx.Colour(0,0,255))
            dc.SetPen(pen)
            dc.DrawLine(200,50,350,50)  
            dc.SetBrush(wx.Brush(wx.Colour(0,255,0), wx.CROSS_HATCH))  
            dc.DrawRectangle(380, 15, 90, 60) 
            dc.SetBrush(wx.Brush('#781f36')) 
            dc.DrawRectangle(130, 30, 90, 60)

    
    ex = wx.App()
    Mywin(None, 'Drawing demo')
    ex.MainLoop()

def main(): 
    example1()
    example2()
    example3()
    example4()
    example5()
    example6() 
    example7()
    example8()
    example9()
    example10()
    example11()
main()
