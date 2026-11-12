class Solution:
    def firstDuplicate(self, nums):
        seen = {}

        for num in nums:
            if num in seen:
                return num

            seen[num] = 1

        return -1
