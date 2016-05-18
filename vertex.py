class Vertex(object):
	name = ''
	adj = []

	def __init__(self, n, ad):
		self.name = n
		self.adj = ad

	def getAdjacent(self):
		return self.adj