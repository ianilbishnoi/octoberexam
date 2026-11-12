class Solution:
    def before(self, a, b):
        if a[0] != b[0]:
            return a[0] < b[0]

        return a[1] > b[1]

    def mergeSort(self, items):
        if len(items) <= 1:
            return items

        mid = len(items) // 2
        left = self.mergeSort(items[:mid])
        right = self.mergeSort(items[mid:])

        merged = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if self.before(right[j], left[i]):
                merged.append(right[j])
                j += 1
            else:
                merged.append(left[i])
                i += 1

        while i < len(left):
            merged.append(left[i])
            i += 1

        while j < len(right):
            merged.append(right[j])
            j += 1

        return merged

    def sortByRarity(self, nums):
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        items = []

        for num in freq:
            items.append((freq[num], num))

        items = self.mergeSort(items)

        ans = []

        for count, num in items:
            for _ in range(count):
                ans.append(num)

        return ans
