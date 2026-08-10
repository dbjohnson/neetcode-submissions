class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return max([
            max(prices[i + 1:]) - buy
            for i, buy in enumerate(prices[:-1])
        ] + [0])
        