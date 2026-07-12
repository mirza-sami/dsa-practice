class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
       
       # Brute force
       
        # l = 0
        # r = k-1
        # size = len(nums)
        # output = [0]*(size-(k-1))
        # index = 0
        
        # while r <= size-1:
        #     maximum = nums[l]
        #     for j in range(l, r+1):
        #         maximum = max(maximum , nums[j])
    
        #     output[index] = maximum
        #     index += 1
        #     r += 1
        #     l += 1

        # return output


        # optimized

        
        size = len(nums)
        output = []
        q = collections.deque()
        
        for i in range(size):
           
            if q and q[0] < i-k+1:
                q.popleft()

            while q and nums[q[-1]] < nums[i]:
                q.pop()
            
            q.append(i)

            if i >= k - 1:
                output.append(nums[q[0]])

        return output