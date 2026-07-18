class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        position.sort()
        def isValid(mid):
            n = len(position)
            balls = 1
            lastP = position[0]
            for i in range(n):
                if position[i] - lastP >= mid:
                    lastP = position[i]
                    balls += 1 

            return balls >= m


        l = 1
        r = position[-1] - position[0]
        ans = -1
        while l <= r:

            mid = (l + r) // 2
            if isValid(mid):
                l = mid + 1
                ans = mid
            else:
                r = mid - 1

        return ans
