
class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class queue:
	def __init__(self,value):
		new_node = Node(value)
		self.first = new_node
		self.last = new_node
		self.length = 1
	
	def print(self):
		temp = self.first
		while temp is not None:
			print(temp.value)
			temp = temp.next
		print("-----")

q = queue(4)
q.print()