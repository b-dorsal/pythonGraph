import Queue
from vertex import Vertex

class Graph(object):
	nodes = []		#Vertex objects

	vertices = []	#Chars
	edges = []		#2-tuple Chars

	def __init__(self, V, E):
		self.vertices = V
		self.edges = E

		for v in self.vertices:
			temp = []
			
			for e in self.edges:
				if e[0] == v:
					temp.append(e[1])
				if e[1] == v:
					temp.append(e[0])

			v = Vertex(v, temp)
			self.nodes.append(v)


	#def spanningTree(self, node):
		


	def getNode(self, name):
		v = Vertex(None, None)
		for node in self.nodes:
			if node.name == name:
				v = node
		return v

	def printNodes(self):
		for n in self.nodes:
			print n.name, "\t", n.getAdjacent()

	def printVertices(self):
		for v in self.vertices:
			print v

	def printEdges(self):
		for e in self.edges:
			print e[0], e[1]

	def listHas(self, el, li):
		for e in li:
			if e == el:
				return True
		return False