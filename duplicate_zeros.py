
def duplicateZeros(arr):
    """
    :type arr: List[int]
    :rtype: None Do not return anything, modify arr in-place instead.
    """
    length_of_arr = len(arr)
    i = 0
    
    while i < length_of_arr:
            #if the current element in the array is 0 
            if arr[i] == 0:
                    #then insert zero to the next element
                    arr.insert(i + 1, 0)
                    i += 1
                    #increment by 1 then remove the next element bcs it isnt needed anymore
                    arr.pop()
            i += 1
    return arr
    
arr = [1,0,2,3,0,4,5,0]

print(duplicateZeros(arr))




    
                
               