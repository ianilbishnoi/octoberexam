class Solution:
    def mergeSort(self, intervals):
        if len(intervals) <= 1:
            return intervals

        mid = len(intervals) // 2
        left = self.mergeSort(intervals[:mid])
        right = self.mergeSort(intervals[mid:])

        merged = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i][0] <= right[j][0]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        while i < len(left):
            merged.append(left[i])
            i += 1

        while j < len(right):
            merged.append(right[j])
            j += 1

        return merged

    def mergeIntervals(self, intervals):
        intervals = self.mergeSort(intervals)

        ans = [[intervals[0][0], intervals[0][1]]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start <= ans[-1][1]:
                if end > ans[-1][1]:
                    ans[-1][1] = end
            else:
                ans.append([start, end])

        return ans
