#User function Template for python3

from typing import List
import heapq 
class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        adj = [[] for i in range(n)]
        for i in range(len(edges)):
            adj[edges[i][0]].append([edges[i][2],edges[i][1]])
        q = []
        heapq.heapify(q)
        dist = [float("inf")]*n
        heapq.heappush(q,0)
        dist[0] = 0
        while q:
            u = heapq.heappop(q)
            for i in adj[u]:
                node = i[1]
                if dist[node]>i[0]+dist[u]:
                    dist[node] = i[0]+dist[u]
                    heapq.heappush(q,i[1])
        for i in range(len(dist)):
            if dist[i] == float("inf"):
                dist[i] = -1
        return dist


#{ 
 # Driver Code Starts

#Initial Template for Python 3

from typing import List




class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()



class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m=map(int,input().split())
        
        
        edges=IntMatrix().Input(m, 3)
        
        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        
        IntArray().Print(res)
# } Driver Code Ends