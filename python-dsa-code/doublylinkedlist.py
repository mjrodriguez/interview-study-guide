
class Node:
	def __init__(self, value):
		self.value = value
		self.next = None
		self.prev = None

class DoublyLinkedList:

	def __init__(self, value):
		new_node = Node(value)
		self.head = new_node
		self.tail = new_node
		self.length = 1
	
	def print(self):
		current = self.head
		while current is not None:
			print(current.value)
			current = current.next
		print("-----")

	def append(self, value):
		new_node = Node(value)
		if self.head is None:
			self.head = new_node
			self.tail = new_node
		else:
			self.tail.next = new_node
			new_node.prev = self.tail
			self.tail = new_node

		self.length += 1

		return True
	
	def pop_back(self):
		if self.length == 0:
			return None

		temp = self.tail
		if self.length == 1:
			self.head = None
			self.tail = None
		else:
			self.tail = temp.prev
			self.tail.next = None
			temp.prev = None

		self.length -= 1

		return temp
	
	def prepend(self, value):
		new_node = Node(value)
		if self.head is None:
			self.head = new_node
			self.tail = new_node
		else:
			new_node.next = self.head
			self.head.prev = new_node
			self.head = new_node
		
		self.length += 1
		return True

	def pop_front(self):
		if self.length == 0:
			return None
		temp = self.head
		if self.length == 1:
			self.head = None
			self.tail = None
		else:
			self.head = temp.next
			temp.next = None
			self.head.prev = None
		
		self.length -= 1

		return temp
			

dll = DoublyLinkedList(7)
dll.append(2)
dll.prepend(1)
dll.print()
print(dll.pop_front())
print(dll.pop_front())
print(dll.pop_front())
print(dll.pop_front())