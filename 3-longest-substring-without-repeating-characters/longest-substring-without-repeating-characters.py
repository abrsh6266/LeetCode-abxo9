class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        start = 0
        n = len(s)
        maxi = 0
        for i in range(n):
            if s[i] in chars and chars[s[i]] >= start:
                start = chars[s[i]]+1
            chars[s[i]] = i
            maxi = max(maxi,i-start+1)
        return maxi