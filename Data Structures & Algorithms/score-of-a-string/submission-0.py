class Solution:
    def scoreOfString(self, s: str) -> int:
        n=len(s)
        su=0
        for i in range(len(s) - 1):
            su+=abs(ord(s[i+1]) - ord(s[i]))
        return su        