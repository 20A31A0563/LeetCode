#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        def rec(ind,w):
            if ind>=n:
                return 0
            if w > W:
                return 0
            if (ind,w) in dp:
                return dp[(ind,w)]
            x = 0
            if w+wt[ind]<=W:
                x = val[ind]+rec(ind+1,w+wt[ind])
            y = rec(ind+1,w)
            dp[(ind,w)] = max(x,y)
            return max(x,y)
        dp = dict()
        return rec(0,0)
            
                
                
            
       

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends