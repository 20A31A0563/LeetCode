#User function Template for python3

class Solution:

    def nCr(self, n, r):
        if n<r:
            return 0
        f =1 
        r1 = 1
        r2=1
        for i in range(1,n+1):
            f = f*i 
            if(i==r):
                r1 = f 
            if(i==(n-r)):
                r2 = f
        return (f//(r1*r2))%(10**9+7)
                
        
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nCr(n, r))
# } Driver Code Ends