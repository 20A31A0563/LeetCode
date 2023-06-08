#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
from typing import List


class Solution:
    def kthPermutation(self, n : int, k : int) -> str:
        fact =1
        nums = []
        for i in range(1,n):
            fact = fact*i
            nums.append(i)
        nums.append(n)
        k=k-1
        ans =""
        while(True):
            ans = ans+str(nums[k//fact])
            nums.remove(nums[k//fact])
            if(len(nums)==0):
                break
            k = k%fact
            fact = fact//len(nums)
        return ans
            
        


#{ 
 # Driver Code Starts.
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N, K = map(int, input().split())
        
        obj = Solution()
        res = obj.kthPermutation(N, K)
        
        print(res)
        

# } Driver Code Ends