
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
	if len(input_list) == 1:
		return input_list
	mid = int(len(input_list)/2)
	left = input_list[:mid]
	right = input_list[mid:]
	return merge(merge_sort(left),merge_sort(right))

def swap(list1, index1, index2):
	temp = list1[index1]
	list1[index1] = list1[index2]
	list1[index2] = temp

def pivot(list1, pivot_index, end_index):
	swap_index = pivot_index

	for i in range(pivot_index+1, end_index+1):
		if list1[i] < list1[pivot_index]:
			swap_index += 1
			swap(list1, swap_index, i)
		
	
	swap(list1, pivot_index, swap_index)
	return swap_index

def quick_sort_alg(list1, left, right):
	if left < right:
		pivot_index = pivot(list1, left, right)
		quick_sort_alg(list1,left, pivot_index-1)
		quick_sort_alg(list1,pivot_index+1,right)
	return list1

def quick_sort(list1):
	return quick_sort_alg(list1, 0, len(list1)-1)
input = [4,2,6,5,1,3]

print("Input: ", input)
# print(bubble_sort(input))
# print("Output:", selection_sort(input))
print("Output:", insertion_sort(input))

# print(merge([1,2,7,8],[3,4,5,6]))

print(merge_sort([3,1,4,2]))

l = [4, 6, 1, 7, 3, 2, 5]

print(l)
print(quick_sort(l))
