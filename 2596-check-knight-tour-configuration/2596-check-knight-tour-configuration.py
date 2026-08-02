class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:

        def checkBounds(r, c):
            rows = len(grid) - 1
            cols = len(grid[0]) - 1
            if (r < 0) or (c < 0) or (r > rows) or (c > cols ):
                return False
            return True

        def getNextPos(r, col, val):

            if checkBounds(r-1, col+2) and grid[r-1][col+2] == val:
                if val == (len(grid)*len(grid)) - 1:
                    return True
                return checkPos(r-1, col+2, val)

            if checkBounds(r+1, col+2) and grid[r+1][col+2] == val:
                if val == (len(grid)*len(grid)) - 1:
                    return True
                return checkPos(r+1, col+2, val)

            if checkBounds(r+1, col-2) and grid[r+1][col-2] == val:
                if val == (len(grid)*len(grid)) - 1:
                    return True
                return checkPos(r+1, col-2, val)

            if checkBounds(r-1, col-2) and grid[r-1][col-2] == val:
                if val == (len(grid)*len(grid)) - 1:
                    return True
                return checkPos(r-1, col-2, val)

            if checkBounds(r+2, col+1) and grid[r+2][col+1] == val:
                if val == (len(grid)*len(grid)) - 1:
                    return True
                return checkPos( r+2, col+1, val)

            if checkBounds(r+2, col-1) and grid[r+2][col-1] == val:
                if val == (len(grid)*len(grid)) - 1:
                    return True
                return checkPos(r+2, col-1, val)

            if checkBounds(r-2, col+1) and grid[r-2][col+1] == val:
                if val == (len(grid)*len(grid)) - 1:
                    return True
                return checkPos(r-2, col+1, val)

            if checkBounds(r-2, col-1) and grid[r-2][col-1] == val:
                if val == (len(grid)*len(grid)) - 1:
                    return True
                return checkPos(r-2, col-1, val)
            
            return False

        def checkPos(row, col, curr):
            nextV = curr + 1
            return getNextPos(row, col, nextV)

        if grid[0][0] != 0:
            return False

        return checkPos(0, 0, grid[0][0])