from goody import type_as_str
from math import sqrt



class DimensionError(Exception):
    def __init__(self,message=None):
        Exception.__init__(self,message)


class Dimensional:
    
    def __init__(self, value, l=0, m=0, t=0):
        self.value = value
        self.l = l
        self.m = m
        self.t = t
        
        assert type(l) == int and type(m) == int and type(t) == int

    def __bool__(self):
        return self.value != 0
    
    def __len__(self):
        return abs(self.l) + abs(self.m) + abs(self.t)
        

    def __repr__(self):
        
        astring = 'Dimensional(' + str(self.value)
        if self.l != 0:
            astring += ',l=' + str(self.l)
        if self.t != 0:
            astring += ',t=' 
        astring += str(self.t) + ')'
        return astring
        
    def __str__(self):
        astring = str(self.value) + "(" + str(self.l) + ',' + str(self.m) + ',' +str(self.t) + ')'
        return astring
        
    def __getitem__(self, key):
        if key == 'value': 
            return self.value
        elif key == 'l': 
            return self.l 
        elif key == 'm': 
            return self.m 
        elif key == 't': 
            return self.t 
        elif key == 'd': 
            return self.l, self.m, self.t
        else: 
            raise KeyError
    
    def format(self, iterable):
        result = str(self.value) + ' '
        if self.l == 0 and self.m == 0 and self.t == 0: 
            return self.value
        for dim in iterable: 
            if dim == 'm' or dim == 'meter': 
                if self.l == 1: 
                    result += str(dim) + '/'
                else: 
                    if self.l < 0: 
                        result += str(dim) + '**' + str(self.l)
                    elif self.l > 0:
                        result += str(dim) + '**' + str(self.l)

            if dim == 'g' or dim == 'gram': 
                if self.m != 1 and self.m != -1:
                    if self.m > 0: 
                        result += str(dim) + '**' + str(self.m)
                    elif self.m < 0: 
                        result += str(dim) + '**' + str(abs(self.m)) + '/'
                else: 
                    if self.m < 0: 
                        result += str(dim) + '/'
                    else: 
                        result += str(dim)

            if dim == 's' or dim == 'second':
                if self.t != 1 and self.t != -1:
                    if self.t > 0: 
                        result += str(dim) + '**' + str(self.t)
                    elif self.t < 0: 
                        result += str(dim) + '**' + str(abs(self.t)) 
                else: 
                    if self.t < 0 and self.m ==0 and self.l == 0: 
                        result += str(abs(self.t)) + '/' + str(dim)
                    elif self.t < 0:
                        result += '/' + str(dim)
                    else: 
                        result += str(dim)
        return result
    
    
    def __pos__(self):      
        return Dimensional(self.value, self.l, self.m, self.t)
    
    
    def __neg__(self):
        return Dimensional(-abs(self.value), self.l, self.m, self.t)

    
    def __add__(self, right):

        if self.l == 0 and self.m == 0 and self.t == 0:
            return Dimensional((self.value + right), self.l, self.m, self.t)
        
        elif type(self) == Dimensional and type(right) == float or type(right) == int:
            raise DimensionError
        
        elif type(self) == Dimensional and type(right) != float and type(right) != int and type(right) != Dimensional:
            raise TypeError
        
        elif len(self) != len(right):
            raise DimensionError

        elif (self.l != right.l) or (self.m != right.m) or (self.t != right.t):
            return DimensionError
        
        elif (self.l == right.l) or (self.m == right.m) or (self.t == right.t):
            return Dimensional(self.value + right.value, self.l, self.m, self.t)
        


    def __radd__(self, left):
        
        if self.l == 0 and self.m == 0 and self.t == 0:
            return Dimensional((self.value + left), self.l, self.m, self.t)
         
        if type(self) == Dimensional and type(left) == float or type(left) == int:
            raise DimensionError
        
        elif type(self) == Dimensional and type(left) != float and type(left) != int and type(left) != Dimensional:
            raise TypeError
        
        elif len(self) != len(left):
            raise DimensionError
        
        elif (self.l != left.l) or (self.m != left.m) or (self.t != left.t):
            return DimensionError
        
        elif (self.l == left.l) or (self.m == left.m) or (self.t == left.t):
            return Dimensional(self.value + left.value, self.l, self.m, self.t)
        
    
    def __sub__(self, right):
        if self.l == 0 and self.m == 0 and self.t == 0:
            return Dimensional((self.value - right), self.l, self.m, self.t)
        
        elif type(self) == Dimensional and type(right) == float or type(right) == int:
            raise DimensionError
        
        elif type(self) == Dimensional and type(right) != float and type(right) != int and type(right) != Dimensional:
            raise TypeError
        
        elif len(self) != len(right):
            raise DimensionError

        elif (self.l != right.l) or (self.m != right.m) or (self.t != right.t):
            return DimensionError
        
        elif (self.l == right.l) or (self.m == right.m) or (self.t == right.t):
            return Dimensional(self.value - right.value, self.l, self.m, self.t)
        
        
    def __rsub__(self, left):
        if self.l == 0 and self.m == 0 and self.t == 0:
            return Dimensional((left - self.value), self.l, self.m, self.t)
         
        if type(self) == Dimensional and type(left) == float or type(left) == int:
            raise DimensionError
        
        elif type(self) == Dimensional and type(left) != float and type(left) != int and type(left) != Dimensional:
            raise TypeError
        
        elif len(self) != len(left):
            raise DimensionError
        
        elif (self.l != left.l) or (self.m != left.m) or (self.t != left.t):
            return DimensionError
        
        elif (self.l == left.l) or (self.m == left.m) or (self.t == left.t):
            return Dimensional(self.value - left.value, self.l, self.m, self.t)
        

    def __mul__(self, right):
        if type(self) == Dimensional and type(right) != float and type(right) != int and type(right) != Dimensional:
            raise TypeError
        
        elif type(right) == float:
            return Dimensional(float(self.value *right), self.l, self.m, self.t)
        

        elif type(right) == int:
            return Dimensional(self.value *right, self.l, self.m, self.t)
        
        elif type(self.value) == float or type(right.value) == float:
            return Dimensional(float(self.value *right.value), self.l+right.l, self.m+right.m, self.t+right.t)
     
        
    def __rmul__(self, left):
        if type(self) == Dimensional and type(left) != float and type(left) != int and type(left) != Dimensional:
            raise TypeError
        
        elif type(left) == float:
            return Dimensional(float(self.value *left), self.l, self.m, self.t)
        
        elif type(left) == int:
            return Dimensional(self.value *left, self.l, self.m, self.t)
        
        elif type(self.value) == float or type(left.value) == float:
            return Dimensional(float(self.value *left.value), self.l+left.l, self.m+left.m, self.t+left.t)


    def __truediv__(self, right):
        if type(self) == Dimensional and type(right) != float and type(right) != int and type(right) != Dimensional:
            raise TypeError
        
        elif type(right) == float:
            return Dimensional(float(self.value /right), self.l, self.m, self.t)
        

        elif type(right) == int:
            return Dimensional((self.value/right), self.l, self.m, self.t)
        
        elif type(self.value) == float or type(right.value) == float and type(self) == type(right):
            return Dimensional(float(self.value /right.value), self.l-right.l, self.m-right.m, self.t-right.t)
    
            
    def __rtruediv__(self, left):
        if type(self) == Dimensional and type(left) != float and type(left) != int and type(left) != Dimensional:
            raise TypeError
        
        elif type(left) == float:
            return Dimensional(float(left/self.value), -1*self.l, self.m, -1*self.t)
        

        elif type(left) == int:
            return Dimensional(left/self.value, -1*self.l, self.m, -1*self.t)
        
        elif type(self.value) == float or type(left.value) == float:
            return Dimensional(float(self.value /left.value), self.l-left.l, self.m-left.m, self.t-left.t)
             
             
    def __pow__(self, right):
        if type(right) == float:
            raise TypeError

        
        if self.l == 0 and self.m == 0 and self.t == 0:
            return Dimensional(self.value**right, self.l, self.m, self.t)
                
        if type(right) == type(self):
            if right.l == 0 and right.m == 0 and right.t == 0:
                return Dimensional(self.value**right.value, self.l*2, self.m*2, self.t*2)
        
        if type(self) == type(right):
                raise DimensionError
            
        else:
            return Dimensional(self.value**right, self.l*right, self.m*right, self.t*right)
    
    
    def __eq__(self, right):

        if type(self) == type(right):
            if len(self) != len(right):
                raise DimensionError


        if type(self) == type(right):
            return (self.value == right.value and self.l == right.l and self.m == right.m and self.t == right.t) 
            
        elif type(right) == int or type(right) == float:
            return right == self.value


    def __lt__(self, right):
        if type(self) == type(right):
            if len(self) != len(right):
                raise DimensionError
        
        if type(self) == type(right):
            return (self.value < right.value) 
            
        elif type(right) == int or type(right) == float:
            return (self.value < right)
        
        
    def __gt__(self, right):
        if type(self) == type(right):
            if len(self) != len(right):
                raise DimensionError
        
        if type(self) == type(right):
            return (self.value > right.value) 
            
        elif type(right) == int or type(right) == float:
            return self.value > right
        
        
    def __le__(self, right):
        if type(self) == type(right):
            if len(self) != len(right):
                raise DimensionError
        
        if type(self) == type(right):
            return (self.value <= right.value and self.l <= right.l and self.m <= right.m and self.t <= right.t) 
            
        elif type(right) == int or type(right) == float:
            return self.value <= right
        
        
    def __ge__(self, right):
        if type(self) == type(right):
            if len(self) != len(right):
                raise DimensionError
        
        if type(self) == type(right):
            return (self.value >= right.value and self.l >= right.l and self.m >= right.m and self.t >= right.t) 
            
        elif type(right) == int or type(right) == float:
            return self.value >= right
        
        
    def __abs__(self):
        if self < 0:
            return self *-1
        elif self > 0:
            return self
        
    def sqrt(self):
        if self.value % 2 != 0 or self.l % 2 != 0 or self.m % 2 != 0 or self.t % 2 != 0:
            raise DimensionError
        else:
            return Dimensional(sqrt(self.value), int(self.l/2), int(self.m/2), int(self.t/2))
        
    def __setattr__(self, name, value):
        assert name not in self.__dict__
        assert name in ['l', 'm', 't', 'value'] 
        self.__dict__[name] = value


        

  





if __name__ == '__main__':
    # You can put your own code to test Dimensional here; for example
#     t = Dimensional(2.5,t=1)
#     g = Dimensional(9.8,l=1,t=-2)
#     d = .5*g*t**2
#     print(g/t)
# #     print(d.format("mgs"))
    
    
    #driver tests
    import driver
    driver.default_file_name = 'bsc2.txt'
#     driver.default_show_exception         = True
#     driver.default_show_exception_message = True
#     driver.default_show_traceback         = True
    driver.driver()
