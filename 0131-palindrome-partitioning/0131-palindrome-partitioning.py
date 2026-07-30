class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(st, l, r):

            while l <= r:
                if st[l] != st[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        res = []
        def partitioning(ind, curr, s):

            if ind == len(s):
                res.append(curr.copy())
                return

            for i in range(ind,len(s)) :
                if isPalindrome(s, ind, i):
                    curr.append(s[ind : i+1])
                    partitioning(i+1, curr, s)
                    curr.pop()




        partitioning(0, [], s)
        return res