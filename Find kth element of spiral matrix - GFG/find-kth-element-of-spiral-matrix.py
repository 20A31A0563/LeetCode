#User function Template for python3

class Solution:
    def findK(self, a, n, m, k):
        # Write Your Code here
        x=1
        for i in range((n//2)+1):
            for j in range(i,m-i):
                if x==k:
                    return a[i][j]
                x=x+1 
            for j in range(i+1,n-i):
                if x==k:
                    return a[j][m-i-1]
                x=x+1 
            for j in range(m-i-2,i-1,-1):
                if x==k:
                    return a[n-i-1][j]
                x=x+1 
            for j in range(n-i-2,i,-1):
                if x==k:
                    return a[j][i]
                x=x+1
                
            
            


#{ 
 # Driver Code Starts

#Initial Template for Python 3

for _ in range(int(input())):
    n, m, k = map(int,input().split())
    a = [
            list(map(int,input().split()))
            for _ in range(n)
        ]
    
    ob = Solution()
    print(ob.findK(a,n,m,k))
    
# } Driver Code Ends