class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # result =[]
        # nums.sort()
        # size = len(nums)
        # for a in range(size):
        #     if a > 0 and nums[a] == nums[a-1]:
        #         continue
        #     for b in range(a+1,size):
        #         if b > a+1 and nums[b] == nums[b-1]:
        #             continue
        #         for c in range(b+1, size):
        #             if c > b+1 and nums[c] == nums[c-1]:
        #                 continue
        #             for d in range(c+1, size):
        #                 if d > c+1 and nums[d] == nums[d-1]:
        #                     continue
        #                 if nums[a] + nums[b] + nums[c] + nums[d] == target and a!=b and b!=c and c!=d and a!= d and a!=c and b!=d:
        #                     result.append([nums[a], nums[b], nums[c], nums[d]])

        # return result


        result =[]
        nums.sort()
        size = len(nums)
        for a in range(size):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            for b in range(a+1,size):
                if b > a+1 and nums[b] == nums[b-1]:
                    continue
                l , r = b+1 , size -1
                while l < r:
                    if nums[a] + nums[b] + nums[l] + nums[r] == target:
                        result.append([nums[a], nums[b], nums[l], nums[r]])
                        l +=1
                        while l < r and nums[l] == nums[l-1]:
                            l +=1
                    elif nums[a] + nums[b] + nums[l] + nums[r] > target:
                        r -=1
                    else:
                        l +=1

        return result