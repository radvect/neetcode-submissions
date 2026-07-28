class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 1000
        prof = 0

        for i in prices:
            min_price = min(min_price, i)
            prof = max(prof, i - min_price)
        return prof