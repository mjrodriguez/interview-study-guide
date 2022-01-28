class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class stack:
	def __init__(self,value):
		new_node = Node(value)
		self.top = new_node
		self.height = 1

	