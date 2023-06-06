#User function Template for python3

class Solution:

    def isPossible(self, S):
        d  = dict()
        for i in S:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        c = 0
        for i in d:
            if d[i]%2!=0:
                c=c+1
        return c<=1
            




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        if solObj.isPossible(S):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends