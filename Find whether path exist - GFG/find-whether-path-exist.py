
class Solution:
    
    #Function to find whether a path exists from the source to destination.
	def is_Possible(self, grid):
	    from collections import deque
	    q = deque([])
	    for i in range(len(grid)):
	        for j in range(len(grid)):
	            if grid[i][j]==1:
	                grid[i][j] =0
	                q.append([i,j])
	            if grid[i][j]==2:
	                de = [i,j]
	    while q:
	        r,c = q.popleft()
	        if r==de[0] and c==de[1]:
	            return 1
	        if r+1< len(grid) and grid[r+1][c]!=0:
	            grid[r+1][c] = 0
	            q.append([r+1,c])
	        if r-1>=0 and grid[r-1][c]!=0:
	            grid[r-1][c] = 0
	            q.append([r-1,c])
	        if c-1>=0 and grid[r][c-1]!=0:
	            grid[r][c-1] = 0
	            q.append([r,c-1])
	        if c+1<len(grid) and grid[r][c+1]!=0:
	            grid[r][c+1] = 0
	            q.append([r,c+1])
	    return 0
	        
	       
	    
	    
	                
	                
	            
		


#{ 
 # Driver Code Starts

T=int(input())
for i in range(T):
	n = int(input())
	grid = []
	for _ in range(n):
		a = list(map(int, input().split()))
		grid.append(a)
	obj = Solution()
	ans = obj.is_Possible(grid)
	if(ans):
		print("1")
	else:
		print("0")

# } Driver Code Ends