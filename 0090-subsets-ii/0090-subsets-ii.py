class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        ans = []
        n = len(nums)
        nums.sort()

        def subset(i, ans , curr):

            if i == n :
                ans.append(curr.copy())
                return
            
            curr.append(nums[i])
            subset(i+1, ans, curr)
            curr.pop()
            i += 1
            while i < n and nums[i] == nums[i-1]:
                i += 1
            subset(i, ans, curr) 


        subset(0, ans, [])

        return ans 

