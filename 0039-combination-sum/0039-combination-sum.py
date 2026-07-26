class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        List = []

        def combination(i, curr, total):
            if target == total:
                List.append(curr.copy())
                return
            if total > target or i > len(candidates)-1:
                return
            
            c  = candidates[i]
            curr.append(c)
            combination(i, curr, total + c)
            curr.pop()
            combination(i+1, curr, total)
        
        combination(0, [] , 0)

        return List