# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.


# Time Complexity: O(n)
class Solution(object):
    def __init__(self) -> None:
        pass

    def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        #the mth positon element to the end of the list is replaced with second list from beginning to nth position of element
        nums1[m:] = nums2[:n]
        
        #then sort the merge list
        nums1.sort()

        return nums1

#test with any array input
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3


print(Solution.merge(nums1, m, nums2, n))

#Output => [1, 2, 2, 3, 5, 6] |excluding the zeroes|
