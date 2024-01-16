class Solution:
    def isPalindrome(self, s: str) -> bool:
        return ''.join(char for char in s if char.isalnum()).lower() == ''.join(char for char in s if char.isalnum())[::-1].lower()