class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = float('inf')
        max = 0 
        for price in prices: 
            if price < min: 
                min = price
            elif price - min > max: 
                max = price - min
        return max
