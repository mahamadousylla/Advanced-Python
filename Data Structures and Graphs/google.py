import prompt 
from goody       import safe_open,irange
from collections import defaultdict # Use defaultdict for prefix and query


def all_prefixes(fq : (str,)) -> {(str,)}:
    x = [fq[0:(i+1)]  for i in range(len(fq))]
    return set(x)


def add_query(prefix : {(str,):{(str,)}}, query : {(str,):int}, new_query : (str,)) -> None:
    for i in all_prefixes(new_query):
        prefix[i].update({new_query})
    query[new_query] += 1


def read_queries(open_file : open) -> ({(str,):{(str,)}}, {(str,):int}):
    prefix = defaultdict(set)
    query = defaultdict(int)
    for line in open_file:
        line = tuple(line.strip().split())
        for i in all_prefixes(line):
            alist = [ ]
            alist.append(line)
            prefix[i].update(alist)
        query[line] += 1
    return prefix, query


def dict_as_str(d : {None:None}, keey : callable=None, reverse : bool=False) -> str:
    astring = ''
    for item in sorted(d, key = keey, reverse = reverse):
        astring += '  ' + str(item)  + ' ' +  '->' + ' ' + str(d[item]) + '\n'
    return astring


def top_n(a_prefix : (str,), n : int, prefix : {(str,):{(str,)}}, query : {(str,):int}) -> [(str,)]:
    result = [ ]
    new_list = [ ]
    if a_prefix not in prefix:
        return [ ]
    else:
        
        for key in prefix[a_prefix]:
            result.append((query[key], key))
        for item in sorted(result, key = lambda x: (-x[0], x[1])):
            new_list.append(item[1])
        return new_list[0:n]
        

# Script

if __name__ == '__main__':
    # Write script here
#     print(all_prefixes(('a','b','c')))
#     print(read_queries(open('googleq0.txt')))
    # For running batch self-tests
    
    file = safe_open('Enter the name of any file with the full queries: ', 'r', 'Invalid, file could not be opened', 'googleq0.txt')
    print()
    print('Prefix dictionary:')
    prefix_dict, query_dict = read_queries(file)
    print(dict_as_str(prefix_dict,lambda x: (len(x), x), False))
    print('Query dictionary:')
    print(dict_as_str(query_dict, lambda x: query_dict[x], True))
    while True:
        user_input = input('Enter any prefix (or quit): ').strip()
        if user_input == 'quit':
            break
        user_input = tuple(user_input.split())
        top_three = top_n(user_input, 3, prefix_dict, query_dict)
        print('  Top 3 (or fewer) full queries = ', top_three)
        print()
        user_input_update = input('Enter any full query (or quit): ').strip()
        if user_input_update == 'quit':
            break
        print()
        user_input_update = tuple(user_input_update.split())
        add_query(prefix_dict, query_dict, user_input_update)
        print('Prefix dictionary:')
        print(dict_as_str(prefix_dict,lambda x: (len(x), x), False))
        print('Query dictionary:')
        print(dict_as_str(query_dict, lambda x: query_dict[x], True))
#     
#         
#     print()
    import driver
    driver.default_file_name = "bsc5.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
