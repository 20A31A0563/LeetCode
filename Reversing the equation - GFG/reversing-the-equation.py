#User function Template for python3

class Solution:
    def reverseEqn(self, s):
        l=""
        sub=""
        for i in s:
            if i =='+' or i=='-' or i=='*' or i=='/':
                l = sub+l
                l = i+l
                sub=""
            else:
                sub += i
        l = sub+l
        return l
       
                
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseEqn(s)
        print(ans)
# } Driver Code Ends