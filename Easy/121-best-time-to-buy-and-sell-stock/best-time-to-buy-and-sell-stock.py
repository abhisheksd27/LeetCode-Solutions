class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        l=0
        r=1
        while r<len(prices):
            if prices[r]>prices[l]:
                profit = prices[r] - prices[l]
                maxprofit = max(maxprofit,profit)
            else:
                l=r
            r+=1
        return maxprofit