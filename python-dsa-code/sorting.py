
def bubble_sort(input_list):
	# Worst Case: O(n^2)
	# Average Case: O(n^2)
	# n is length of input_list
	for i in range(len(input_list)-1,0,-1):
		for j in range(i):

			print("i = ", i, "j = ", j)
			if input_list[j] > input_list[j+1]:
				temp = input_list[j]
				input_list[j] = input_list[j+1]
				input_list[j+1] = temp
		
	return input_list

def selection_sort(input_list):
	# Worst case: O(n^2):

	for i in range(len(input_list)-1):
		min_index = i
		for j in range(i+1,len(input_list)):
			if input_list[j] < input_list[min_index]:
				min_index = j
		if min_index != i:
			temp = input_list[i]
			input_list[i] = input_list[min_index]
			input_list[min_index] = temp
	return input_list

def insertion_sort(input_list):
	# Worst case: O(n^2)
	# Best case: Almost sorted data O(n)
	for i in range(1,len(input_list)):
		temp = input_list[i]
		j = i-1
		while temp < input_list[j] and j > -1:
			input_list[j+1] = input_list[j]
			input_list[j] = temp
			j -= 1
	
	return input_list

def merge(list1, list2):
	# List1 and list2 should be sorted
	combined = []
	i = 0
	j = 0
	while i < len(list1) and j < len(list2):
		if list1[i] < list2[j]:
			combined.append(list1[i])
			i += 1
		else:
			combined.append(list2[j])
			j += 1
	
	while i < len(list1):
		combined.append(list1[i])
		i += 1
	
	while j < len(list2):
		combined.append(list2[j])
		j += 1
	
	return combined

def merge_sort(input_list):
	return 0



input = [4,2,6,5,1,3]

print("Input: ", input)
# print(bubble_sort(input))
# print("Output:", selection_sort(input))
print("Output:", insertion_sort(input))

print(merge([1,2,7,8],[3,4,5,6]))