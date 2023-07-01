#User function Template for python3

class Solution:  
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        def rec(ind):
            if ind>=n:
                return 0
            if ind in d:
                return d[ind]
            x = a[ind]+rec(ind+2)
            y = rec(ind+1)
            d[ind] = max(x,y)
            return max(x,y)
        dp = [0]*(n+2)
        for i in range(n-1,-1,-1):
            dp[i] = max(dp[i+1],a[i]+dp[i+2])
        return dp[0]
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.FindMaxSum(a,n))
# } Driver Code Ends