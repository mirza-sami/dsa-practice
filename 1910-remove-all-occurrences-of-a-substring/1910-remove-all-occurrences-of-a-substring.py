class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        l = len(part)
        stack = []
        part_list = list(part)
        for c in s:
            stack.append(c)
            if len(stack) >= l and stack[-l:] == part_list:
                
                del stack[-l:]
        
        return "".join(stack)