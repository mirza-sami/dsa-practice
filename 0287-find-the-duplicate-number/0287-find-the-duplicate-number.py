class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # for i in range(len(nums)-1):
        #     for j in range(i +1 , len(nums)):
        #         if nums[i] == nums[j] :
        #             return nums[i]


        slow , fast = 0 , 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow

