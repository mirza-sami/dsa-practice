class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minPrice = float('inf')
        maxNumber = 0

        for price in prices:

            if price < minPrice:
                minPrice = price
            elif price - minPrice > maxNumber:
                maxNumber = price - minPrice
            
        return maxNumber
        
