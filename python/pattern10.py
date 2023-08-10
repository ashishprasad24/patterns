class Solution:
    def printTriangle(self, N):
        # Upper Triangle of (N-1) rows
        for i in range(1, N):
            for j in range(1, i + 1):
                print('* ', end = '')
            print()
        
        # Lower triangle of N rows
        for i in range(N, 0, -1):
            for j in range(1, i + 1):
                print('* ', end = '')
            print()
