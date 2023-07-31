#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        from collections import deque
        q = deque([])
        vis = [-1]*V
        l =[]
        #print(adj)
        q.append(0)
        while q:
                 x = q.popleft()
                 l.append(x)
                 vis[x]=1
                 for i in adj[x]:
                      if vis[i]==-1:
                          vis[i]=1
                          q.append(i)
        return l
            


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends