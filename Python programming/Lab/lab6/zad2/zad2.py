import future
import tkinter as tk
from tkinter import *
"""
Za pomoca biblioteki tkinter stworzylem aplikacje ktora jest sklepem mangowym 
.Program zlicza ile wszystk mang zostal kupionych. Wybor mang jest dokonowany za pomoca checkbox a liczba
sztuk jest okreslana za pomoca elementu spinbox. Wynik zakupu jest wyswietlany w nowym okienku  
"""

def configure_window():
    window.title("Maly sklep spozywczy")
    width = 720
    height= 240
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (width/2)
    y = (hs/2) - (height/2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))
    window.resizable(False, False)

def look_shop():
    lb1_number = tk.Label(window, text="amount:")
    lb1_number.grid(row=0, column=1, sticky=W)
    lb2_number = tk.Label(window, text="amount:")
    lb2_number.grid(row=1, column=1, sticky=N)
    lb3_number = tk.Label(window, text="amount:")
    lb3_number.grid(row=2, column=1, sticky=N)
    lb4_number = tk.Label(window, text="amount:")
    lb4_number.grid(row=3, column=1, sticky=N)
    lb5_number = tk.Label(window, text="amount:")
    lb5_number.grid(row=4, column=1, sticky=N)
    lb6_number = tk.Label(window, text="amount:")
    lb6_number.grid(row=5, column=1, sticky=N)
    lb7_number = tk.Label(window, text="amount:")
    lb7_number.grid(row=6, column=1, sticky=N)
    lb8_number = tk.Label(window, text="amount:")
    lb8_number.grid(row=7, column=1, sticky=N)

    number1 = IntVar()
    number2 = IntVar()
    number3 = IntVar()
    number4 = IntVar()
    number5 = IntVar()
    number6 = IntVar()
    number7 = IntVar()
    number8 = IntVar()

    field_number1 = tk.Spinbox(window, from_=number1.get(), to=10, width=5, textvariable = number1 ).grid(
            row=0, column=2, sticky=W)
    field_number2 = tk.Spinbox(window, from_=number2.get(), to=10, width=5, textvariable = number2 ).grid(
            row=1, column=2, sticky=W) 
    field_number3 = tk.Spinbox(window, from_=number3.get(), to=10, width=5, textvariable = number3 ).grid(
            row=2, column=2, sticky=W)
    field_number4 = tk.Spinbox(window, from_=number4.get(), to=10, width=5, textvariable = number4 ).grid(
            row=3, column=2, sticky=W)
    field_number5 = tk.Spinbox(window, from_=number5.get(), to=10, width=5, textvariable = number5  ).grid(
            row=4, column=2, sticky=W)
    field_number6 = tk.Spinbox(window, from_=number6.get(), to=10, width=5, textvariable = number6  ).grid(
            row=5, column=2, sticky=W)
    field_number7 = tk.Spinbox(window, from_=number7.get(), to=10, width=5, textvariable = number7  ).grid(
            row=6, column=2, sticky=W)
    field_number8 = tk.Spinbox(window, from_=number8.get(), to=10, width=5, textvariable = number8  ).grid(
            row=7, column=2, sticky=W)
    
    lbl_cena1 = tk.Label(window, text="price: 10$ ")
    lbl_cena1.grid(row=0, column=4, sticky=W)
    lbl_cena2 = tk.Label(window, text="price: 20$ ")
    lbl_cena2.grid(row=1, column=4, sticky=W)
    lbl_cena3 = tk.Label(window, text="price: 15$ ")
    lbl_cena3.grid(row=2, column=4, sticky=W)
    lbl_cena4 = tk.Label(window, text="price: 22$ ")
    lbl_cena4.grid(row=3, column=4, sticky=W)
    lbl_cena5 = tk.Label(window, text="price: 15$ ")
    lbl_cena5.grid(row=4, column=4, sticky=W)
    lbl_cena6 = tk.Label(window, text="price: 20$ ")
    lbl_cena6.grid(row=5, column=4, sticky=W)
    lbl_cena7 = tk.Label(window, text="price: 10$ ")
    lbl_cena7.grid(row=6, column=4, sticky=W)
    lbl_cena8 = tk.Label(window, text="price: 12$ ")
    lbl_cena8.grid(row=7, column=4, sticky=W)

    def choose_1():
        if CheckVar1.get() == 1:
            number1.set(1)
        else:
            number1.set(0)
    def choose_2():
        if CheckVar2.get() == 1:
            number2.set(1)
        else:
            number2.set(0)
    def choose_3():
        if CheckVar3.get() == 1:
            number3.set(1)
        else:
            number3.set(0)
    def choose_4():
        if CheckVar4.get() == 1:
            number4.set(1)
        else:
            number4.set(0)
    def choose_5():
        if CheckVar5.get() == 1:
            number5.set(1)
        else:
            number5.set(0)
    def choose_6():
        if CheckVar6.get() == 1:
            number6.set(1)
        else:
            number6.set(0)
    def choose_7():
        if CheckVar7.get() == 1:
            number7.set(1)
        else:
            number7.set(0)
    def choose_8():
        if CheckVar8.get() == 1:
            number8.set(1)
        else:
            number8.set(0)

    CheckVar1 = IntVar()
    CheckVar2 = IntVar()
    CheckVar3 = IntVar()
    CheckVar4 = IntVar()
    CheckVar5 = IntVar()
    CheckVar6 = IntVar()
    CheckVar7 = IntVar()
    CheckVar8 = IntVar()
    c1 = tk.Checkbutton(window, text="Chleb", variable=CheckVar1,
            onvalue=1, offvalue=0, command=choose_1 ).grid(row=0, column=0, sticky=W)
    c2 = tk.Checkbutton(window, text="Ser kozi", variable=CheckVar2,
            onvalue=1, offvalue=0, command=choose_2).grid(row=1, column=0, sticky=W)
    c3 = tk.Checkbutton(window, text="Pomarancze", variable=CheckVar3,
            onvalue=1, offvalue=0, command=choose_3).grid(row=2, column=0, sticky=W)
    c4 = tk.Checkbutton(window, text="Kiełbasa", variable=CheckVar4,
            onvalue=1, offvalue=0, command=choose_4).grid(row=3, column=0, sticky=W)
    c5 = tk.Checkbutton(window, text="Banany", variable=CheckVar5,
            onvalue=1, offvalue=0, command=choose_5).grid(row=4, column=0, sticky=W)
    c6 = tk.Checkbutton(window, text="Papryka", variable=CheckVar6,
            onvalue=1, offvalue=0, command=choose_6).grid(row=5, column=0, sticky=W)
    c7 = tk.Checkbutton(window, text="Masło", variable=CheckVar7,
            onvalue=1, offvalue=0, command=choose_7).grid(row=6, column=0, sticky=W)
    c8 = tk.Checkbutton(window, text="Jaja kurze", variable=CheckVar8,
            onvalue=1, offvalue=0, command=choose_8).grid(row=7, column=0, sticky=W)

    def paid():
        suma = 0 
        val1, val2, val3, val4, val5, val6, val7, val8 = 0, 0, 0, 0, 0, 0, 0, 0
        if CheckVar1.get() == 1:
            val1 = number1.get() * 10
        if CheckVar2.get() == 1:
            val2 = number2.get() * 20
        if CheckVar3.get() == 1:
            val3 = number3.get() * 15
        if CheckVar4.get() == 1:
            val4 = number4.get() * 22
        if CheckVar5.get() == 1:
            val5 = number5.get() * 15
        if CheckVar6.get() == 1:
            val6 = number6.get() * 20
        if CheckVar7.get() == 1:
            val7 = number7.get() * 10
        if CheckVar8.get() == 1:
            val8 = number8.get() * 12
        suma+= val1 + val2 + val3 + val4 + val5 + val6 + val7 + val8
        second_win = tk.Toplevel(window)
        def config_second_win():
            second_win.resizable(False, False)
            width = 180
            height= 20
            ws = second_win.winfo_screenwidth()
            hs = second_win.winfo_screenheight()
            x = (ws/2) - (width/2)
            y = (hs/2) - (height/2)
            second_win.geometry('%dx%d+%d+%d' % (width, height, x, y))
        config_second_win()
        if suma > 0: 
            lbl_spc = tk.Label(second_win, text="Twoja zakupy wynosa {}".format(suma) , bg="green" )
            lbl_spc.pack()
        else: 
            lbl_spc = tk.Label(second_win, text="Nic nie wybrales" , bg="red")
            lbl_spc.pack()

    btn1 = tk.Button(text="Kup", comm=paid)
    btn1.grid(row=8, column=0, sticky=W)

window = tk.Tk()
configure_window()
look_shop()
window.mainloop()
