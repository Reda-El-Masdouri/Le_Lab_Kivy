from kivy.uix.widget import Widget
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color
from kivy.metrics import dp
from kivy.properties import Clock
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
        a, b = self.rect.size
        x, y = self.rect.pos
        inc = dp(10)
        diff = self.width - (x+a)
        if diff < inc:
            inc = diff
        x += inc
        self.rect.pos = (x, y)

class CanvasExemple5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = dp(3)
        self.vy = dp(4)
        with self.canvas:
            self.ball = Ellipse(pos=self.center, size=(self.ball_size,self.ball_size))
        Clock.schedule_interval(self.update, 1/60)

    def on_size(self, *args):
        self.ball.pos = (self.center_x - self.ball_size/2, self.center_y - self.ball_size/2)

    def update(self, dt):
        x, y = self.ball.pos
        x += self.vx
        y += self.vy
        if y + self.ball_size > self.height:
            y = self.height - self.ball_size
            self.vy = -self.vy
        elif y < 0:
            y = 0
            self.vy = -self.vy
        elif x + self.ball_size > self.width:
            x = self.width - self.ball_size
            self.vx = -self.vx
        elif x < 0:
            x = 0
            self.vx = -self.vx
        self.ball.pos = (x,y)

class CanvasExemple6(Widget):
    pass