# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):
        self.data=data
        self.next=None
class LinkedList: 
  
    def __init__(self): 
        self.head=None
  
    def push(self, new_data):
        nnode=Node(new_data)
        nnode.next=self.head
        self.head=nnode
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self):
        sptr=self.head
        fptr=self.head
        if self.head is not None:
            while fptr is not None and fptr.next is not None:
                sptr=sptr.next
                fptr=fptr.next.next
            print(sptr.data)
# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
