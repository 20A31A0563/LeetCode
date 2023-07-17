#User function Template for python3

class Solution:
	def FirstNonRepeating(self, A):
		# Code here
		from collections import OrderedDict
		ans=""
		d= OrderedDict()
		for i in A:
		    if i not in d:
		        d[i] = 1
		    else:
		        d[i]+=1
		    f = 0
		    for j in  d:
		            if d[j]==1:
		                f=1
		                ans = ans+j 
		                break
		    if f==0:
		            ans = ans+"#"
		    #print(d)
	    return ans
		                


#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		A = input()
		ob = Solution()
		ans = ob.FirstNonRepeating(A)
		print(ans)

# } Driver Code Ends