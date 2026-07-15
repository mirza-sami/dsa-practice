class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        index = 0
        n = len(nums)
        while index <= n-1:
            if index == n -1:
                return nums[n-1]
            if not nums[index] == nums[index + 1]:
                return nums[index]
            index += 2
