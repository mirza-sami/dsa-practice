class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        index = 0
        while i < len(chars):

            count = 0
            ch = chars[i]

            while i < len(chars) and chars[i] == ch:
                count += 1
                i += 1
            chars[index] = ch
            index += 1
            count_str = str(count)
            if not count == 1:
                for c in count_str:
                    chars[index] = c
                    index += 1
        
        del chars[index:]

        return index