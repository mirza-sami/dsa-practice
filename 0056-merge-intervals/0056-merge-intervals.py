class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. Sort the intervals based on start time
        intervals.sort(key=lambda x: x[0])
        
        merged = []

        for interval in intervals:
            # 2. If 'merged' is empty, OR there is no overlap with the last interval in 'merged':
                # Append the current interval to 'merged'
            
            if not merged or (not merged[len(merged)-1][1] >= interval[0]):
                merged.append(interval)
            # 3. Else (there is an overlap):
                # Update the end time of the last interval in 'merged' 
                # to be the max of its current end time and the new interval's end time
                
            else :
                merged[len(merged)-1][1] = max(interval[1] , merged[len(merged)-1][1] )
            
        return merged