class Solution:
    def reverseWords(self, s: str) -> str:

        # Pythonic way
        # return " ".join(s.split()[::-1])

        # manual way

        word , words = [] , []

        for ch in s:
            if ch != ' ':
                word.append(ch)
            elif word:
                words.append("".join(word))
                word = []
        
        if word:
            words.append("".join(word))
        words.reverse()

        return " ".join(words)