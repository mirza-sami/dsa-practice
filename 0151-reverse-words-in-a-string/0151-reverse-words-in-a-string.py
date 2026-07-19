class Solution:
    def reverseWords(self, s: str) -> str:

        # Pythonic way
        return " ".join(s.split()[::-1])