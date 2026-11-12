class Solution:
    def maxProfit(self, prices):
        lowest = prices[0]
        best = 0

        for i in range(1, len(prices)):
            if prices[i] - lowest > best:
                best = prices[i] - lowest

            if prices[i] < lowest:
                lowest = prices[i]

        return best
