class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = float('inf')
        max_val = 0 

        for i in prices:

            if i< min_val: 
                min_val = i

            else:
                max_val = max(max_val, i - min_val)

        return max_val