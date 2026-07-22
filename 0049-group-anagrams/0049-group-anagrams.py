class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # correct but gives TLE

        # group = 0
        # index = 0 # for each group
        # anagrams = []
        # for i in range(len(strs)):

        #     if strs[i] == 0: continue

        #     current_group = [strs[i]]
        #     sorted_i = sorted(strs[i])

        #     for j in range(i+1, len(strs)):
        #         if strs[j] == 0: 
        #             continue

        #         sorted_j = sorted(strs[j])
        #         if sorted_i == sorted_j:
        #             current_group.append(strs[j]) # 
        #             strs[j] = 0 # Mark as visited so we don't use it again

        #     anagrams.append(current_group)

        # return anagrams

        # optimized

        anagram = {}

        for word in strs:

            key = tuple(sorted(word))

            if key not in anagram:
                anagram[key] = []
            
            anagram[key].append(word)
        
        return list(anagram.values())