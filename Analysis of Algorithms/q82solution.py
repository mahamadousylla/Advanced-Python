import cProfile
from graph_goody import random_graph, spanning_tree
import pstats

# Put script below to generate data for Problem #2
# In case you fail, the data appears in sample8.pdf in the helper folder

graph = random_graph (50000, lambda n : 10*n)
cProfile.run('spanning_tree(graph)','profile50K')
p = pstats.Stats('profile50K')
p.strip_dirs().sort_stats('ncalls').print_stats()

graph = random_graph (100000, lambda n : 10*n)
cProfile.run('spanning_tree(graph)','profile100K')
p = pstats.Stats('profile100K')
p.strip_dirs().sort_stats('time').print_stats()