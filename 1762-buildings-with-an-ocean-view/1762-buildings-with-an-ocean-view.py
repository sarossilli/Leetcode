class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        result = list()
        highest = 0 
        for index,height in enumerate(heights[::-1]):
            originalIndex = len(heights) - index-1
            if height > highest:
                result.append(originalIndex)
            highest = max(highest,height)
            
        return result[::-1]