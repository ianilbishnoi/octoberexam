class Solution:
    def bubbleSort(self, nums):
        n = len(nums)
        passes = 0

        for i in range(n - 1):
            swapped = False

            for j in range(n - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True

            if not swapped:
                break

            passes += 1

        return nums, passes
