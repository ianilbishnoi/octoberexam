class Solution:
    def mergeUnion(self, A, B):
        i = 0
        j = 0
        ans = []

        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                ans.append(A[i])
                i += 1
            elif A[i] > B[j]:
                ans.append(B[j])
                j += 1
            else:
                ans.append(A[i])
                i += 1
                j += 1

        while i < len(A):
            ans.append(A[i])
            i += 1

        while j < len(B):
            ans.append(B[j])
            j += 1

        return ans
