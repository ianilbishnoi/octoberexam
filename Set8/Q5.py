class Solution:
    def shipWithinDays(self, weights, days):
        low = 0
        high = 0

        for w in weights:
            if w > low:
                low = w

            high += w

        while low < high:
            mid = low + (high - low) // 2

            needed = 1
            load = 0

            for w in weights:
                if load + w > mid:
                    needed += 1
                    load = 0

                load += w

            if needed <= days:
                high = mid
            else:
                low = mid + 1

        return low
