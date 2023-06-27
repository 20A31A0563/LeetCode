#User function Template for python3

class Solution:
    def union(self, head1,head2):
        temp1 = head1
        temp2  =head2
        l1 = set()
        c1=0
        c2=0
        while(temp1!=None):
            l1.add(temp1.data)
            temp1=temp1.next 
            c1+=1
        while(temp2!=None):
            l1.add(temp2.data)
            temp2=temp2.next
            c2+=1
        l1 = list(l1)
        l1.sort()
        ans = None
        if(c1>c2):
            prev= head1
            ans = head1
            alt = head2
        else:
            prev=head2
            ans = head2
            alt  = head1
        
        for i in l1[0:len(l1)-1]:
            
            prev.data = i 
            if prev.next==None:
                prev.next = alt
            prev = prev.next
        
        prev.data = l1[-1]
        prev.next=None
        return ans
        




#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def insert(self,data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    for _ in range(int(input())):
        
        n1 = int(input())
        arr1 = [int(x) for x in input().split()]
        ll1 = linkedList()
        for i in arr1:
            ll1.insert(i)
        
        n2 = int(input())
        arr2 = [int(x) for x in input().split()]
        ll2 = linkedList()
        for i in arr2:
            ll2.insert(i)
        
        ob = Solution()
        printList(ob.union(ll1.head,ll2.head))
        print()

# } Driver Code Ends