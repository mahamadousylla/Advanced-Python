# A Hunter is both a Mobile_Simulton and Pulsator: it updates
#   like a Pulsator, but it moves (either in a straight line
#   or in pursuit of Prey) and displays as a Pulsator.


from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from prey import Prey
from math import atan2


class Hunter(Pulsator,Mobile_Simulton):
    the_distance = 200
    
    def __init__(self, x, y):
        Pulsator.__init__(self, x, y)
        Mobile_Simulton.__init__(self, x, y, self.get_dimension()[0], self.get_dimension()[1], None, 5)
        self.randomize_angle()
        self._x = x
        self._y = y
        
    def update(self, model):
        alist = [ ]
        settt = Pulsator.update(self, model)
        result = model.find(lambda x: isinstance(x, Prey) and self.distance(x.get_location()) <= Hunter.the_distance)
        if len(result) > 0:
            for i in result:
                x = (self.distance(i.get_location()), i)
                alist.append(x)
            lowest = min(alist)
            self.set_angle(atan2(lowest[1].get_location()[1]-self.get_location()[1], lowest[1].get_location()[0]-self.get_location()[0]))
        self.move()
        return settt
    