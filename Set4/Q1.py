class Solution:
    def maxWindowSum(self, nums, k):
        window = 0

        for i in range(k):
            window += nums[i]

        best = window

        for i in range(k, len(nums)):
            window += nums[i] - nums[i - k]

            if window > best:
                best = window

        return best
