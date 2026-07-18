class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        buy = 0
        profit = 0
        for r in range(1, len(prices)):
            if prices[r] <= prices[l]:
                buy = prices[r]
                l = r
            else:
                profit = max(profit, prices[r]-prices[l])
        
        return profit