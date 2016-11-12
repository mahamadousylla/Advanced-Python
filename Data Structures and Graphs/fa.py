import goody


def read_fa(file : open) -> {str:{str:str}}:
    dictionary = { }
    for line in file:
        values_dict = { }
        line = line.strip().split(';')
        values = [list(i) for i in zip(*2*[iter(line[1:])])]
        for alist in values:
            values_dict[alist[0]] = alist[1]
        dictionary[line[0]] = values_dict
    return dictionary
       

def fa_as_str(fa : {str:{str:str}}) -> str:
    result = '  '
    count = 1
    for key in sorted(fa, key = lambda x: x):
        alist = [  ]
        for i in fa[key]:
            pair = (i, fa[key][i])
            alist.append(pair)
        if count == len(fa):
            result += '{} transitions: {}\n'.format(str(key), str(sorted(alist, key = lambda x: x[0][0])))
        else:
            result += '{} transitions: {}\n  '.format(str(key), str(sorted(alist, key = lambda x: x[0][0])))
        count += 1
    return result

    
def process(fa : {str:{str:str}}, state : str, inputs : [str]) -> [None]:
    result = [state]
    current_state = state
    for input in inputs:
        if input not in fa[current_state]:
            pair = (input, None)
            result.append(pair)
        else:
            next_state = fa[current_state][input]
            pair = (input, next_state)
            result.append(pair)
            current_state = next_state
    return result
       

def interpret(result : [None]) -> str:
    astring = ''
    count = 1
    astring += 'Start state = {}\n  '.format(result[0])
    for pair in result[1:]:
        if count == len(result[1:]):
            line = 'Input = {}; new state = {}\nStop state = {}\n'.format(pair[0], pair[1], result[-1][-1])        
            if result[-1][0] == 'x':
                line = 'Input = {}; illegal input: simulation terminated\nStop state = None\n'.format(pair[0])
        else: 
            line = 'Input = {}; new state = {}\n  '.format(pair[0], pair[1])
        count +=1
        astring += line
    return astring
        
    

    

if __name__ == '__main__':
    # Write script here

    file = goody.safe_open('Enter the name of any file with a finite automaton: ', 'r', 'Invalid, file could not be opened', 'faparity.txt')
    print()
    print('Finite Automaton\'s Description')
    dict = read_fa(file)
    print(fa_as_str(dict))
    start_state_file = goody.safe_open('Enter the name of any file with the start-state and inputs: ', 'r', 'Invalid, file could not be opened', 'fainputparity.txt')
    print()
    for line in start_state_file:
        print('Starting new simulation')
        line = line.strip().split(';')
        state = line[0]
        inputs = line[1:]
        alist = process(dict, state, inputs)
        print(interpret(alist))
    
    
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc3.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
