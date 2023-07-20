#User function Template for python3


class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        def dfs(node):
            vis[node] = 1
            rec[node] = 1
            x=False
            for i in adj[node]:
                if vis[i] == -1:
                    x=  x | dfs(i)
                elif vis[i]==1 and rec[i]==1:
                    return True
            rec[node] = 0 
            return x
        #print(adj)
        vis = [-1]*V
        ans = False
        for i in range(V):
            #print(vis)
            if vis[i]==-1:
                rec = [0]*V
                ans = ans | dfs(i)
                #if ans==True:
                #print(i)
        return ans
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends