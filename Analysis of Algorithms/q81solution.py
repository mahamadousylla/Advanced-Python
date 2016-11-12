from performance import Performance
from goody import irange
from graph_goody import random_graph,spanning_tree

# Put script below to generate data for Problem #1
# In case you fail, the data appears in sample8.pdf in the helper folder


def create_random(n):
    global edges
    edges = random_graph(n, lambda n: 10*n)

    
for i in irange(1,8) :
    n = 1000 * 2**i
    p = Performance(lambda : spanning_tree(edges), lambda : create_random(n),5,'Spanning Tree of size {}'.format(n))
    p.evaluate()
    p.analyze()
    