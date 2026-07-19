class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # if not len(s) == len(t): return False

        # sorted_s = sorted(s)
        # sorted_t = sorted(t)

        # for i,ch in enumerate(sorted_s):
        #     if ch != sorted_t[i]:
        #         return False
        
        # return True

        # optimized

        if not len(s) == len(t): return False

        countS , countT = {} , {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i],0) + 1
            countT[t[i]] = countT.get(t[i],0) +1
        
        return countS == countT
