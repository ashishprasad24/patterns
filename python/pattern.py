class Solution:
    def printTriangle(self, N):
        for row in range(N, 0, -1):
            for space in range(N - row):
                print(' ', end = '')
            for asterisk in range(1, 2 * row):
                print('*', end = '')
            print()

