class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the keys
        intervals.sort(key=lambda x: x[0])
        arr = intervals
        pointer = 0
        while len(arr) > pointer+1:
            pointer = check(arr, pointer)
        return arr
    
def check(arr,pointer):
    a,b = arr[pointer]
    c,d = arr[pointer+1]
    
    # a <= c (sorted)
    
    #overlaping [1,2] [2,4]
    # b >= c ?
    
    #included [1,4] [2,3]
    # b >= c ?
    # b >= d

	# check if element N+1 is within element N
	# Example: [1, 5], [2, 4]
    if c in range(a, b+1) and d in range(a, b+1):
        arr.pop(pointer+1)
        return pointer
    
    # check if the start of element N+1 is in range of element N and end is not in range of it.
	# example: [1, 5], [2, 6]
    elif c in range(a, b+1) and not d in range(a, b+1):
        arr.pop(pointer+1)
        arr[pointer] = [a, d]
        return pointer
    
    return pointer+1
    
    return pointer+1