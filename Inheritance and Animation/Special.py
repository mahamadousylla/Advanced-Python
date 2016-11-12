#Special is a prey



from prey import Prey


class Special(Prey):
    radius = 8
    def __init__(self, x, y):
        Prey.__init__(self, x, y, 10, 10, None, 5)
        self.randomize_angle()
        self._x = x
        self._y = y
        
    def update(self, model):
        self.move()
        self.wall_bounce()
        self.set_speed(50)
        
        
    def display(self, canvas):
        canvas.create_oval(self._x-Special.radius, self._y-Special.radius,
                                self._x+Special.radius, self._y+Special.radius,
                                fill='green')