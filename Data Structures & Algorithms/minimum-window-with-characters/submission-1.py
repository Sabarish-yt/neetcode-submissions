class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""
        ct,window={},{}
        for c in t:
            ct[c]=1+ct.get(c,0)

        have,need=0,len(ct)
        res,resLen=[-1,-1], float("infinity")
        l=0
        for r in range(len(s)):
            c=s[r] 
            window[c]=1+window.get(c,0)
            if c in ct and window[c]==ct[c]:
                have+=1

            while have==need:
                if(r-l+1)<resLen:
                    res=[l,r]
                    resLen=(r-l+1)
                window[s[l]]-=1
                if s[l] in ct and window[s[l]]<ct[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if resLen!=float("infinity") else ""                           