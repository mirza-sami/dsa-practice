class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if not len(s) == len(t): return False

        sorted_s = sorted(s)
        sorted_t = sorted(t)

        for i,ch in enumerate(sorted_s):
            if ch != sorted_t[i]:
                return False
        
        return True