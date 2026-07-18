class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # cleaned = [c.lower() for c in s if c.isalnum()] 

        # return cleaned == cleaned[::-1]

        # optimizsd

        l = 0
        h = len(s) - 1

        while l < h:
            while l<h and not s[l].isalnum():
                l += 1
            while l < h and not s[h].isalnum():
                h -=1
            if s[l].lower() != s[h].lower():
                return False
            else:
                l += 1
                h -= 1

        return True