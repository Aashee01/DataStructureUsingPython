
#concept of deletion of singly linked list by value


# singlyLinkedList concept of insertion in betwwen the node (InsertAfterNode)


class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList():
    def __init__(self):
        self.head=None
    def print_list(self):
        curr_node=self.head
        while curr_node != None:
            print(curr_node.data)
            curr_node=curr_node.next

    def append(self,data):
        new_node=Node(data)
        #check whether linkedlist is empty or not
        if self.head is None:
            self.head=new_node
            return
        last_node=self.head
        while last_node.next !=None:
            last_node=last_node.next
        last_node.next=new_node
    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def insert_after_node(self,prev_node,data):
        if not prev_node:
            print("Previous node does not exists")
            return
        new_node=Node(data)
        new_node.next= prev_node.next
        prev_node.next=new_node

    def delete_node(self,key):
        # case 1: node to be deleted is head node
        curr_node=self.head
        if curr_node and curr_node.data == key:
            self.head=curr_node.next
            curr_node=None
            return
        # case 2: node to be deleted is not head
        prev=None
        while curr_node and curr_node.data!=key:
            prev=curr_node
            curr_node=curr_node.next
        if curr_node is None:
            return
        prev.next=curr_node.next
        curr_node=None
    def delete_node_at_pos(self,pos):
        curr_node=self.head
        if pos==0:
            self.head=curr_node.next
            curr_node=None
        prev=None
        count=0
        while curr_node and count!=pos:
            prev=curr_node
            curr_node=curr_node.next
            count+=1
        if curr_node is None:
            return
        prev.next=curr_node.next
        curr_node=None
llist=LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
#llist.prepend("E")
#llist.insert_after_node(llist.head.next,"D")
llist.delete_node("B") # delete by value
llist.delete_node_at_pos(0)
llist.print_list()