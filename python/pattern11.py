class Solution:
    def printTriangle(self, N):
        for i in range(1, N + 1):
            value = i % 2
            for j in range(1, i + 1):
                print(value, end = ' ')
                value ^= 1
            print()
