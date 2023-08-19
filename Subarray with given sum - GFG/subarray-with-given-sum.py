#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
        winsum = 0
        st = 0
        end = -1
        if s==0:
            if s in arr:
                return [arr.index(0)+1,arr.index(0)+1]
            else:
                return [-1]
            
        for j in range(len(arr)):
            i = arr[j]
            winsum += i
            if winsum==s:
                return [st+1,j+1]
            while winsum>=s:
                winsum -= arr[st]
                st = st+1
                if winsum==s:
                     return [st+1,j+1]
                
        return [-1]
        
           
           
           


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends