"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The relative order of the elements may be changed.
"""

def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        #WHILE VALLUE IS IN THE LIST
        while val in nums:  
            #KEEP REMOVING THE VALUE UNTIL IT ISNT IN THE LIST
            nums.remove(val)

        return nums


nums = [3,2,2,3]
val = 3

print(removeElement(nums, val))


