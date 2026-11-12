class Solution:
    def longestUniqueRun(self, nums):
        last = {}
        start = 0
        longest = 0

        for i in range(len(nums)):
            if nums[i] in last and last[nums[i]] >= start:
                start = last[nums[i]] + 1

            last[nums[i]] = i

            if i - start + 1 > longest:
                longest = i - start + 1

        return longest
