#User function Template for python3

class Solution:
    
    def maxDiamonds(self, A, N, K):
        import heapq
        l = []
        heapq.heapify(l)
        for i in A:
            heapq.heappush(l,-1*i)
        ans = 0
        while(K!=0):
            x = -1*heapq.heappop(l)
            ans = ans +x
            x = x//2
            heapq.heappush(l,-1*x)
            K=K-1
        return ans
            
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        A=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.maxDiamonds(A,N,K))
# } Driver Code Ends