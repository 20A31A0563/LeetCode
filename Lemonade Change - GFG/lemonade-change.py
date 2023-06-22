#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def lemonadeChange(self, N, bills):
        c5 = 0
        c10 = 0
        c20 = 0
        for i in range(N):
            if bills[i] == 10:
                if c5>=1:
                    c5 = c5-1 
                    c10 += 1
                else:
                    return False
            if bills[i] == 20:
                if c10>=1 and c5>= 1:
                    c5 = c5-1 
                    c10 -= 1
                    c20 += 1
                elif c5>=3:
                    c5 -= 3
                    c20 += 1
                else:
                    return False
            if bills[i]==5:
                c5 += 1
        return True
            
            
            
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        bills = list(map(int, input().split()))
        ob = Solution()
        res = ob.lemonadeChange(N, bills)
        print(res)
# } Driver Code Ends