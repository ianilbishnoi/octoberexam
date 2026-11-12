class Solution:
    def secondHighest(self, nums):
        first = None
        second = None

        for num in nums:
            if first is None or num > first:
                if num != first:
                    second = first
                    first = num
            elif num != first and (second is None or num > second):
                second = num

        return second
