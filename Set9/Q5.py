class Solution:
    def insertInterval(self, intervals, newInterval):
        ans = []
        i = 0
        n = len(intervals)
        start = newInterval[0]
        end = newInterval[1]

        while i < n and intervals[i][1] < start:
            ans.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= end:
            if intervals[i][0] < start:
                start = intervals[i][0]

            if intervals[i][1] > end:
                end = intervals[i][1]

            i += 1

        ans.append([start, end])

        while i < n:
            ans.append(intervals[i])
            i += 1

        return ans
