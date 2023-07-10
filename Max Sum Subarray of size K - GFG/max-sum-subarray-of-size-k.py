#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        def calculate_min_loss(N, K, costs):
                            window_sum = sum(costs[:K])
                            min_loss = window_sum
                            for i in range(K, N):
                                  window_sum += costs[i] - costs[i-K]
                                  min_loss = max(min_loss, window_sum)
                            return min_loss
        return calculate_min_loss(N,K,Arr)
        
        
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends