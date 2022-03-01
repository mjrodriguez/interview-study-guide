from tkinter import N


from typing import List

class solution:
	def moveZeroes(self, nums: List[int]):
		
		nz = 0 # Count the nonzero entries
		for n in nums:
			if n != 0:
				nums[nz] = n
				nz += 1
			
		for i in range(nz,len(nums)):
			nums[i] = 0
		return nums

s = solution()
print(s.moveZeroes([0,2,0,1,4]))