class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)

        for i in range(n):
            index = nums[i]
            if index < 0:
                index = -index

            index -= 1

            if nums[index] > 0:
                nums[index] = -nums[index]

        ans = []

        for i in range(n):
            if nums[i] > 0:
                ans.append(i + 1)

        return ans
