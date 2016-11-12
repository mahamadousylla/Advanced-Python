# Generators must be able to iterate through any iterable.
# hide is present and called to ensure that your generator code works on
#   general iterable parameters (not just a string, list, etc.)
# For example, although we can call len(string) we cannot call
#   len(hide(string)), so the generator functions you write should not
#   call len on their parameters
# Leave hide in this file and add code for the other generators.

def hide(iterable):
    for v in iterable:
        yield v


# The combination of return and yield None make each of the following
#   a generator (yield None) that immediately raises the StopIteration
#   exception (return)

def sequence(*iterables):
    for iterable in iterables:
        for i in iterable:
            yield i
        


            
def group_when(iterable,p):
    alist = [ ]
    for i in iterable:
        if p(i):
            alist.append(i)
            yield alist
            alist = [ ]
        else:
            alist.append(i)

    if alist:
        yield alist
            
    
                
def drop_last(iterable,n):
    alist = list(iterable)
    while True:
        for iter in alist[:-n]:
            yield iter
        break



        
def yield_and_skip(iterable,skip):
    iterab = iter(iterable)
    while True:
        result = next(iterab)
        yield result
        for i in range(skip(result)):
            next(iterab)
            

   
def alternate(*args):
    args = [iter(a) for a in args]
    while True:
        result = False
        for arg in args:
            try:
                yield next(arg)
                result = True
            except StopIteration:
                pass
        if not result:
            return
    


def min_key_order(adict):
    if not adict:
        return
    lowest = min(adict)
    yield lowest,adict[lowest]
    while True:
        biggest = [key for key in adict if key>lowest]
        if not biggest:
            return
        else:
            lowest = min(biggest)
            yield lowest,adict[lowest]


 
 
                 


 
           
         
if __name__ == '__main__':
    from goody import irange
    
    # Test sequence; you can add your own test cases
    print('Testing sequence')
    for i in sequence('abc', 'd', 'ef', 'ghi'):
        print(i,end='')
    print('\n')

    print('Testing sequence on hidden')
    for i in sequence(hide('abc'), hide('d'), hide('ef'), hide('ghi')):
        print(i,end='')
    print('\n')


    # Test group_when; you can add your own test cases
    print('Testing group_when')
    for i in group_when('combustibles', lambda x : x in 'aeiou'):
        print(i,end='')
    print('\n')

    print('Testing group_when on hidden')
    for i in group_when(hide('combustibles'), lambda x : x in 'aeiou'):
        print(i,end='')
    print('\n')


    # Test drop_last; you can add your own test cases
    print('Testing drop_last')
    for i in drop_last('combustible', 5):
        print(i,end='')
    print('\n')

    print('Testing drop_last on hidden')
    for i in drop_last(hide('combustible'), 5):
        print(i,end='')
    print('\n')


# #     Test sequence; you can add your own test cases
#     print('Testing yield_and_skip')
#     for i in yield_and_skip('abbabxcabbcaccabb',lambda x : {'a':1,'b':2,'c':3}.get(x,0)):
#         print(i,end='')
#     print('\n')
#  
#     print('Testing yield_and_skip on hidden')
#     for i in yield_and_skip(hide('abbabxcabbcaccabb'),lambda x : {'a':1,'b':2,'c':3}.get(x,0)):
#         print(i,end='')
#     print('\n')


    # Test alternate; you can add your own test cases
#     print('Testing alternate')
#     for i in alternate('abcde','fg','hijk'):
#         print(i,end='')
#     print('\n')
#      
#     print('Testing alternate on hidden')
#     for i in alternate(hide('abcde'), hide('fg'),hide('hijk')):
#         print(i,end='')
#     print('\n\n')
#         
         
#     Test min_key_order; add your own test cases
#     print('\nTesting Ordered')
#     d = {1:'a', 2:'x', 4:'m', 8:'d', 16:'f'}
#     i = min_key_order(d)
#     print(next(i))
#     print(next(i))
#     del d[8]
#     print(next(i))
#     d[32] = 'z'
#     print(next(i))
#     print(next(i))
     


         
         
    import driver
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
    
