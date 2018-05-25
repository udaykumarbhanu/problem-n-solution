class Node(object):
	def __init__(self, data=None):
		self.left = None
		self.data = data
		self.right = None

	def print_node(self):
		return self.data

single_node = Node(20)
print single_node.print_node()
