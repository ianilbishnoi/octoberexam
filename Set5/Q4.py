class Solution:
    def countInversions(self, nums):
        n = len(nums)
        temp = [0] * n
        count = 0
        width = 1

        while width < n:
            left = 0

            while left < n:
                mid = left + width
                right = left + 2 * width

                if mid > n:
                    mid = n

                if right > n:
                    right = n

                i = left
                j = mid
                k = left

                while i < mid and j < right:
                    if nums[i] <= nums[j]:
                        temp[k] = nums[i]
                        i += 1
                    else:
                        temp[k] = nums[j]
                        j += 1
                        count += mid - i

                    k += 1

                while i < mid:
                    temp[k] = nums[i]
                    i += 1
                    k += 1

                while j < right:
                    temp[k] = nums[j]
                    j += 1
                    k += 1

                for t in range(left, right):
                    nums[t] = temp[t]

                left += 2 * width

            width *= 2

        return count
