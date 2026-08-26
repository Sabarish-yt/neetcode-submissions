from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1] * n

        pre=1
        for i in range(n):
            res[i]=pre
            pre*=nums[i]

        po=1
        for i in range(n-1,-1,-1):
            res[i]*=po
            po*=nums[i]
        return res        
