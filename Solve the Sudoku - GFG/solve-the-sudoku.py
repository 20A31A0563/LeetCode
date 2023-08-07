#User function Template for python3

class Solution:
    
    #Function to find a solved Sudoku. 
    
    def SolveSudoku(self,grid):
        def valid(grid,r,c,k):
         for i in range(9):
            if grid[i][c] == k:
                return False
            if grid[r][i] ==k:
                return False
            if grid[3*(r//3)+(i//3)][3*(c//3)+(i%3)]==k:
                return False
         return True
        for i in range(len(grid)):
            for j in range(len(grid)):
              if grid[i][j]==0:
                for k in range(1,10):
                    if valid(grid,i,j,k):
                        grid[i][j] = k 
                        if self.SolveSudoku(list(grid)):
                            return True
                        grid[i][j] = 0
                return False
        return True
    
                
                                    
    #Function to print grids of the Sudoku.    
    def printGrid(self,arr):
        for i in range(9):
            for j in range(9):
                print(arr[i][j],end=" ")
        # Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t = int(input())
    while(t>0):
        grid = [[0 for i in range(9)] for j in range(9)]
        row = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(9):
            for j in range(9):
                grid[i][j] = row[k]
                k+=1
                
        ob = Solution()
            
        if(ob.SolveSudoku(grid)==True):
            ob.printGrid(grid)
            print()
        else:
            print("No solution exists")
        t = t-1
# } Driver Code Ends