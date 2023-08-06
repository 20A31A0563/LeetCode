#User function Template for python3

class Solution:
    def permutation(self,s):
        def rec(prev,s1):
            if len(prev) == len(s):
                res.append(s1)
            for i in range(len(s)):
                if i not in prev:
                    prev.append(i)
                    rec(prev,s1+s[i])
                    prev.pop()
        res=[]
        rec([],"")
        res.sort()
        return res
    
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T=int(input())
    while(T>0):
        s=input()
        ob=Solution()
        ans=ob.permutation(s)
        for i in ans:
            print(i,end=" ")
        print()
        
        T-=1
# } Driver Code Ends