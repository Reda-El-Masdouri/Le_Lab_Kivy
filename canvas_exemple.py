from kivy.uix.widget import Widget
from kivy.graphics.vertex_instructions import Line, Rectangle
from kivy.graphics.context_instructions import Color
from kivy.metrics import dp

from kivy.lang import Builder
from numpy import size

Builder.load_file("canvas_exemple.kv")


class CanvasExemple1(Widget):
    pass
class CanvasExemple2(Widget):
    pass
class CanvasExemple3(Widget):
    pass
class CanvasExemple4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100,100,400,400), width=2)
            Color(1,0,0)
            Line(circle=(50,50,50))
            Line(rectangle=(200,150,150,100), width=5)
            self.rect = Rectangle(pos=(500,300), size=(150,100))
    def on_press_button_a_click(self):
        x, y = self.rect.pos
        x += dp(10)
        self.rect.pos = (x, y)
            