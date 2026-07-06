class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # length = 0
        # startIndex = 0
        # endIndex = 0
        # size = len(s)

        # while endIndex < size - 1:
        #     if not s[endIndex + 1] in s[startIndex:endIndex]:
        #         length +=1
        #         endIndex += 1
        #     else:
        #         length = 1
        #         endIndex += 1
        #         startIndex = endIndex
        # return length

        left = 0
        charSet = set()
        length = 0

        for right in range(len(s)):

            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1

            charSet.add(s[right])
            length = max(length , len(charSet))

        return length