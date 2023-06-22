#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        l = []
        for i in range(n):
            l.append([start[i],end[i]])
        l.sort()
        i = 0
        j=1
        c = 0
        while(j<len(l)):
            if l[j][0] > l[i][1]:
                i= j 
                j=j+1
            else:
                if l[j][1] <= l[i][1]:
                    i = j
                j=j+1 
                c=c+1
        return n-c
                
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends