class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergeSort(nums, l, r):
            if l < r:
                mid = (l + r) // 2

                mergeSort(nums, l, mid)
                mergeSort(nums, mid+1, r)

                merge(nums[l:mid+1], nums[mid+1:r+1], l, r)


        def merge(a,b, l, r):

            m,n = len(a), len(b)
            i,j = 0, 0 
            k = l

            while i < m and j < n:
                if a[i] <= b[j]:
                    nums[k] = a[i]
                    i += 1
                else:
                    nums[k] = b[j]
                    j += 1
                
                k += 1
            
            while i < m:
                nums[k] = a[i]
                i += 1
                k += 1

            while j < n:
                nums[k] = b[j]
                j += 1
                k += 1





        mergeSort(nums, 0, len(nums)-1)

        return nums