import goody


def read_voter_preferences(file : open):
    a_set = { }
    for line in file:
        line = line.strip().split(';')
        key = line[0]
        values = list(line[1:])
        a_set[key] = list(values)
    return a_set
        


def dict_as_str(d : {None:None}, key : callable=None, reverse : bool=False) -> str:
    astring = ''
    for item in sorted(d, key = key, reverse = reverse):
        astring += '  ' + str(item)  + ' -> ' + str(d[item]) + '\n'
    return astring


def evaluate_ballot(vp : {str:[str]}, cie : {str}) -> {str:int}:
    a_set = { }
    for cand in cie:
        count = 0
        for key in vp:
            for i in range(len(vp[key])):
                if vp[key][i] == cand:
                    count +=1
                    break
                elif vp[key][i] in cie:
                    break            
        a_set[cand] = count
    return a_set
        


def remaining_candidates(vd : {str:int}) -> {str}:
    a_set = set()
    lowest = min(vd.items(), key = lambda x: x[1])[-1]
    for key in vd:
        if vd[key] != lowest:
            a_set.add(key)
    return a_set
        

def run_election(vp_file : open) -> {str}:
    dictionary = read_voter_preferences(vp_file)
    for key in dictionary:
        voters = dictionary[key]
    candidate = set(voters)
    print('Voting Preferences')
    print(dict_as_str(dictionary, None, False))
    f = lambda x: x[0]
    g = lambda x: (0, x[-1])
    
    while len(candidate) > 1:
        str_int = evaluate_ballot(dictionary, candidate)
        candidate = remaining_candidates(str_int)
        print('Vote count on ballot #1 with candidate (alphabetical order); remaining candidate set = {}'.format(candidate))
        print(dict_as_str(str_int, f, False))
        
        print('Vote count on ballot #1 with candidate (numerical order); remaining candidate set = {}'.format(candidate))
        print(dict_as_str(str_int, g, True))
        
        str_int = evaluate_ballot(dictionary, candidate)
        candidate = remaining_candidates(str_int)
        print('Vote count on ballot #2 with candidate (alphabetical order); remaining candidate set = {}'.format(candidate))
        print(dict_as_str(str_int, f, False))
        
        print('Vote count on ballot #2 with candidate (numerical order); remaining candidate set = {}'.format(candidate))
        print(dict_as_str(str_int, g, False))
        
        print('Winner is {}'.format(candidate))
    
    return candidate
      
    
if __name__ == '__main__':
    # Write script here
    
    file = goody.safe_open('Enter the name of any file with voter preferences: ', 'r', 'Invalid, file could not be opened', 'votepref1.txt')
    run_election(file)
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc2.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
