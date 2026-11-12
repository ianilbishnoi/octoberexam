class Solution:
    def countingSort(self, marks):
        count = [0] * 101

        for mark in marks:
            count[mark] += 1

        ans = []

        for value in range(101):
            for _ in range(count[value]):
                ans.append(value)

        return ans
