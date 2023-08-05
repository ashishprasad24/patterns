class Solution:
    def printTriangle(self, N):
        for i in range(1, 1 + N):
            for j in range(1, i + 1):
                print(j, end = ' ')
            print()

