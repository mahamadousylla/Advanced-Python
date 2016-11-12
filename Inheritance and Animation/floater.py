# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


# from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey):
    radius = 5
    def __init__(self, x, y):
        Prey.__init__(self, x, y, 10, 10, None, 5)
        self.randomize_angle()
        self._x = x
        self._y = y
        self.width = 10
        self.height = 10
        
    def update(self, model):
        percentage = random()*100
        if percentage <= 30.0:
            r = random() - 0.3
            maximum = max(self.get_speed() + r, 3)
            lowest = min(maximum, 7)
            self.set_velocity(lowest, self.get_angle() + r)
        self.move()
        self.wall_bounce()
        
    def display(self, canvas):
        canvas.create_oval(self._x-Floater.radius, self._y-Floater.radius,
                                self._x+Floater.radius, self._y+Floater.radius,
                                fill='red')