class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n > m: return False
        h1,h2 = [0] * 26, [0] * 26
        for i in range(n):
            h1[ord(s1[i]) - ord('a')] += 1
            h2[ord(s2[i]) - ord('a')] += 1
        match = 0
        for i in range(26):
            if h1[i] == h2[i]:
                match += 1
        l = 0
        for r in range(n,m):
            if match == 26: return True  
            t = ord(s2[r])-ord('a')
            h2[t] += 1
            if h2[t] == h1[t]:
                match +=1
            elif h1[t] + 1 == h2[t]:
                match -= 1
            t = ord(s2[l])-ord('a')
            h2[t] -= 1
            if h2[t] == h1[t]:
                match +=1
            elif h2[t] + 1 == h1[t]:
                match -= 1
            l += 1
        return match == 26