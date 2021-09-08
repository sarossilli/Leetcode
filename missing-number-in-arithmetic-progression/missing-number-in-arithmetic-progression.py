class Solution:
    def missingNumber(self, arr: List[int]) -> int:

        if arr[0] < arr[1]:
            diff = min(arr[1]-arr[0], arr[-1]-arr[-2])
        else:
            diff = max(arr[1]-arr[0], arr[-1]-arr[-2])
            
        if diff == 0:
            return arr[0]
        
        expected = sum([i for i in range(arr[0],arr[-1]+diff,diff)])
        actual = sum(arr)

        return expected-actual