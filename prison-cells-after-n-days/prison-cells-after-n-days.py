class Solution:
    
    def update(self,cells):
        cell_day = [0]*len(cells)
        
        for cell_indx in range(1,len(cells)-1):
            if (cells[cell_indx-1] == 0 and cells[cell_indx+1] == 0) or (cells[cell_indx-1] == 1 and cells[cell_indx+1] == 1):
                cell_day[cell_indx] = 1
            else:
                cell_day[cell_indx] = 0
        cell_day[0] = 0
        cell_day[-1] = 0
        
        return cell_day
    
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen = dict()
        ff = False
        while n > 0:
            # we only need to run the fast-forward once at most
            if not ff:
                state_key = tuple(cells)
                if state_key in seen:
                    # the length of the cycle is seen[state_key] - N 
                    n %= seen[state_key] - n
                    is_fast_forwarded = True
                else:
                    seen[state_key] = n

            # check if there is still some steps remained,
            # with or without the fast-forwarding.
            if n > 0:
                n -= 1
                cells = self.update(cells)

        return cells