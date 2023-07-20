from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		def dfs(node,par):
		    vis[node] = 1
		    x = False
		    for i in adj[node]:
		        if vis[i]==-1:
		            if dfs(i,node)==True:
		                return True
		        elif i!=par:
		            return True
		    
		    return False
	    vis= [-1]*V
	    #rec = [0]*V
	    ans = False
	    for i in range(V):
	       if vis[i]==-1:
	           ans = ans | dfs(i,None)
	    return ans
	 
	   


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
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends