from tkinter import *
import tkinter as tk
import tkinter

def pr_1():
    """
    przyklad wyswietla proste okno o tytule Welcome to LikeGeeks.app
    Zmienilem tytul okna 
    """
    win = Tk()
    win.title("Zmodyfikowany przyklad 1")
    win.mainloop()
def pr_2():
    """
    przyklad wyswietla proste okno z etykieta 
    Dodalem dwie etykiety i zmienilem tytul okna
    """
    window = Tk()
    window.title("Zmodyfikowany przyklad 2")
    lbl = Label(window, text="Megumin")
    lbl2 = Label(window, text="Aqua")
    lbl3 = Label(window, text="Darknese")
    lbl.grid(column=0 , row=0)
    lbl2.grid(column=0, row=1)
    lbl3.grid(column=0, row=2)
    window.mainloop()

def pr_3():
    """
    przyklad tworzony proste okno z etykieta i polem tekstowym 
    Dodalem dodatkowe etykiete i pole tekstowe
    """
    window = tk.Tk()
    label = tk.Label(text="Name")
    label2 = tk.Label(text="surname")
    entry = tk.Entry()
    entry2 = tk.Entry()
    label.pack()
    entry.pack()
    label2.pack()
    entry2.pack()
    name = entry.get()
    surname = entry2.get()
    window.mainloop()

def pr_4():
    """
    przyklad tworzy okno do ktorego jest przypisywana ramka
    Dodalem dodatkowo ramke
    """
    window = tk.Tk()
    frame = tk.Frame()
    frame2 = tk.Frame()
    frame.pack()
    frame2.pack()
    window.mainloop()

def pr_5():
    """
    przyklad tworzy okno z dwa ramkami . W kazdej ramce znajduje sie etykieta
    .Dodalem ramek i dwie etykiety w niej 
    """
    window = tk.Tk()
    frame_a = tk.Frame()
    frame_b = tk.Frame()
    frame_c = tk.Frame()
    label_a = tk.Label(master=frame_a, text="Emilia")
    label_a.pack()
    label_b = tk.Label(master=frame_b, text="Subaru")
    label_b.pack()
    label_c = tk.Label(master=frame_c, text="Ram")
    label_d = tk.Label(master=frame_c, text="Rem")
    label_c.pack()
    label_d.pack()
    frame_a.pack()
    frame_b.pack()
    frame_c.pack()
    window.mainloop()

def pr_6():
    """
    przyklad tworzy okno wraz z ramka ktore jest modifikowane przez atrybut relief
    Dodalem kolejna taka ramke
    """
    border_effects = {  
            "flat": tk.FLAT, 
            "sunken": tk.SUNKEN,
            "raised": tk.RAISED, 
            "groove": tk.GROOVE, 
            "ridge": tk.RIDGE,
    }
    window = tk.Tk()
    for relief_name, relief in border_effects.items(): 
        frame = tk.Frame(master=window, relief=relief, borderwidth=5) 
        frame.pack(side=tk.LEFT) 
        label = tk.Label(master=frame, text=relief_name)  
        label.pack()
    for relief_name, relief in border_effects.items(): 
        frame2 = tk.Frame(master=window, relief=relief, borderwidth=5) 
        frame2.pack(side=tk.LEFT) 
        label2 = tk.Label(master=frame2, text=relief_name)  
        label2.pack()
    window.mainloop()

def pr_7():
    """
    przyklad tworzy okno z czterome przyciskami .Kazdy przycisk ma inny kolor napisu. Przyciski 1 i 2 sa 
    ustawione pionowo a  przyciski  3 i 4 poziomo .
    Dodalem dwa przyciski
    """
    window = tkinter.Tk()
    window.title("GUI")
    top_frame = tkinter.Frame(window).pack()
    bottom_frame = tkinter.Frame(window).pack(side = "bottom")
    btn1 = tkinter.Button(top_frame, text = "Chika", fg = "red").pack() 
    btn2 = tkinter.Button(top_frame, text = "Beatrice", fg = "green").pack()
    btn3 = tkinter.Button(bottom_frame, text = "Kuroko", fg = "purple").pack(side ="left")
    btn4 = tkinter.Button(bottom_frame, text = "Rimuru", fg = "orange").pack(side ="left")
    btn5 = tkinter.Button(bottom_frame, text = "Tanya", fg = "yellow").pack(side ="right")
    btn6 = tkinter.Button(bottom_frame, text = "Shalltear", fg = "brown").pack(side ="right")
    window.mainloop()

