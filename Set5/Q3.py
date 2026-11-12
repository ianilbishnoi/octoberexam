class Solution:
    def insertionSort(self, nums):
        shifts = 0

        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1

            while j >= 0 and nums[j] > key:
                nums[j + 1] = nums[j]
                shifts += 1
                j -= 1

            nums[j + 1] = key

        return nums, shifts
