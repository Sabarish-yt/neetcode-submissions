class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0

        for cha in t:
            if i<len(s) and s[i]==cha:
                i+=1
        return i==len(s)        