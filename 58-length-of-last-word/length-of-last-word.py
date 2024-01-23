class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split()
        return len(l.pop())