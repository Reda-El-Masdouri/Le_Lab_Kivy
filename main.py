from cgitb import text
from turtle import st
from git import Object
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp
from numpy import size
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty
from canvas_exemple import *
from navigation_screen_manager import NavigationScreenManager

     
class MyScreenManager(NavigationScreenManager):
    pass
class MenuPrincipal(BoxLayout):
    pass

class LelabApp(App):
    manager = ObjectProperty(None)
    def build(self):
        self.manager = MyScreenManager()
        #return self.manager
        return CanvasExemple3()


LelabApp().run()