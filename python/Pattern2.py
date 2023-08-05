class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(N):
            for j in range(i+1):
                print("*",end=" ")
            print()    

