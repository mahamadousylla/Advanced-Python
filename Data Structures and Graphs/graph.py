# Defines a special exception for use with the Graph class methods
# Use like any exception: e.g., raise GraphError('Graph.method: ...error indication...')
class GraphError(Exception):
    pass # Inherit all methods, including __init__
 
 
class Graph:
    def __init__(self,*args):
        self.edges = {}
        # You may not define any other attributes
        # Other methods will examine/update the edges attribute
 

    def __setitem__(self,o,d):
        if type(o) != str or type(d) != str:
            raise GraphError
        elif type(o) == str and type(d) == str:
            if o not in self.edges:
                self.edges[o] = [set(), set()]
            if d not in self.edges:
                self.edges[d] = [set(), set()]
            self.edges[o][0].update(d)
            self.edges[d][1].update(o)
 
 
    def __getitem__(self,item):
        if type(item) == tuple and len(item) == 2:
            if all(i for i in item if i in self.edges):
                if item[0] in self.edges:
                    return item[1] in self.edges[item[0]][0]
        if item in self.edges:
            return self.edges[item][0]
        else:
            raise GraphError
        
     
    def __len__(self):
        total = 0
        for s in self.edges:
            total += len(self.edges[s][0])
        return total
     
    def __call__(self,d):
        if d in self.edges:
            return self.edges[d][1]
        else:
            raise GraphError     


    def degree(self,n):
        if n not in self.edges:
            raise GraphError
        else:
            return (len(self.edges[n][0]) + len(self.edges[n][1]))
        
     
    def __contains__(self,item):
        if type(item) is str:
            return item in self.edges
        elif type(item) == tuple and len(item) == 2:
            if item[0] in self.edges:
                return item[1] in self.edges[item[0]][0]
        else:
            return False     
     

    def __iter__(self):
        for key,value in sorted(self.edges.items(), key = lambda x : (self.degree(x[0]),x[0])):
            for item in sorted(value[0]):
                yield (key,item) 


    def __le__(self,right):
        for node,[value,key] in self.edges.items():
            if node not in right:
                return False
            for item in value:
                if (node,item) not in right:
                    return False
        return True
         
                    
         
 
    def __delitem__(self,item):
        if item in self.edges:
            node = item
            for destination in self[node]:
                self.edges[destination][1].remove(node)
            for key in self(node):
                self.edges[key][0].remove(node)
            del self.edges[node]
        elif type(item) is tuple and len(item) == 2 and item[0] in self.edges and item[1] in self.edges:
            key,destination = item
            if key in self and destination in self[key]:
                self.edges[key][0].remove(destination)        
                self.edges[destination][1].remove(key)        
        else: 
            raise GraphError('Graph.__delitem__: argument('+str(item)+') must be string or 2-tuple naming to nodes')
 
   
 
 
     
##############################
 
 
if __name__ == '__main__':
    # Put code here for simpler debugging of exceptions (comapred to bsc.txt)
#     g = Graph()
#     g['a'] = 'b'
#     print(g)
#     g.contains(('a','b'))

    
    import driver
    #Uncomment the following lines to see MORE details on exceptions
    #But probably better to write code above
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
    driver.driver()
