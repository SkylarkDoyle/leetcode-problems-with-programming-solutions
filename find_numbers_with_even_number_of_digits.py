#Given an array nums of integers, return how many of them contain an even number of digits.

def findNumbers(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even_total = 0
        
        for i in range(len(nums)):
            #if the string length of each number divided by 2 == 0(even)
                if len(str(nums[i])) % 2 == 0:
                    #then add one to even total variable
                        even_total += 1
        return even_total
                        
nums = [555,901,482,1771]   
print('Numbers with Even Number of Digits = ', findNumbers(nums))

# Output => Numbers with Even Number of Digits =  1