#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        zero = 0
        two = len(arr)-1
        i=0
        while(i<=two):
            if arr[i] == 0:
                arr[zero],arr[i] = arr[i],arr[zero]
                zero += 1
                i=i+1
            elif arr[i]==2:
                arr[two],arr[i] = arr[i],arr[two]
                two -= 1
            else:
                i=i+1
        return arr
                
       

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends