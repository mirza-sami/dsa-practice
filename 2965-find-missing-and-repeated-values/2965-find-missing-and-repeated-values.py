class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        # find repeating
        seen = set()
        repeating = 0 

        for row in grid:
            for num in row:
                if num in seen:
                    repeating = num
                seen.add(num)
        


        # find the missing value

        actualSum = 0
        theoreticalSum = 0
        missingValue = 0
        length  = len(grid)

        for i in range(length):
            for j in range(length):
                actualSum += grid[i][j]

        for i in range(length*length):
            theoreticalSum += i+1        

        sameValue = abs(actualSum - repeating)
        missingValue = abs(theoreticalSum - sameValue)

        return [repeating , missingValue]