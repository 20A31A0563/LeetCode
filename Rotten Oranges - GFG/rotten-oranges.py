class Solution:

    #Function to find minimum time required to rot all oranges. 
	def orangesRotting(self, grid):
		from collections import deque
		q = deque([])
		for i in range(len(grid)):
		    for j in range(len(grid[0])):
		        if grid[i][j] == 2:
		            q.append([i,j,0])
		            grid[i][j] =-1
		ans = -1
		while q:
		    l = len(q)
		    for i in range(l):
		        x = q.popleft()
		        r ,c = x[0],x[1]
		        ans = max(ans,x[2])
		        if(r-1>=0 and grid[r-1][c]!=0 and grid[r-1][c]!=-1):
		            q.append([r-1,c,x[2]+1])
		            grid[r-1][c] =-1
		        if(r+1<len(grid) and grid[r+1][c]!=0 and grid[r+1][c]!=-1):
		            q.append([r+1,c,x[2]+1])
		            grid[r+1][c] =-1
		        if(c+1<len(grid[0]) and grid[r][c+1]!=0 and grid[r][c+1]!=-1):
		            q.append([r,c+1,x[2]+1])
		            grid[r][c+1] =-1
		        if(c-1>=0 and grid[r][c-1]!=0 and grid[r][c-1]!=-1):
		            q.append([r,c-1,x[2]+1])
		            grid[r][c-1] =-1
		for i in range(len(grid)):
		    for j in range(len(grid[0])):
		        if grid[i][j]==1:
		            return -1
		   
		return ans
		        
		


#{ 
 # Driver Code Starts
from queue import Queue


T=int(input())
for i in range(T):
	n, m = map(int, input().split())
	grid = []
	for _ in range(n):
		a = list(map(int, input().split()))
		grid.append(a)
	obj = Solution()
	ans = obj.orangesRotting(grid)
	print(ans)

# } Driver Code Ends