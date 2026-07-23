class Solution:
    def longestPrefix(self, s: str) -> str:

        # if len(s) == 1: return ""

        # prefix , suffix = [] , []

        # for i in range(1 , len(s)):
        #     prefix.append(s[:i])
        
        # for j in range(len(s) -1 , 0, -1):
        #     suffix.append(s[j:])
        
        # for k in range(len(suffix)-1 , -1, -1):
        #     if prefix[k] == suffix[k]:
        #         return prefix[k]
        
        # return ""

        # another UNoptimized


        # if len(s) == 1: return ""

        # l , r = 0 , 1
        # restarting_pos = -1
        # while r < len(s):
        #     if s[l] == s[r]:
        #         if l == 0: 
        #             restarting_pos = r + 1 
        #         l += 1
        #         r += 1
        #     else:
        #         if l > 0:
        #             r = restarting_pos
        #             l = 0 
        #         else:
        #             r += 1
        
        # return s[: l]


        # Optimized
   
        lps = [0] * len(s)
        
        # length tracks the length of the previous longest prefix suffix
        length = 0 
        i = 1
        
        while i < len(s):
            if s[i] == s[length]:
                # If characters match, we extend the prefix length
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    # If there's a mismatch, fallback to the previous valid prefix length
                    # Notice we do NOT increment `i` here
                    length = lps[length - 1]
                else:
                    # If length is 0 and they still don't match, lps for this index is 0
                    lps[i] = 0
                    i += 1
                    
        # The last value in the lps array gives us the length of the longest 
        # prefix-suffix for the entire string.
        longest_length = lps[-1]
        
        return s[:longest_length]