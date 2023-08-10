class Solution:
    def printTriangle(self, N):
        for i in range(1, N + 1):
            # Print left triangle
            for j in range(1, i + 1):
                print(j, end = ' ')
            
            # Print spaces in between
            for sp in range(2 * (N - i)):
                print('  ', end = '')
            
            # Print right triangle
            for j in range(i, 0, -1):
                print(j, end = ' ')
            
            print()
        
                
