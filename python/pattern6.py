class Solution:
    def printTriangle(self, N):
        for i in range(0,N):
            for j in range(1,N-i+1):
                print(j,end=" ")
            print()    
        # Code here

