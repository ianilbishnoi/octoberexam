class Solution:
    def longestStreak(self, attendance, threshold):
        current = 0
        longest = 0

        for num in attendance:
            if num >= threshold:
                current += 1

                if current > longest:
                    longest = current
            else:
                current = 0

        return longest
