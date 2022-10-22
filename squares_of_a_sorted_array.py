# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

def sortedSquares(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    new_list = []
    for i in nums:
            square = i ** 2
            new_list.append(square)
            new_list.sort()
    return new_list


nums = [-7,-3,2,3,11]
print('Squares of a Sorted Array = ', sortedSquares(nums))


#Output => Squares of a Sorted Array =  [4, 9, 9, 49, 121]
        