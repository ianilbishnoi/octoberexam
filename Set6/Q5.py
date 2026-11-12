class Solution:
    def quickSort(self, nums):
        stack = [(0, len(nums) - 1)]

        while stack:
            low, high = stack.pop()

            if low >= high:
                continue

            pivot = nums[(low + high) // 2]
            lt = low
            i = low
            gt = high

            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1

            stack.append((low, lt - 1))
            stack.append((gt + 1, high))

        return nums
