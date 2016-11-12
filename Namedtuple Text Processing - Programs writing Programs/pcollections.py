import re, traceback, keyword


        
def pnamedtuple(type_name, field_names, mutable=False):
    def show_listing(s):
        for i, l in enumerate(s.split('\n'), 1):
            print(' {num: >3} {txt}'.format(num=i, txt=l.rstrip()))

    # put your code here
    # bind class_definition (used below) to the string constructed for the class
    Result = ''
    if type(type_name) != str:
        raise SyntaxError('Type of type name is not a string')
    if re.match('^[A-Za-z]+(\w)*$', type_name) ==  None:
        raise SyntaxError('Type name is not a legal name')
    if type_name in keyword.kwlist:
        raise SyntaxError('Type name is found in keyword list')
    if type(field_names) == list:
        testlist = field_names
    elif type(field_names) == str:
        if ',' in field_names:
            testlist = field_names.replace(' ', '').split(',')
        elif ' ' in field_names:
            testlist = field_names.split(' ')
        else:
            raise SyntaxError('Field names is invalid')
    else:
        raise SyntaxError('Type of Field names is invalid')
    if all(re.match('^[A-Za-z]+(\w)*$', item)!=None for item in testlist) != True:
        raise SyntaxError('One or more items in Field names is invalid')
    Result += InitFunction.replace('type_name', type_name)
    Result = Result.replace('^', ''.join(('self.' + param +' = ' + param + '\n        ') for param in testlist)[:-9])
    Result = Result.replace('field_names', ''.join((param + ',') for param in testlist)[:-1])
    Result = Result.replace('%field', str(testlist))
    Result = Result.replace('%mutable', str(mutable))
    Result = Result.replace('%source_code', "'''" +  Result + "'''")

    get_function = ''.join(GetFunction.replace('field', param) + '\n' for param in testlist)
    Result += get_function
    
    exec(Result)
    return(eval(type_name))
    
    #print(type(Result))
    #return eval(Result)
InitFunction = '''class type_name:
    source_code = %source_code
    def __init__(self, field_names, mutable=%mutable):
        self._mutable = True
        ^
        self._fields = %field
        self._mutable = mutable
        
    def __repr__(self):
        return 'type_name(' + ''.join(param + '=' + str(self.__dict__[param]) + ',' for param in self._fields)[:-1] + ')'
    
    def __getitem__(self, index):
        if type(index) == str:
            if index not in self._fields:
                raise IndexError('The index does not exist')
            return eval('self.get_' + index + '()')
        elif type(index) == int:
            if index not in range(len(self._fields)):
                raise IndexError('The index is out of range')
            return eval('self.get_' + self._fields[index] + '()')
        else:
            raise IndexError('Index type is invalid')
    
    def __eq__(self, right):
        if type(right) == type(self):
            return all(self.__getitem__(str(param)) == right.__getitem__(str(param)) for param in self._fields) 
        return False
        
    def _replace(self, **kargs):
        
        if not all(key in self._fields for key in kargs.keys()):
            raise TypeError('One or more of the arguments could not be found')
        if self._mutable:
            for karg in kargs.keys():
                exec('self.' + karg + ' = ' + str(kargs[karg]))
                                     
        else:
            new = ''
            for key in self._fields:
                if key in kargs.keys():
                    new += str(kargs[key]) + ','
                else:
                    new += str(self[key]) + ','
            
            return type(self)(*[eval(item) for item in new[:-1].split(',')])
            
           
            
    def __setattr__(self, name, value):
        if '_mutable' in self.__dict__: 
            if self._mutable:
                self.__dict__[name] = value
            else:
                raise AttributeError('type_name is immutable')
        else:
            self.__dict__[name] = value



            
    
               
        
        
'''
GetFunction = '''
    def get_field(self):
        return self.field
    '''
    
# class type_name:
#     def __init__(self, field_names, mutable=False):
#         
#         self._fields = [field_names]
#         self._mutable = mutable
#         
# class Triple3:
#     pass

            
         
            
            
        
     


    # For initial debugging, always show the source code of the class
    #show_listing(class_definition)
    
    # Execute the class_definition string in a local namespace and then bind the
    #   name source_code in its dictionary to the class_defintion; return the
    #   class object created; if there is a syntax error, list the class and
    #   also show the error
#     name_space = dict(__name__='pnamedtuple_{type_name}'.format(type_name=type_name))
#     try:
#         exec(class_definition,name_space)
#         name_space[type_name].source_code = class_definition
#     except(SyntaxError, TypeError):
#         show_listing(class_definition)
#         traceback.print_exc()
#     return name_space[type_name]


    
if __name__ == '__main__':
    Triple1    = pnamedtuple('Triple3', ['a','b','c'])
    Triple2 = Triple1(1,2,3)
    import driver
    driver.driver()
