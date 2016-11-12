from collections import defaultdict
from goody import type_as_str

class Bag:
    
    def __init__(self, iterable = []):
        self.iterable = iterable 
        self.bag = defaultdict(int)
    
        for value in self.iterable: 
            self.bag[value] = iterable.count(value)

    def __repr__(self):
        result = 'Bag('
        result += str(self.iterable)
        result += ')'
        return result

        
    def __str__(self):
        if not self.bag.items(): 
            return 'Bag()'
        
        self.string = 'Bag('

        
        for val, num in self.bag.items(): 
            self.string += str(val) + '[' + str(num) + ']' + ','
        self.string += ')'
        
        return self.string
    
    
    def __len__(self):
        return len(self.iterable)
    

    def unique(self):
        return len(self.bag)
    
    
    def __contains__(self, val):
        return val in self.bag
    
    
    def count(self, value):
        return self.bag[value]
      
        
    def add(self, value):
        if value in self.bag: 
            self.bag[value] += 1
        else: 
            self.bag[value] = 1
            
        self.iterable.append(value)
     
        
    def __add__(self, iterable1):  
        new_iter = []
        if type(iterable1) != Bag: 
            raise TypeError
        new_iter.extend(self)
        new_iter.extend(iterable1)
        return new_iter
        
        
    def remove(self, value):
        if value in self.bag:
            self.bag[value] -= 1
            if self.bag[value] == 0:
                del self.bag[value]
                
        elif value not in self.bag:
            raise ValueError
            print('Value Error' + str(value) + ' is not in ' + str(self.bag))
            
        
    def __eq__(self, bag):
        if type(bag) != type(self):
            return False
        for key in self:
            if self.bag[key] != bag.bag[key]:
                return False
        return True


    def __ne__(self, bag):
        if type(self) != type(bag):
            return True
        for key in self:
            if self.bag[key] != bag.bag[key]:
                return True
        return False

    def __iter__(self):
        result = [ ]
        for key in self.bag:
            for i in range(self.bag[key]):
                result.append(key) 
        return iter(result)
        




if __name__ == '__main__':
    # You can put your own code to test Bags here

    print()
    import driver
    driver.default_file_name = 'bsc1.txt'
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
#     driver.default_show_traceback = True
    driver.driver()
