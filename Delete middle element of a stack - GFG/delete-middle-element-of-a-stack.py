#User function Template for python3

class Solution:
    
    #Function to delete middle element of a stack.
    def deleteMid(self, s, sizeOfStack):
        st = []
        n = sizeOfStack//2
        
        while(n):
            x = s.pop()
            st.append(x)
            n=n-1
        s.pop()
        while st:
            x=st.pop()
            s.append(x)
        return s
            
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import sys
sys.setrecursionlimit(10**8)

def main():
    t=int(input())
    while(t>0):
        sizeOfStack=int(input())
        myStack=[int(x) for x in input().strip().split()]
        ob = Solution()
        ob.deleteMid(myStack,sizeOfStack)
        while(len(myStack)>0):
            print(myStack[-1],end=" ")
            myStack.pop()
        print()
        t-=1


if __name__=="__main__":
    main()
    
    
# } Driver Code Ends