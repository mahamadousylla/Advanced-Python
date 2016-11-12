import prompt                          # for driver
from collections import defaultdict    # use if you want (see problem descriptions)



def service_count2 (db : {str:{str:int}}) -> {str:int}:
    answer = defaultdict(int)
    for key in db:
        tempList = [ ]
        total = len(db[key])
        answer[key] = total
    return answer


def cando2 (service : str, db : {str:{str:int}}) -> [(str,int)]:
    alist = [ ]
    for key in db:
        if service in db[key]:
            count = db[key][service]
            pair = (key, count)
            alist.append(pair)
    return sorted(alist, key = lambda x: (-x[1],x[0]))


def read_db2(file : open) -> {str:{str:int}}:
    answer = { }
    for line in file:
        tempdict = { }
        line = line.strip().split(':')
        result = [i for i in zip(*2*[iter(line[1:])])]
        for tup in result:
            tempdict[tup[0]] = int(tup[1])
        answer[line[0]] = tempdict
    return answer


def stats2(db : {str:{str:int}}) -> [(str,int,float)]: 
    result = [ ]
    for key in db:
        total = 0 
        services = len(db[key])
        for other_key in db[key]:
            tot = db[key][other_key]
            total += tot
        pair = (key, services, total/len(db[key]))
        result.append(pair)
    return sorted(result, key = lambda x: x[0])
        


def translate2to1(db : {str:{str:int}}) -> {(str,str):int}:
    answer = defaultdict(int)
    for key in db:
        for other_key in db[key]:
            pair = (key, other_key)
            answer[pair] = db[key][other_key]
    return answer



 
if __name__ == '__main__':
    import driver
    driver.driver()
