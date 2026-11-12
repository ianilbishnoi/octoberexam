class Solution:
    def twoSumSorted(self, prices, target):
        left = 0
        right = len(prices) - 1

        while left < right:
            total = prices[left] + prices[right]

            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left += 1
            else:
                right -= 1

        return []
