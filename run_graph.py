from graph import Graph

v = ['A', 'B', 'C', 'D']
e = [('A','B'),('B','C'),('A','D')]

G = Graph(v,e)

#G.printNodes()
#G.printVertices()
#G.printEdges()
#print G.getNode('Q').getAdjacent()
G.spanningTree('A')