class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = "".join(char.lower() for char in s if char.isalnum())
        l = len(news)
        for i in range(0, l//2):
            if news[i]!=news[l-i-1]:
                return False
        return True