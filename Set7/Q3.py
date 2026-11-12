class Solution:
    def firstFailingBuild(self, builds):
        low = 0
        high = len(builds) - 1
        ans = -1

        while low <= high:
            mid = low + (high - low) // 2

            if builds[mid] == 1:
                ans = mid + 1
                high = mid - 1
            else:
                low = mid + 1

        return ans
