class Solution:
    def countStrongWindows(self, nums, k, threshold):
        need = k * threshold
        window = 0

        for i in range(k):
            window += nums[i]

        count = 0

        if window >= need:
            count += 1

        for i in range(k, len(nums)):
            window += nums[i] - nums[i - k]

            if window >= need:
                count += 1

        return count
