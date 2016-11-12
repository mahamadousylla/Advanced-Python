from collections import defaultdict

 # Helper function used in testing; do not remove or modify
def palindrome(s : str) -> bool:
    return s == s[-1::-1]


def abs_of(f : callable) -> callable:
    def absf(n):
        result = f(n)
        return abs(result)
    return absf

def select(predicates : [callable]) -> callable:
    def big_odd(iterable):
        return [i for i in iterable if all( (predicate(i) for predicate in predicates) ) ]
    return big_odd
    

def talk(alist : [int]) -> [int]:
    result = [ ]
    count = 1
    assert type(alist) == list
    for item in alist:
        assert type(item) == int
    assert len(alist) >= 1
    for i in range(len(alist)):
        
        if (i+1) == (len(alist)):
            result.append(count)
            result.append(alist[i])
            break
            
        elif alist[i] == alist[i+1]:
            count +=1

        else:
            result.append(count)
            result.append(alist[i])
            count = 1

    return result


def made_quota(db : {str:(str,int,int)}) -> {str}:
    x = [key for key in db if all( (list(db[key])[i][-1] >= list(db[key])[i][1] for i in range(len(list(db[key])))))]
    return set(x)

def sales1(db : {str : (str,int,int)}) -> [str]:
    result = [ ]
    final=[]
    for keey in db:
        total = 0
        fields = list(db[keey])
        for i in range(len(fields)):
            total += fields[i][-1]
        pair = (keey, total)
        result.append(pair)
    for name in sorted(result, key= lambda x: (-x[-1], 0)):
        final.append(name[0])
    return final

        
def sales2(db : {str : (str,int,int)}) -> [(str,int)]:
    result = [ ]
    for key in db:
        total = 0
        fields = list(db[key])
        for i in range(len(fields)):
            total += fields[i][-1]
        pair = (key, total)
        result.append(pair)
    return sorted(result, key= lambda x: (-x[-1], x[0]))


def by_category(db : {str : (str,int,int)}) -> {str : (str,int,int)}:
    categories = [ ]
    new_dict = { }
    for key in db:
        values = list(db[key])
        for value in values:
            if value[0] not in categories:
                categories.append(value[0])
                
            for category in categories:
                if category == value[0]:
                    if category not in new_dict:
                        the_values = [(key, value[1], value[2])]
                        new_dict[category] = the_values
                
                    else:
                        more_values = (key, value[1], value[2])
                        new_dict[category].append(more_values)

    for key in new_dict:
        new_dict[key] = sorted(new_dict[key])
    return new_dict

        
def category_leaders(db : {str : (str,int,int)}) -> [int,{str}]:
    new_dict = by_category(db)
    dictionary = { }

    for key in new_dict:
        localcount = 0
        name = [ ]
        values = list(new_dict[key])
        for i in range(len(values)):
            if values[i][-1] > localcount:
                localcount = values[i][-1]
        for index in range(len(values)):
            if values[index][-1] == localcount:
                name.append(values[index][0])
        
        dictionary[key] = [localcount, set(name)]
    return dictionary
         


 


if __name__ == '__main__':
    from goody import irange
    # Feel free to test other cases as well
    print('Testing abs_of')
    f = abs_of(lambda x : 3*x+2)
    print( [(a,f(a)) for a in [-10, -5, 0, 5, 10]] )
    g = abs_of(lambda x : -x)
    print( [(a,g(a)) for a in [-10, -5, 0, 5, 10]] )
     
    print('\nTesting select')
    big_odd = select ([(lambda x : x%2 == 1), (lambda x : x > 5)]) 
    print( big_odd(range(1,10)) )
    scp = select([(lambda x : len(x) <=5),(lambda x : x[0] not in 'aeiou'),palindrome])
    print( scp(['rotator', 'redder', 'pepper', 'rotor', 'tiny', 'eye', 'mom', 'ere', 'radar', 'racecar', 'peep']) )

    print('\nTesting talk')
    seq = [1]
    print(1, seq)
    for i in irange(2,10):
        seq = talk(seq)
        print(i,seq)

    # For testing functions: none should mutate these dicts
    lexus = {'Rich': {('car', 10, 4), ('suv', 10, 12)},
             'Steve': {('crossover', 10, 12), ('car', 7, 8)},
             'Nancy': {('truck', 10, 5), ('car', 10, 8)},
             'Lori' : { ('suv', 10, 12), ('truck', 10, 10), ('car', 10, 15) } }
    
    ace =   {'Alex'  : {('hammer', 4, 7), ('saw', 6, 6)},
             'Mark'  : {('hammer', 6, 8), ('wrench', 7, 6)},
             'Bernie': {('pliers', 4, 5), ('screws', 4, 2)},
             'Mike'  : { ('pliers', 2, 3), ('screws', 4, 4), ('wrench', 3, 3) },
             'Katie' : { ('hammer', 1, 1), ('pliers', 2, 6), ('screws', 3, 5) } }

    ace2 =  {'Alex'  : {('hammer', 4, 6), ('saw', 6, 6)},
             'Mark'  : {('hammer', 6, 8), ('wrench', 7, 6)},
             'Bernie': {('pliers', 4, 5), ('screws', 4, 7)},
             'Mike'  : { ('pliers', 2, 5), ('screws', 4, 4), ('wrench', 3, 3) },
             'Katie' : { ('hammer', 1, 1), ('pliers', 2, 6), ('screws', 3, 5) } }
    
    print('\nTesting made_quota')
    print(made_quota(lexus))
    print(made_quota(ace))
    
    print('\nTesting sales1')
    print(sales1(lexus))
    print(sales1(ace))
    
    print('\nTesting sales2') 
    print(sales2(lexus))
    print(sales2(ace))
    print(sales2(ace2))
    
    print('\nTesting by_category')
    print(by_category(lexus))
    print(by_category(ace))

    print('\nTesting category_leader')
    print(category_leaders(lexus))
    print(category_leaders(ace))

    
    print('\ndriver testing with batch_self_check:')
    import driver
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()           





























