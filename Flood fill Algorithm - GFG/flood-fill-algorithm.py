class Solution:
	def floodFill(self, image, sr, sc, newColor):
		#Code here
		from collections import deque
		q = deque([])
		q.append([sr,sc])
		color = image[sr][sc]
		while q:
		    r,c = q.popleft()
		    if image[r][c] == color:
		        image[r][c] = -1
		        if r-1>=0 and image[r-1][c]==color:
		            q.append([r-1,c])
		        if r+1<len(image) and image[r+1][c]==color:
		            q.append([r+1,c])
		        if c-1>=0 and image[r][c-1]==color:
		            q.append([r,c-1])
		        if c+1<len(image[0]) and image[r][c+1]==color:
		            q.append([r,c+1])
		for i in range(len(image)):
		    for j in range(len(image[0])):
		        if image[i][j]==-1:
		            image[i][j] = newColor
	    return image
		        
		    



#{ 
 # Driver Code Starts
import sys
sys.setrecursionlimit(10**7)


T=int(input())
for i in range(T):
	n, m = input().split()
	n = int(n)
	m = int(m)
	image = []
	for _ in range(n):
		image.append(list(map(int, input().split())))
	sr, sc, newColor = input().split()
	sr = int(sr); sc = int(sc); newColor = int(newColor);
	obj = Solution()
	ans = obj.floodFill(image, sr, sc, newColor)
	for _ in ans:
		for __ in _:
			print(__, end = " ")
		print()
# } Driver Code Ends