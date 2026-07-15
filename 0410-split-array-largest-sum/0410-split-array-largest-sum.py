class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def isValid(mid):

            stu , pages = 1 , 0

            for i in range(len(nums)):
                if (nums[i] > mid):
                    return False
                if (pages + nums[i] <= mid):
                    pages += nums[i]
                else:
                    stu += 1
                    pages = nums[i]
            
            return stu <= k


        l , r = 0 , sum(nums)
        ans = -1

        while l <= r:

            mid = (l + r) // 2

            if isValid(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans

