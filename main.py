from cgitb import text
from turtle import st
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp
from numpy import size
from kivy.properties import StringProperty, BooleanProperty

class MainWidget(Widget):
    pass

class WidgetExemple(GridLayout):
    mon_texte = StringProperty("0")
    #slider_value_txt = StringProperty("Valeur")
    compteur_actif = BooleanProperty(False)
    compteur = 1
    
    def on_button_click(self):
        print("Button click")
        if self.compteur_actif:
            self.mon_texte = str(self.compteur)
            self.compteur += 1
    def on_toggle_button_state(self, widget):
        #print("Toggle state: " + widget.state)
        if widget.state == "normal":
            print("OFF")
            widget.text = "OFF"
            self.compteur_actif = False
        else:
            print("ON")
            widget.text = "ON"
            self.compteur_actif = True
    def on_switch_active(self, widget):
        print("Switch: "+ str(widget.active))
    #def on_value_slider(self, widget):
    #    print("The value is:" +str(int(widget.value)))
        #self.slider_value_txt = str(int(widget.value))
            

class GridLayoutExemple(GridLayout):
    pass

class StackLayoutExemple(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "lr-tb"
        for i in range(40):
            b = Button(text=str(i+1), size_hint=(None, None), size=(dp(60),dp(60)))
            self.add_widget(b)

class BoxLayoutExemple(BoxLayout):
    """def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text='A')
        b2 = Button(text="B")
        b3 = Button(text="C")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)"""
    pass


class LelabApp(App):
    pass

LelabApp().run()