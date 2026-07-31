class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = "".join(char.lower() for char in s if char.isalnum())
        return news==news[::-1]