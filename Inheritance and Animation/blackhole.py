# A Black_Hole is a Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    radius = 10
    
    def __init__(self, x, y):
        Simulton.__init__(self, x, y, 20, 20)
        self._x = x
        self._y = y

    def update(self, model):
        result = model.find(lambda x: isinstance(x, Prey) and self.contains(x.get_location()))
        for item in model.find(lambda x: isinstance(x, Prey) and self.contains(x.get_location())):
            model.remove(item)
        return result
    
    def display(self, canvas):
        canvas.create_oval(self._x - (self.get_dimension()[0]/2), self._y - (self.get_dimension()[1]/2),
                           self._x + (self.get_dimension()[0]/2), self._y + (self.get_dimension()[1]/2), fill='black')
        
        
    def contains(self, xy):
        w, h = self.get_dimension()
        return self.distance(xy) <= w/2  
        
        
        