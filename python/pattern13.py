class Solution:
    def printTriangle(self, N):
        value = 1
        for i in range(1, N + 1):
            for j in range(i):
                print(value, end = ' ')
                value += 1
            print()
