
class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList:
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

	def append(self, value):
		new_node = Node(value)

		if self.head is None:
			self.head = new_node
			self.tail = new_node
		else:
			self.tail.next = new_node
			self.tail = new_node

		self.length += 1

		return True

	def pop_back(self):

		# Check to see if linked list is empty
		if self.length == 0:
			return None
		
		# Pop last one
		current = self.head
		prev = current
		while current.next is not None:
			prev = current
			current = current.next

		self.tail = prev
		self.tail.next = None
		self.length -= 1

		# In the case that there was only one node in Linked List
		if self.length == 0:
			self.head = None
			self.tail = None
		
		return current
	
	def pop_front(self):

		# Case 1: No items in linked list
		if self.length == 0:
			return None
		
		# Case 2: More than 1 node in linked list
		temp = self.head
		self.head = self.head.next
		temp.next = None
		self.length -= 1

		# Case 3: Only one item on LL --> Fixes tail to point to None
		if self.length == 0:
			self.tail = None
		
		return temp
		
	def prepend(self, value):

		new_node = Node(value)
		if self.length == 0:
			self.head = new_node
			self.tail = new_node
		else:
			new_node.next = self.head
			self.head = new_node
		
		self.length += 1
		return True
	
	def get(self, index):
		if index >= self.length or index < 0:
			return None
		
		current = self.head
		for _ in range(index):
			current = current.next
		
		return current

	def set_value(self, index, value):
		temp = self.get(index)
		if temp:
			temp.value = value
			return True
		return False

	def insert(self, index, value):
		# Check if index wihtin bounds
		if index > self.length or index < 0:
			return False 
		# Check to see if inserting at beginning or end
		if index == 0:
			return self.prepend(value)
		if index == self.length:
			return self.append(value)

		# Insert in between other nodes
		temp = self.get(index-1)
		new_node = Node(value)
		new_node.next = temp.next
		temp.next = new_node

		# Increment length
		self.length += 1

		return True	
	
	def remove(self, index):

		if index >= self.length or index < 0:
			return None 
		
		if index == 0:
			return self.pop_front()
		if index == self.length:
			return self.pop_back()
		
		prev = self.get(index-1)
		current = prev.next

		prev.next = current.next
		current.next = None

		self.length -= 1

		return current 

	def reverse(self):

		# Reverse head and tail
		temp = self.head
		self.head = self.tail
		self.tail = temp

		before = None
		after = temp.next

		for _ in range(self.length):
			after = temp.next
			temp.next = before
			before = temp
			temp = after
		return True




myll = LinkedList(4)
myll.append(5)
myll.prepend(7)
myll.print()
# print(myll.pop_front())
# print(myll.pop_front())
# print(myll.pop_front())
# print(myll.pop_front())

print("---------------------------------")
myll.insert(1,23)
myll.print()

print("---------------------------------")
print(myll.reverse())
myll.print()