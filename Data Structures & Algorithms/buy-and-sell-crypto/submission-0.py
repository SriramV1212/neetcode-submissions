class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy_idx = 0
        sell_idx = len(prices)-1
        profit = 0

        while buy_idx < sell_idx:
            sale = prices[sell_idx] - prices[buy_idx]
            if sale<profit:
                buy_idx+=1
            else:
                profit = sale
                sell_idx-=1
        
        return(profit)



