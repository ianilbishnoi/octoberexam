class Solution:
    def findAnagrams(self, s, p):
        n = len(s)
        m = len(p)
        ans = []

        if m > n:
            return ans

        need = [0] * 26
        window = [0] * 26

        for ch in p:
            need[ord(ch) - 97] += 1

        diff = 0

        for i in range(26):
            if need[i] != 0:
                diff += 1

        for i in range(n):
            c = ord(s[i]) - 97
            before = window[c] == need[c]
            window[c] += 1
            after = window[c] == need[c]

            if before and not after:
                diff += 1
            elif not before and after:
                diff -= 1

            if i >= m:
                c = ord(s[i - m]) - 97
                before = window[c] == need[c]
                window[c] -= 1
                after = window[c] == need[c]

                if before and not after:
                    diff += 1
                elif not before and after:
                    diff -= 1

            if i >= m - 1 and diff == 0:
                ans.append(i - m + 1)

        return ans
