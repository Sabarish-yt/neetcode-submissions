from collections import defaultdict
from typing import List 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)

        for s in strs:
            sot="".join(sorted(s))
            res[sot].append(s)

        return list(res.values())    