#User function Template for python3

class Solution:

    def longestPalinSubseq(self, S):
        def rec(ind1,ind2,s,t):
            if ind1<0 or ind2<0:
                return 0
            if (ind1,ind2) in dp:
                return dp[(ind1,ind2)]
            if s[ind1]==t[ind2]:
                dp[(ind1,ind2)] = 1+rec(ind1-1,ind2-1,s,t)
                return dp[(ind1,ind2)]
            dp[(ind1,ind2)] = max(rec(ind1,ind2-1,s,t),rec(ind1-1,ind2,s,t))
            return dp[(ind1,ind2)]
        dp=dict()
        return rec(len(s)-1,len(s)-1,s,s[::-1])
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        ans = ob.longestPalinSubseq(s)
        print(ans)
# } Driver Code Ends