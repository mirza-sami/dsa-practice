class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        longestP = strs[0]
        length1 = len(longestP)
        if len(strs) == 1: return longestP

        for i in range(1,len(strs)):
            length2 = len(strs[i])
            if length2 < length1:
                length1 , length2 = length2, length1
            same = 0
            for j in range(length1):
                if longestP[j] == strs[i][j]:
                    same += 1
                else:
                    break
            if same == 0:
                return ""
            else:
                longestP = longestP[:same]
                length1 = len(longestP)
        
            
        return longestP