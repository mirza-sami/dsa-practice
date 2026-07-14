class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        l = 1
        r = len(arr) - 2

        while l <= r:

            mid = l +((r-l)//2) 
            
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            
            if arr[mid] > arr[mid - 1]:
                l = mid + 1
            else:
                r = mid - 1
        
        return - 1