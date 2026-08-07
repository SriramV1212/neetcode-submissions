class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy_idx = 0
        sell_idx = 1
        profit = 0

        while sell_idx < len(prices):
            if prices[buy_idx] < prices[sell_idx]:
                sale = prices[sell_idx] - prices[buy_idx]
                profit = max(sale,profit)
            else:
                buy_idx = sell_idx
            sell_idx+=1
        
        return(profit)





        



