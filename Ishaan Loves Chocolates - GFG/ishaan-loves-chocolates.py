from typing import List


class Solution:
    def chocolates(self, n : int, arr : List[int]) -> int:
        i = 0
        j = len(arr)-1
        while(i<j and i<len(arr) and j>=0):
            if arr[i]>arr[j]:
                i=i+1
            else:
                j=j-1
        return arr[i]
        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.chocolates(n, arr)
        
        print(res)
        

# } Driver Code Ends