class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        answer = [1] * n
        
        leftProduct = 1
        for i in range(n):
            answer[i] = leftProduct
            leftProduct *= nums[i]

        rightProduct = 1
        for i in range(n-1 , -1 , -1):
            answer[i] *= rightProduct
            rightProduct *= nums[i]
        
        return answer