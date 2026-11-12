class Solution:
    def splitArray(self, pages, m):
        n = len(pages)

        if m > n:
            return -1

        low = 0
        high = 0

        for p in pages:
            if p > low:
                low = p

            high += p

        while low < high:
            mid = low + (high - low) // 2

            groups = 1
            load = 0

            for p in pages:
                if load + p > mid:
                    groups += 1
                    load = 0

                load += p

            if groups <= m:
                high = mid
            else:
                low = mid + 1

        return low
