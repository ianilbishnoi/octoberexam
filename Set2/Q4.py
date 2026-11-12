class Solution:
    def rangeSumQueries(self, nums, queries):
        prefix = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]

        ans = []

        for l, r in queries:
            ans.append(prefix[r + 1] - prefix[l])

        return ans