def pr_8():
    """
    przyklad tworzy okno potem tworzy trzy ramki o roznych rozmiarach a na koncu wypelnia poszczegolne ramki
    podanym kolorem 
    Dodalem dwie ramki
    """
    window = tk.Tk()
    frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
    frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    frame2 = tk.Frame(master=window, width=100, bg="yellow")
    frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    frame3 = tk.Frame(master=window, width=50, bg="blue")
    frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    frame4 = tk.Frame(master=window, width=125, bg="brown")
    frame4.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)
    frame5 = tk.Frame(master=window, width=175, bg="orange")
    frame5.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)
    window.mainloop()

def pr_9():
    """
    przyklad tworzy okno z dwa checkbox
    Dodalem checkbox
    """
    top = tkinter.Tk()
    CheckVar1 = IntVar()
    CheckVar2 = IntVar()
    CheckVar3 = IntVar()
    tkinter.Checkbutton(top, text = "ZSRR",variable = CheckVar1,onvalue = 1, offvalue=0).grid(
            row=0,sticky=W)
    tkinter.Checkbutton(top, text = "USA", variable = CheckVar2, onvalue =0, offvalue =1).grid(
            row=1,sticky=W)
    tkinter.Checkbutton(top, text=  "KRLD", variable = CheckVar3, onvalue=0, offvalue=0).grid(
            row=3, sticky=W
            )
    top.mainloop()

def pr_10():
    """
    przyklad tworzy okno wraz z 9 etykietami .Tekst etykiet okresla numer rzedu i kolu mn gdzie jest 
    rozmieszczona etykieta
    Dodalem tytyl okna i  zwiekszylem liczbe etykiet
    """
    window = tk.Tk()
    window.title("przyklad 10")
    for i in range(4):   
        for j in range(4):
            frame = tk.Frame(       
                    master=window,   
                    relief=tk.RAISED,  
                    borderwidth=1 
            )       
            frame.grid(row=i, column=j, padx=6, pady=6)   
            label = tk.Label(master=frame, text="Row {0}\nColumn {1}".format(i,j))      
            label.pack(padx=6, pady=6)
    window.mainloop()

def pr_11():
    """
    przyklad tworzy okno wraz z ramka .Wewnatrz ramki znajduja sie dwie etykiety ktore sa rozmieszczone
    w roznych miejscach i dodatkowo maja inne .Kazda z etykiety ma inny kolor
    Dodalem tytul okna i dwie etykiety 
    """
    window = tk.Tk()
    window.title("przyklad 11")
    frame = tk.Frame(master=window, width=150, height=150)
    frame.pack()
    label1 = tk.Label(master=frame, text="Janusz ", bg="red")
    label1.place(x=0, y=0)
    label2 = tk.Label(master=frame, text="Korwin", bg="yellow")
    label2.place(x=75, y=75)
    label3 = tk.Label(master=frame , text="Szyderczy", bg="purple")
    label3.place(x=50, y=100)
    label4 = tk.Label(master=frame, text="Skrot", bg="blue")
    label4.place(x=20, y=20)
    window.mainloop()

def pr_12():
    """
    pzyklad tworzy okno o nazwie GUI wraz z przyciskiem . Przycisk po kliknieciu tworzy etykiete z napisem
    Gui with Tkinter
    Dodalem przycisk i oblugiwana funkcje przez niego
    """
    window = tkinter.Tk()
    window.title("GUI")
    def Tutorial():   
        tkinter.Label(window, text = "TAK").pack()
    tkinter.Button(window, text = "Click Me!", command = Tutorial).pack()
    def Tutorial2():
        tkinter.Label(window, text= "Nie").pack()
    tkinter.Button(window, text= "Click Me too", command=Tutorial2).pack()
    window.mainloop()

def pr_13():
    """
    przyklad tworzy okno ktore po kliknieciu dowolnego przycisku myszy tworzy etykiete o tekscie
    mowiacym jakim przyciskiem myszy kliknieto  okno
    Dodalem funkcjonalnosc po wcisnieciu klawiszy ctrl+a tworzono jest etykieta z odpowiednim komunikatem 
    """
    window = tkinter.Tk()
    window.title("GUI")
    def left_click(event): 
        tkinter.Label(window, text = "Left Click!").pack()
    def middle_click(event): 
        tkinter.Label(window, text = "Middle Click!").pack()
    def right_click(event): 
        tkinter.Label(window, text = "Right Click!").pack()
    def control(event):
        tkinter.Label(window, text= "Janusz hahaha").pack()
    window.bind("<Button-1>", left_click)
    window.bind("<Button-2>", middle_click)
    window.bind("<Button-3>", right_click)
    window.bind("<Control-a>", control)
    window.mainloop()

def main():
    pr_1()
    pr_2()
    pr_3()
    pr_4()
    pr_5()
    pr_6()
    pr_7()
    pr_8()
    pr_9()
    pr_10()
    pr_11()
    pr_12()
    pr_13()

main()
