import goody


def read_ndfa(file : open) -> {str:{str:{str}}}:
    dictionary = { }
    for line in file:
        values_dict = { }
        line = line.strip().split(';')
        values = [i for i in zip(*2*[iter(line[1:])])]
        for pair in values:
            aset = set()
            aset.add(pair[1])
            if pair[0] in values_dict:
                values_dict[pair[0]].update(aset)
            else:
                values_dict[pair[0]] = aset
        dictionary[line[0]] = values_dict
    return dictionary
                

def ndfa_as_str(ndfa : {str:{str:{str}}}) -> str:
    result = '  '
    count = 1
    for key in sorted(ndfa, key = lambda x: x):
        alist = [  ]
        for i in ndfa[key]:
            pair = (i, list(ndfa[key][i]))
            alist.append(pair)
        for item in alist:
            item[1].sort()
        if count == len(ndfa):
            result += '{} transitions: {}\n'.format(str(key), str(sorted(alist, key = lambda x: x[0][0])))
        else:
            result += '{} transitions: {}\n  '.format(str(key), str(sorted(alist, key = lambda x: x[0][0])))
        count += 1
    return result

       
def process(ndfa : {str:{str:{str}}}, state : str, inputs : [str]) -> [None]:
    result = [state]
    current_state = [state]
    for input in inputs:
        possible_states = [ ]
        for the_state in current_state:
            if input not in ndfa[the_state]:
                pass
            else:         
                next_state = ndfa[the_state][input]
                for item in next_state:
                    possible_states.append(item)

        current_state = possible_states
        pair = (input, set(possible_states))
        result.append(pair)
        if len(possible_states) < 1:
            return result
            
    return result


def interpret(result : [None]) -> str:
    astring = ''
    count = 1
    astring += 'Start state = {}\n  '.format(result[0])

    for pair in result[1:]:
        if count == len(result[1:]):
            line = 'Input = {}; new possible states = {}\n'.format(pair[0], sorted(list(pair[1])))   
            line += 'Stop state(s) = {}\n'.format(sorted(list(pair[1])))
        else: 
            line = 'Input = {}; new possible states = {}\n  '.format(pair[0], sorted(list(pair[1])))
        count +=1
        astring += line
    return astring





if __name__ == '__main__':
    # Write script here
#     file = goody.safe_open('Enter the name of any file with a finite automaton: ', 'r', 'Invalid, file could not be opened', 'ndfaendin01.txt')
#     print(read_ndfa(file))
#     dict = read_ndfa(file)
#     print(ndfa_as_str(dict)) 
#     result = process(dict, 'start', ['1','0','1','1','0','1'])
#     print(interpret(result))

    # For running batch self-tests
    
    file = goody.safe_open('Enter the name of any file with a non-deterministic finite automaton: ', 'r', 'Invalid, file could not be opened', 'ndfaendin01.txt')
    print()
    print('Non-Deterministic Finite Automaton\'s Description')
    dict = read_ndfa(file)
    print(ndfa_as_str(dict))
    start_state_file = goody.safe_open('Enter the name of any file with the start-state and inputs: ', 'r', 'Invalid, file could not be opened', 'ndfainputendin01.txt')
    print()
    for line in start_state_file:
        print('Starting new simulation')
        line = line.strip().split(';')
        state = line[0]
        inputs = line[1:]
        alist = process(dict, state, inputs)
        print(interpret(alist))
    print()
    import driver
    driver.default_file_name = "bsc4.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
