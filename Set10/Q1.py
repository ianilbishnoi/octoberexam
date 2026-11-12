class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        ans = [0] * n

        left = 0
        right = n - 1

        for pos in range(n - 1, -1, -1):
            if nums[left] * nums[left] > nums[right] * nums[right]:
                ans[pos] = nums[left] * nums[left]
                left += 1
            else:
                ans[pos] = nums[right] * nums[right]
                right -= 1

        return ans
