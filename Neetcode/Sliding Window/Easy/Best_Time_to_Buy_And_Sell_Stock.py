# Completed: 01/13/2026

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest = 0
        min_price = prices[0]
        max_price = prices[0]

        for price in prices:
            if price < min_price:
                min_price = price
                max_price = price
            if price > max_price:
                max_price = price
            if max_price - min_price > highest:
                highest = max_price - min_price
        
        return highest