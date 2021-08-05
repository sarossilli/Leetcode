class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        counts = []
        for edge in edges:
            for node in edge:
                if node in counts:
                    return node
                else:
                    counts.append(node)
                