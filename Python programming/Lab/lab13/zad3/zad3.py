from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols =1
    
        self.inside = GridLayout()

        self.inside.cols = 2
        self.inside.add_widget(Label(text="Imie: ", color='#00FF00'))
        self.imie = TextInput(multiline=False, padding_y=(20,20))  
        self.inside.add_widget(self.imie)

        self.inside.add_widget(Label(text="Nazwisko: ", color='#00FF00'))
        self.nazwisko = TextInput(multiline=False, padding_y=(20,20))  
        self.inside.add_widget(self.nazwisko)
        
        self.inside.add_widget(Label(text="Telefon: ", color='#00FF00'))
        self.tel = TextInput(multiline=False, padding_y=(20,20))  
        self.inside.add_widget(self.tel)

        self.inside.add_widget(Label(text="Miejscowosc: ", color='#00FF00'))
        self.miej = TextInput(multiline=False, padding_y=(20,20))  
        self.inside.add_widget(self.miej)
        
        self.inside.add_widget(Label(text="Wojewodztwo: ", color='#00FF00'))
        self.woj = TextInput(multiline=False, padding_y=(20,20))  
        self.inside.add_widget(self.woj)

        self.inside.add_widget(Label(text="Szczepionka: ", color='#00FF00'))
        self.rodz = TextInput(multiline=False, padding_y=(20,20))  
        self.inside.add_widget(self.rodz)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=20)
        self.submit.bind(on_press=self.zgloszono)
        self.add_widget(self.submit)

    def zgloszono(self, instance):
            imie = self.imie.text
            nazwisko = self.nazwisko.text
            woj = self.woj.text
            tel = self.tel.text
            rodz = self.rodz.text
            miej = self.miej.text
            
            if imie and nazwisko and woj and tel and rodz and miej:
                print("zgloszono ", imie, nazwisko, tel, woj, miej, rodz)
            else:
                print("nie wypelniles wszystkich pol")

class MyApp(App):
    def build(self):
        self.title = 'Aplikacje do zapisu na szczepienia'
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()
