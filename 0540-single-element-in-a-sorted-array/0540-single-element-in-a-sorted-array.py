class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        


        # index = 0
        # n = len(nums)
        # while index <= n-1:
        #     if index == n -1:
        #         return nums[n-1]
        #     if not nums[index] == nums[index + 1]:
        #         return nums[index]
        #     index += 2

        # optimized

        l = 0
        r = len(nums) - 1
        # edge cases
        if (l == r) : return nums[r]
        if not (nums[0] == nums[1]): return nums[0]
        if not (nums[r] == nums[r - 1]): return nums[r]
        
        while l <= r:
            
            mid = (l + r) // 2
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
    
            if mid % 2 == 1:
                if nums[mid] == nums[mid -1]:
                    l = mid + 1
                else:
                    r = mid -1
            else:
                if nums[mid] == nums[mid -1]:
                    r = mid -1
                else:
                    l = mid + 1
