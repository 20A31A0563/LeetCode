#User function Template for python3


class Solution:
    def nextHappy (self, N):
        def ishappy(n):
            if n==1:
               return True
            if n<=9 and n not in vis:
                vis[n] =1
                return ishappy(n*n)
            if n<=9 and n  in vis:
                return False
            so = 0
            s = str(n)
            for i in s:
                so += (int(i)*int(i))
            return ishappy(so)
            
            
        for i in range(N+1,100000):
            vis  ={}
            if ishappy(i):
               
               return i
        return 100003


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())

        ob = Solution()
        print(ob.nextHappy(N))
# } Driver Code Ends