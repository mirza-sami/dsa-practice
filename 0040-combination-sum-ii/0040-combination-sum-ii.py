class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        List = []
        # seen = set()

        def combination(i, curr, total):
            if target == total:
                # tup = tuple(curr.copy())
                # if tup not in seen:
                #     seen.add(tup)
                List.append(curr.copy())
                return
            if total > target or i > len(candidates)-1:
                return
            
            
            c  = candidates[i]
            curr.append(c)
            combination(i+1, curr, total + c)
            curr.pop()
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            combination(i+1, curr, total)
        
        combination(0, [] , 0)

        return List