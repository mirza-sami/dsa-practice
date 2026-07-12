class Solution:
    def trap(self, height: List[int]) -> int:

        # Brute Force
        
        # count = 0
        # for i in range(1 , len(height)-1):
        #     l = i-1
        #     r = i +1
        #     for j in range(i-1, -1, -1):
        #         if height[j] > height[l]:
        #             l = j
        #     for k in range(i+1 , len(height)):
        #         if height[k] > height[r]:
        #             r = k
        #     H = min(height[l],height[r])
        #     water = H - height[i]
        #     if water > 0: count += water
        # return count
        size = len(height)

        l_max = [0]*size
        l_max[0] = height[0]
        
        r_max = [0]*size
        r_max[size-1] = height[size-1]

        for i in range(1 , size):
            l_max[i] = max(l_max[i-1] , height[i])

        for j in range(size-2, -1, -1):
            r_max[j] = max(r_max[j+1] , height[j])

        count = 0

        for k in range(size):
            H = min(l_max[k], r_max[k])
            water = H - height[k]
            if water > 0: count += water
        return count 