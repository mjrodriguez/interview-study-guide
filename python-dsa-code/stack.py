class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class stack:
	def __init__(self,value):
		new_node = Node(value)
		self.top = new_node
		self.height = 1

	def print(self):
		temp = self.top
		while temp is not None:
			print(temp.value)
			temp = temp.next	
		print("-----")
	
	def push(self, value):
		new_node = Node(value)
		if self.height == 0:
			self.top = new_node
		else:
			new_node.next = self.top
			self.top = new_node
		
		self.height += 1
		return True
	
	def pop(self):
		if self.height == 0:
			return None

		temp = self.top
		self.top = temp.next
		temp.next = None
		
		self.height -= 1
		return temp


s = stack(4)
s.push(3)
s.print()
s.pop()
s.pop()
s.pop()
s.print()