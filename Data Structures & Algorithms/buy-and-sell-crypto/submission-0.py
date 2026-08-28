class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        for i in range(len(prices)):
            bu=prices[i]
            for j in range(i + 1, len(prices)):
                se=prices[j]
                res=max(res, se-bu)
        return res        