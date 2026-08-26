class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars=""
        for c in s:
            if c.isalnum():
                chars+=c.lower()
        return chars==chars[::-1]    