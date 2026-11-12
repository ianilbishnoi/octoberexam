class Solution:
    def findKthLargest(self, nums, k):
        low = 0
        high = len(nums) - 1
        target = len(nums) - k

        while low < high:
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

            if target < lt:
                high = lt - 1
            elif target > gt:
                low = gt + 1
            else:
                return pivot

        return nums[low]
