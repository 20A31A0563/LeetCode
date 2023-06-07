#User function Template for python3
class Solution:
    def leastPrimeFactor (self, n):
        sieve = []
        for i in range(n+2):
            sieve.append(i)
        p=2
        while(p*p<=(n+1)):
            if sieve[p] == p:
                
                for i in range(p*p,n+2,p):
                    if sieve[i]==i:
                          sieve[i] = p 
            p=p+1
        return sieve


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.leastPrimeFactor(n)
		for i in range(1, n+1):
			print(ans[i], end = " ")
		print()

# } Driver Code Ends