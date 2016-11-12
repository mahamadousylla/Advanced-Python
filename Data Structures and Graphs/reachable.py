import goody
import prompt
from collections import defaultdict


def read_graph(file : open) -> {str:{str}}:
    '''
    reads a file and builds a dictionary using the information
    '''
    dictionary = { }
    for line in file:
        line = line.strip()
        key, value = line.split(';')
        if key in dictionary:
            dictionary[key].update(set(value))
        else:
            dictionary[key] = set(value)
    return dictionary


def graph_as_str(d : {str:{str}}) -> str:
    '''
    prints the a string information from given dictionary in textual format
    '''
    astring = ''
    for item in sorted(d, key = lambda x: x):
        astring += '  ' + str(item)  + ' ' +  '->' + ' ' + str(sorted(list(d[item]))) + '\n'
    return astring

            
def reachable(d : {str:{str}}, start : str) -> {str}:
    aset = set()
    alist = [start]
    while alist:
        edge = alist.pop(0)
        aset.add(edge)
        for letter in d.get(edge, {}):
            if letter not in aset:
                alist.append(letter)
    return aset





if __name__ == '__main__':
    # Write script here

    file = goody.safe_open('Enter the name of any file with a graph ', 'r', 'Invalid, file could not be opened', 'graph1.txt')          
    dict = read_graph(file)
    print('Graph: source -> [destination] edges')
    string = graph_as_str(dict)
    print(string)
    while True:
        try:
            start_node = input('Enter the name of any starting node: ')
            if start_node == 'quit':
                break
            else: 
                destination = reachable(dict, start_node)
                if len(destination) == 1 and destination[0:] == start_node: 
                    raise Exception
            print('From a the reachable nodes are {}\n'.format(destination))

        except:
            print('  Entry Error: ' + str(start_node) + ';  Illegal: not a source node')
            print('  Please enter a legal String \n')
            
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
    
