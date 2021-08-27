class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def solve(targetLeft,combo,indx):
            if targetLeft == 0:
                res.append(list(combo))
                return
            elif targetLeft<0:
                return
            for i in range(indx,len(candidates)):
                combo.append(candidates[i])
                solve(targetLeft-candidates[i],combo,i)
                combo.pop()
            
        solve(target,[],0)
        return res