import pylab as p
import networkx as nx

G = nx.Graph()
G.add_edge("A","B")
G.add_edge("A","H")
G.add_edge("H","C")
G.add_edge("B","C")
G.add_edge("B","D")

nx.draw(G)
p.show()