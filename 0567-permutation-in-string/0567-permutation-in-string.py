class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        letters = [0]*26
        letters2 = [0]*26

        for c in s1:
            letters[ord(c)- ord('a')] +=1
        for i in range( len(s1)):
            letters2[ord(s2[i])- ord('a')] +=1

        if letters == letters2: return True

        for i in range(len(s1), len(s2)):
            prev_i = i-len(s1)
            letters2[ord(s2[prev_i])- ord('a')] -=1
            letters2[ord(s2[i])- ord('a')] +=1
            if letters == letters2: return True
        
        return False