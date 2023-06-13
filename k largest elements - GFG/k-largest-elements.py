#User function Template for python3
class Solution:
    

	def kLargest(self,arr, n, k):
	    import heapq
	    l = []
	    heapq.heapify(l)
	    for i in arr:
	        heapq.heappush(l,-1*i)
	    ans= [ ]
	    while(k!=0):
	        x = heapq.heappop(l)
	        ans.append(-1*x)
	        k=k-1
	    return ans
	        
	    
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.kLargest(arr, n, k)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends