# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole


class Pulsator(Black_Hole):
    max_count = 30
    def __init__(self, x, y):
        Black_Hole.__init__(self, x, y)
        self.count = 0
        self._x = x
        self._y = y
        
    def update(self, model):
        result = Black_Hole.update(self, model)
        size = len(result)
        self.count += 1
            
        if size > 0:
            self.change_dimension(size, size)
            self.count = 0
              
        elif self.count == Pulsator.max_count:
            self.change_dimension(-1, -1)
            self.count = 0
            if self.get_dimension()[0] == 0 and self.get_dimension()[1] == 0:
                model.remove(self)
        return result
            
            