class Node:
    def __init__(self,value):
        self.value = value
        self.next=None





class LinkedList:
    def __init__(self,value): #creates a new node , constructor
        new_node = Node(value) #creates new node called new node
        self.head=new_node #sets head to new node
        self.tail = new_node #sets tail to new node (only one node in LL)
        self.length = 1 #sets length to 1 
        #to start a linked list we would call my_linked_list = LinkedList(4)

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next


    def append(self,value): #create node,add at end
        new_Node = Node(value)
        if(self.head == None): #edge case if list is empty
            self.head = new_Node
            self.tail = new_Node
        else:
             self.tail.next =new_Node #last item points to new node
             self.tail = new_Node #tail points to new node 
        self.length +=1
        return True #we return true because later another method will require a return val T or F

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self,value):
        new_Node= Node(value)
        if(self.head == None):
            self.head = new_Node
            self.tail = new_Node
        elif(self.length == 1):
            self.head = new_Node
            self.head.next = self.tail
        else:
            temp = self.head
            self.head = new_Node
            self.head.next = temp
        self.length +=1 
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp #temp is item we removed from LL

    def get(self,index):
        if(index < 0 or index >= self.length):
            return None
        temp = self.head
        for _ in range(index): # if we are not using variable in for loop, we replace with an underscore
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index) 
        if temp is not None:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1   
        return True

    def remove_by_index(self,index):
        if(self.length == 0):
            self.head = None
            self.taile = None
            return None
        if(index == 0):
            return self.pop_first()
        if(index == self.length):
            return self.pop()
        pre = self.get(index -1)
        remove_Node = self.get(index)
        pre.next = remove_Node.next
        remove_Node.next = None
        self.length -=1
        return remove_Node

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp ## switching head and tail
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next 
            temp.next = before ##flips pointer
            before = temp 
            temp = after

    def deleteNode(self, key):
         
        # Store head node
        temp = self.head
 
        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.value == key):
                self.remove_by_index(0)
                return
 
        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while(temp is not None):
            if temp.value == key:
                break
            prev = temp
            temp = temp.next
 
        # if key was not present in linked list
        if(temp == None):
            return
 
        # Unlink the node from linked list
        prev.next = temp.next
 
        temp = None



     

        



        



    



            


 
            



  
        
        

    
    






my_LL =LinkedList(0)
my_LL.append(1)
my_LL.append(2)
my_LL.append(3)
my_LL.remove_by_value(21)

my_LL.print_list()
print("\n")
print(my_LL.length)

