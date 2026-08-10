class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = 1000
        profit = 0
        for price in prices:
            if price < mn:
                mn = price
            elif price - mn > profit:
                profit = price - mn

        return profit