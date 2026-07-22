class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)

        if m < n: return ""

        t_map , window_map = {} , {}
        for c in t:
            t_map[c] = t_map.get(c,0) + 1
        res_len = float('inf')
        result = [-1,-1]
        need , have = len(t_map) , 0
        l = 0
        for r in range(m):
            
            window_map[s[r]] = window_map.get(s[r],0) + 1
            
            if s[r] in t_map and window_map[s[r]] == t_map[s[r]]:
                have += 1
            
            while have == need:
                if res_len > (r - l + 1):
                    res_len = r - l + 1
                    result[0] = l
                    result[1] = r+1 # r is included

                window_map[s[l]] -= 1

                if s[l] in t_map and window_map[s[l]] < t_map[s[l]]:
                    have -= 1
                l += 1
        
        return s[result[0] : result[1]]

        