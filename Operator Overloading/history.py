from collections import defaultdict


class History:
    
    def __init__(self):
        self.history = defaultdict(list)


    def __setattr__(self,key,value):
        if '_prev' in key:
            raise NameError('NameError')
        
        if 'history' in self.__dict__:
            self.history[key].append(value)
        
        self.__dict__[key] = value 
           
           
    def __getattr__(self,user_name):
        count = user_name.count('_prev')
        if count == 0 or user_name.endswith('_prev') == False:
            raise NameError('NameError')
        
        other_name = user_name[:1]
        if other_name not in self.history:
            raise NameError('NameError')
        
        new = self.history[other_name]
        if count < len(new):
            result = -(count) - 1
            return new[result]
        else:
            return None


    def __getitem__(self,number):
        
        if number > 0:
            raise IndexError('IndexError')
        
        else:   
            return {key:value[(number-1)] if abs(number) < len(value) else None for key,value in self.history.items()}






if __name__ == '__main__':
    # Put in simple tests for History before allowing driver to run

    print()
    import driver
    
    driver.default_file_name = 'bsc2.txt'
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
