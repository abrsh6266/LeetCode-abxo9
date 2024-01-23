class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        y = s.strip()
        n = len(y)-1
        ss = 0
        for i in range(n,-1,-1):
            if y[i] == ' ':
                return ss
            ss  += 1
        return ss