class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
       # brute force
       
        # nums1.extend(nums2)
        # nums1.sort()
        # n = len(nums1)
        # if n % 2 == 1:
        #     return nums1[(n//2)]
        # else:
        #     i = (n // 2)
        #     return (nums1[i-1] + nums1[(i+1)-1]) / 2 

        # optimal

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        a = len(nums1) 
        b = len(nums2)  

        half = (a+b+1)//2
        l = 0
        h = a
        while l<=h:
            mid = (l+h) // 2
            mid2 = half - mid

            l1 = float('-inf') if mid == 0 else nums1[mid-1] 
            r1 = float('inf') if mid == a else nums1[mid] 
            l2 = float('-inf') if mid2 == 0 else nums2[mid2-1] 
            r2 = float('inf') if mid2 == b else nums2[mid2]

            if l1<=r2 and l2 <= r1:
                if (a+b) % 2 == 1:
                    return float((max(l1,l2)))
                else:
                    return ((max(l1,l2) + min(r1,r2))/2.0)
            elif l1>r2:
                h = mid -1
            else:
                l = mid+1