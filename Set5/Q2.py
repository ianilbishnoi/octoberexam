class Solution:
    def kSmallest(self, nums, k):
        n = len(nums)

        for i in range(k):
            smallest = i

            for j in range(i + 1, n):
                if nums[j] < nums[smallest]:
                    smallest = j

            nums[i], nums[smallest] = nums[smallest], nums[i]

        ans = []

        for i in range(k):
            ans.append(nums[i])

        return ans
