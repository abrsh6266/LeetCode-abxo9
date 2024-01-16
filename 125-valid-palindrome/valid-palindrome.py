class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ''.join(char for char in s if char.isalnum()).lower()
        y = x[::-1]
        return x == y