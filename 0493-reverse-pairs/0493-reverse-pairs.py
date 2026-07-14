class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        # Brute force

        # count = 0
        # size = len(nums)

        # for i in range(size - 1):
        #     for j in range(i+1, size):
        #         if nums[i] > 2*nums[j]: count += 1
        
        # return count

        # optimize

        def merge_sort(left: int, right: int) -> int:
            # Base case: if the segment has 1 or fewer elements, no pairs exist
            if left >= right:
                return 0
            
            mid = (left + right) // 2
            
            # Count pairs in the left half and right half recursively
            count = merge_sort(left, mid) + merge_sort(mid + 1, right)
            
            # Count cross-pairs where i is in left half and j is in right half
            j = mid + 1
            for i in range(left, mid + 1):
                # Advance j as long as the condition holds
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1
                # The number of valid j elements for this i is exactly j - (mid + 1)
                count += (j - (mid + 1))
            
            # Standard Merge process: combine the two sorted halves
            temp = []
            i, j = left, mid + 1
            
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
                    
            # Collect any remaining elements from both halves
            while i <= mid:
                temp.append(nums[i])
                i += 1
            while j <= right:
                temp.append(nums[j])
                j += 1
                
            # Copy the sorted temp array back into the original array
            nums[left:right + 1] = temp
            
            return count

        return merge_sort(0, len(nums) - 1)