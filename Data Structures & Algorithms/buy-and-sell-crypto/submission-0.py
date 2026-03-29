class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left, right = 0, 1 # left is buy, right is sell
        max_profit = 0
        
        while right < len(prices):
            # Is this transaction profitable?
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                # We found a lower buy price, move left pointer
                left = right
            
            # Always move right pointer forward to check future days
            right += 1
            
        return max_profit