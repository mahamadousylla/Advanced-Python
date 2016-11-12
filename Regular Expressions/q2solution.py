import re
from goody import irange
from collections import defaultdict

# Before running the driver on the bsc.txt file, ensure you have put a regular
#   expression pattern in the files repattern1a.txt, repattern1b.txt, and
#   repattern2a.txt. 

#result in ascending order (duplicates allowed)
def pages (page_spec : str) -> [int]:
    result = [ ]
    assert ',,' not in page_spec
    pages_spec = page_spec.split(',')
    for item in pages_spec:
        assert not item.split(':')[0].startswith('0') and not item.split(':')[-1].startswith('0')
        assert not item.split('-')[-1].startswith('0') and not item.split('-')[0].startswith('0')
        assert not ':-' or not '-:' in item
        if '-' in item:
            item = item.split('-')
            assert item[-1] > item[0]
            difference = int(item[-1]) - int(item[0])
            result.append(int(item[0]))
            for i in range(difference):
                next = int(item[0]) + (i+1)
                result.append(next)
        elif ':' in item:
            item = item.split(':')
            result.append(int(item[0]))
            total = int(item[-1]) + int(item[0])
            difference = total - int(item[0])
            for i in range(difference):
                next = int(item[0]) + (i+1)
                result.append(next)
        else:
            result.append(int(item))
    result.sort()
    return result



def multi_search(pat_file : open, text_file : open) -> [(int,str,{int})]:
    prefix = [(i,re.compile(p.rstrip())) for i,p in enumerate(pat_file,1)]
    result = []
    for number,line in enumerate(text_file,1):
        line = line.rstrip()
        pattern = [i for i,p in prefix if p.search(line)]
        if pattern:
            result.append((number,line,pattern))
    return result


    


if __name__ == '__main__':
    print(multi_search(open("pats.txt"),open("texts.txt")))
    import driver
#     print(multi_search(open('pats.txt)')))
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
