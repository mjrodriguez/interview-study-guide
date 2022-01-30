
from re import I


class HashTable:
	def __init__(self,size=7):
		self.data_map = [None]*size
	
	def __hash(self, key):
		my_hash = 0
		for letter in key:
			my_hash = (my_hash + ord(letter)*23) % len(self.data_map)
		
		return my_hash
	
	def print(self):
		for i, val in enumerate(self.data_map):
			print(i, ": ", val)
	
	def set(self, key, value):
		index = self.__hash(key)
		if self.data_map[index] == None:
			self.data_map[index] = []
		
		self.data_map[index].append([key, value])
	
	def get(self, key):
		index = self.__hash(key)
		if self.data_map[index] is not None:
			for i in range(len(self.data_map[index])):
				if self.data_map[index][i][0] == key:
					return self.data_map[index][i][1]
		return None
	
	def keys(self):
		all_keys = []
		for i in range(len(self.data_map)):
			if self.data_map[i] is not None:
				for j in range(len(self.data_map[i])):
					all_keys.append(self.data_map[i][j][0])
		
		return all_keys


h = HashTable()
h.set('bolts', 1400)
h.set('washers', 50)
h.set('lumber',70)

# print(h.get('bolts'))
# print(h.get('washers'))
# print(h.get('lumber'))

print(h.keys())

h.print()