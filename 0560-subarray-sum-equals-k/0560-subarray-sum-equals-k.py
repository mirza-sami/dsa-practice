class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # size = len(nums)
        # count = 0

        # for i in range(size):
        #     for j in range(i , size):
        #         if sum(nums[i:j+1]) == k:
        #             count +=1
            
        # return count


        count = 0
        currentSum = 0

        prefixSum = {0 : 1}

        for num in nums:
            currentSum +=num
            diff = currentSum - k

            if diff in prefixSum:
                count += prefixSum.get(diff, 0)
            
            prefixSum[currentSum] = 1 + prefixSum.get(currentSum, 0)
        
        return count