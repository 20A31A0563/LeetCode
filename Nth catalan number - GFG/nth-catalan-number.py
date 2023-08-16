
class Solution:
    def findCatalan(self, n : int) -> int:
        # code here
        dp = [0]*(n+1)
        dp[0] =1
        dp[1] =1
        for i in range(2,n+1):
            for j in range(i):
                dp[i] += (dp[j] * dp[i-j-1])%((10**9+7))
        return dp[n]%(10**9+7)
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.findCatalan(n)
        
        print(res)
        

# } Driver Code Ends