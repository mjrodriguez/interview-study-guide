class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class BinarySearchTree:
	def __init__(self):
		self.root = None

	def insert(self, value):
		new_node = Node(value)
		if self.root is None:
			self.root = new_node
			return True

		temp = self.root
		while True:
			if new_node == temp:
				return False

			if new_node.value < temp.value:
				if temp.left is None:
					temp.left = new_node
					return True
				temp = temp.left	
			else:
				if temp.right is None:
					temp.right = new_node
					return True
				temp = temp.right
	
	def contains(self, value):
		
		if self.root is None:
			return False
		
		temp = self.root
		while temp is not None:
			if value == temp.value:
				return True
			elif value < temp.value:
				temp = temp.left
			elif value > temp.value:
				temp = temp.right
			
		return False
	
	def min_value_node(self, current_node):
		while current_node.left is not None:
			current_node = current_node.left

		return current_node
			



bst = BinarySearchTree()
bst.insert(47)
bst.insert(21)
bst.insert(76)
bst.insert(18)
bst.insert(27)
bst.insert(52)
bst.insert(82)

print(bst.root.value)
print(bst.root.left.value)
print(bst.root.right.value)

print("----")

print(bst.contains(5))


print( bst.min_value_node(bst.root).value)
print( bst.min_value_node(bst.root.right).value)

num = 1152

x = num // 1000

print("x = ", x)

