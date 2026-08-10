class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = [c.lower() for c in s if c.isalnum()]
        n = len(x) // 2
        return "".join(x[:n]) == "".join(x[len(x)-n:][::-1])