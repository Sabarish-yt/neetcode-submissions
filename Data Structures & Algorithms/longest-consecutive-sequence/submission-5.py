class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st=set(nums)
        lo=0
        for n in nums:
            if (n-1) not in st:
                le=0
                while (n+le) in st:
                    le+=1
                lo=max(le,lo)
        return lo            