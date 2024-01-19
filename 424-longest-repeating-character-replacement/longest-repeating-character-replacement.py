class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h = {}
        l = 0
        m = 0
        res = 0
        n = len(s)
        for r in range(n):
            h[s[r]] = 1 + h.get(s[r],0)
            m = max(m,h[s[r]])
            while (r-l+1) - m > k:
                h[s[l]] = h[s[l]] - 1
                l += 1
            res = max(r-l+1,res) 
        return res

        