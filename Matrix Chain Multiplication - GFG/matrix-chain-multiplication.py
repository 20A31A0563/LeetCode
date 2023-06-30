#User function Template for python3

class Solution:
    def matrixMultiplication(self, N, arr):
        def rec(i,j):
            if i==j:
                return 0 
            if (i,j) in d:
                return d[(i,j)]
            ans = float("inf")
            for k in range(i,j):
                steps = arr[i-1]*arr[k]*arr[j]+rec(i,k)+rec(k+1,j)
                if steps<ans:
                    ans=steps
            d[(i,j)] = ans
                
            return ans
        d = dict()
        return rec(1,N-1)
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.matrixMultiplication(N, arr))
# } Driver Code Ends