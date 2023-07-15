1#User function Template for python3

class Solution:
    def shortestDistance(self,N,M,A,X,Y):
        from collections import deque
        q = deque([])
        grid = A
        q.append([0,0,0])
        grid[0][0] = 0 
        while q:
	        r,c,s= q.popleft()
	        if r==X and c==Y:
	            return s
	        if r+1< len(grid) and grid[r+1][c]!=0:
	            grid[r+1][c] = 0
	            q.append([r+1,c,s+1])
	        if r-1>=0 and grid[r-1][c]!=0:
	            grid[r-1][c] = 0
	            q.append([r-1,c,s+1])
	        if c-1>=0 and grid[r][c-1]!=0:
	            grid[r][c-1] = 0
	            q.append([r,c-1,s+1])
	        if c+1<len(grid[0]) and grid[r][c+1]!=0:
	            grid[r][c+1] = 0
	            q.append([r,c+1,s+1])
	    return -1
        #code here


#{ 
 # Driver Code Starts

#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split())
        a=[]
        for i in range(N):
            s=list(map(int,input().strip().split()))
            a.append(s)
        x,y=map(int,input().strip().split())    
        ob=Solution()
        print(ob.shortestDistance(N,M,a,x,y))
        
# } Driver Code Ends