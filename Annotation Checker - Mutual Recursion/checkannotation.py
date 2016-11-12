from goody import type_as_str
import inspect

class Check_All_OK:
    """
    Check_All_OK class implements __check_annotation__ by checking whether each
      annotation passed to its constructor is OK; the first one that
      fails (by raising AssertionError) prints its problem, with a list of all
      annotations being tried at the end of the check_history.
    """
       
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_All_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check, param, value,check_history):
        for annot in self._annotations:
            check(param, annot, value, check_history+'Check_All_OK check: '+str(annot)+' while trying: '+str(self)+'\n')


class Check_Any_OK:
    """
    Check_Any_OK implements __check_annotation__ by checking whether at least
      one of the annotations passed to its constructor is OK; if all fail 
      (by raising AssertionError) this classes raises AssertionError and prints
      its failure, along with a list of all annotations tried followed by the
      check_history.
    """
    
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_Any_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check, param, value, check_history):
        failed = 0
        for annot in self._annotations: 
            try:
                check(param, annot, value, check_history)
            except AssertionError:
                failed += 1
        if failed == len(self._annotations):
            assert False, repr(param)+' failed annotation check(Check_Any_OK): value = '+repr(value)+\
                         '\n  tried '+str(self)+'\n'+check_history                 



class Check_Annotation():
    # set this name to True for checking to occur
    checking_on  = True
  
    # self._checking_on must also be true for checking to occur
    def __init__(self,f):
        self._f = f
        self.checking_on = True
        
    # Check whether param's annot is correct for value, adding to check_history
    #    if recurs; defines many local function which use it parameters.  
    def check(self,param,annot,value,check_history=''):
        
        CommonErrors = ["'{}' failed annotation check({}): value = '{}'\n was type {} ...should be type {}\n" + check_history, "'{}' failed annotation check({}): value = {}\n{}", "'{}' annotation inconsistency: {} should have 1 item but had {}\n\tannotation = {}"]
        
        def check_list(usestruct=list):
            assert isinstance(value, usestruct), CommonErrors[0].format(param,'wrong type', value, type(value).__name__, usestruct.__name__)
            if len(annot) != 1:
                assert len(annot) == len(value), CommonErrors[1].format(param, 'wrong number of elements', value, '\tannotation had {} elements{}'.format(str(len(value)), value))
                checkh = ''
                for item in range(len(annot)):
                    checkh += '{}[{}] check: {}'.format(usestruct.__name__,str(item), str(annot[item]) +'\n')
                    self.check(param, annot[item], value[item], checkh)
            else:
                checkh = ''
                for item in range(len(value)):
                    checkh += '{}[{}] check: {}'.format(usestruct.__name__,str(item), str(annot[0]) +'\n')
                    self.check(param, annot[0], value[item], checkh)
        
        def check_dict():
            assert isinstance(value, dict), CommonErrors[0].format(param, 'wrong type', value, type(value).__name__, 'dict')
            assert len(annot) == 1, CommonErrors[2].format(param, 'dict', str(len(annot)), str(annot))
            for key in value:
                self.check(param, list(annot.items())[0][0], key)
                self.check(param, list(annot.items())[0][1], value[key])
                        
        def check_set(usestruct=set):
            assert isinstance(value, usestruct), CommonErrors[0].format(param, 'wrong type', value, type(value).__name__, usestruct.__name__)
            assert len(annot) == 1, CommonErrors[2].format(param, usestruct.__name__, str(len(annot)), str(annot))
            for item in value:
                self.check(param, list(annot)[0], item)
         
        def check_str():
            try:
                EvaluateAnnot = annot
                for key in self.AllParameters:
                    EvaluateAnnot = EvaluateAnnot.replace(key, str(self.AllParameters[key]))
                assert eval(EvaluateAnnot),"{} failed annotation check(str predicate: '{}')".format(param, annot)
            
            except Exception as e:
                raise AssertionError("{} failed annotation check(str predicate: '{}')\n exception = {}".format(param, str(annot), str(e)))
                                
        
        if annot == None:
            return
        elif isinstance(annot, type):
            assert isinstance(value, annot), CommonErrors[0].format(param,'wrong type', value, type(value).__name__, annot.__name__)
        elif isinstance(annot, list):
            check_list()
        elif isinstance(annot, tuple):
            check_list(tuple)
        elif isinstance(annot, dict):
            check_dict()
        elif isinstance(annot, set):
            check_set()
        elif isinstance(annot, frozenset):
            check_set(frozenset)
        elif isinstance(annot, type(lambda x:x)):
            assert len(inspect.getargspec(annot)[0]) == 1, '{} annotation inconsistency: predicate should have 1 parameter but had {}\n\t predicate = {}'.format(param, str(len(inspect.getargspec(annot)[0])), annot)
            try:
                assert annot(value) == True, CommonErrors[1].format(param, str(value), '\tpredicate = ' + str(annot))
            except Exception as e:
                raise AssertionError('{} annotation predicate({}) raised exception\n\t exception = {}'.format(param, str(annot), str(e)))
        elif isinstance(annot, str):
            check_str()
        
        else:
            try:
                assert callable(getattr(annot, '__check_annotation__')), '{} annotation undecipherable: {}'.format(param, str(annot))
                try:
                    annot.__check_annotation__(self.check,param,value,check_history)
                except Exception as e:
                    raise AssertionError('{} annotation predicate({}) raised exception\n\texception = {}\n{} value check: {}'.format(param, str(value), str(e), annot, str(value)))
            except AttributeError as e:
                raise AssertionError('{} annotation undecipherable: {}'.format(param, str(annot)))
            
            
        # Define local functions for checking, list/tuple, dict, set/frozenset,
        #   lambda/functions, and str (str for extra credit)
        # Many of these local functions called by check, call check on their
        #   elements (thus are indirectly recursive)
        # Decode the annotation here and then check it 
        pass 
        
    # Return result of calling decorated function call, checking present
    #   parameter/return annotations if required
    def __call__(self, *args, **kargs):
        
        # Return a dictionary of the parameter/argument bindings (actually an
        #    ordereddict, in the order parameters occur in the function's header)
        def param_arg_bindings():
            f_signature  = inspect.signature(self._f)
            bound_f_signature = f_signature.bind(*args,**kargs)
            for param in f_signature.parameters.values():
                if param.name not in bound_f_signature.arguments:
                    bound_f_signature.arguments[param.name] = param.default
            return bound_f_signature.arguments

        # If annotation checking is turned off at the class or function level
        if any([Check_Annotation.checking_on, self.checking_on]) == False:
                return self._f(*args, **kargs)
        #   just return the result of calling the decorated function
        # Otherwise do all the annotation checking
        
        try:
            # Check the annotation for every parameter (if there is one)
            GetParameters = param_arg_bindings()
            self.AllParameters = GetParameters
            for param in GetParameters:
                if param in self._f.__annotations__:
                    self.check(param, self._f.__annotations__[param], GetParameters[param])
                
            # Compute/remember the value of the decorated function
            ReturnValue = self._f(*args, **kargs)
            # If 'return' is in the annotation, check it
            if 'return' in self._f.__annotations__:
                self.check('return', self._f.__annotations__['return'], ReturnValue)
            # Return the decorated answer
            return ReturnValue
            
        # On first AssertionError, print the source lines of the function and reraise 
        except AssertionError:
#             print(80*'-')
#             for l in inspect.getsourcelines(self._f)[0]: # ignore starting line #
#                 print(l.rstrip())
#             print(80*'-')
            raise




  
if __name__ == '__main__':     
    # an example of testing a simple annotation  
    try:
        def f(x:int): pass
        f = Check_Annotation(f)
        f(3)
        f('a')
    except AssertionError as e:
        print(e)
           
    import driver
    driver.driver()
