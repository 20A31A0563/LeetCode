#User function Template for python3

class Solution:

    def longestKSubstr(self, s, k):
        win = ''
        d = dict()
        ans = -1
        for i in range(len(s)):
            win += s[i]
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] =1 
            if len(d)>k:
                i = 0
                while(len(d)>k):
                    d[win[i]] -= 1
                    if d[win[i]] ==0 :
                        d.pop(win[i])
                    i=i+1
                win = str(win[i:])
            if len(d)==k:
                ans = max(ans,len(win))
        return ans
                    
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends