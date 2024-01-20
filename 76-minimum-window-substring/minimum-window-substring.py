class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        if t == '':
            return ''
        ct, w = {},{}
        for c in t:
            ct[c] = 1 + ct.get(c,0)
        res,rl = [-1,-1],float('inf')
        n,h = len(ct),0
        l = 0
        for r in range(m):
            x = s[r]
            w[x] = 1 + w.get(x,0)
            if x in ct and w[x] == ct[x]:
                h += 1
            while h == n:
                if (r-l+1) < rl:
                    res = [l,r]
                    rl = r-l+1
                w[s[l]] -= 1
                if s[l] in ct and w[s[l]] < ct[s[l]]:
                    h -= 1
                l += 1
        l,r = res
        return s[l:r+1] if rl != float('inf') else ""