class Solution:
    def floorAndCeiling(self, nums, q):
        floor = None
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] <= q:
                floor = nums[mid]
                low = mid + 1
            else:
                high = mid - 1

        ceiling = None
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] >= q:
                ceiling = nums[mid]
                high = mid - 1
            else:
                low = mid + 1

        return [floor, ceiling]
