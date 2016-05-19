import sys
from graph import Graph

def main(argv = None):
	v = ['A', 'B', 'C', 'D']
	e = [('A','B'),('B','C'),('A','D')]

	G = Graph(v,e)

	#G.printNodes()
	#G.printVertices()
	#G.printEdges()
	print G.getNode('A').getAdjacent()
	#G.spanningTree('A')s

if __name__ == "__main__":
    sys.exit(main())