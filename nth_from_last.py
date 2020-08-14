
# nth to last node

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

    def swap_nodes(self, key_1, key_2):

        if key_1 == key_2:
            return

        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next
    def reverse_recursive(self):
        # base case
        def recursive_reverse(curr,prev):
            if not curr:
                return prev

            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
            return recursive_reverse(curr,prev) # recursive call
        self.head=recursive_reverse(curr=self.head,prev=None) #update the head pointer
    def merge_sorted(self,llist):
        p=self.head
        q=llist.head
        s=None

        #check whether any of thrm is null

        if not p:
            return q
        if not q:
            return p
        if p and q:
            if p.data<=q.data:
                s=p
                p=s.next
            else:
                s=q
                q=s.next
            new_head=s
        while p and q:
            if p.data<=q.data:
                s.next=p
                s=p
                p=s.next
            else:
                s.next=q
                s=q
                q=s.next
        if not p:
            s.next=q
        if not q:
            s.next=p
        return  new_head
    def len_iterative(self):
        count=0
        curr_node=self.head
        while curr_node:
            count+=1
            curr_node=curr_node.next
        return count
    def print_nth_from_last(self,n):
        total_len=self.len_iterative()
        curr=self.head
        while curr:
            if total_len==n:
                print(curr.data)
                return curr.data
            total_len-=1
            curr=curr.next
        if curr is None:
            return
    def print_nth_from(self,n):
        p=self.head
        q=self.head
        count=0
        while q:
            count+=1
            if count>=n:
                break
            q=q.next
        if not q:
            print(str(n)+" is greater than the number of nodes ")
            return
        while p and q.next:
            p= p.next
            q=q.next
        return p.data

llist_1=LinkedList()
llist_1.append(1)
llist_1.append(4)
llist_1.append(7)
llist_1.append(6)
llist_1.append(5)
print(llist_1.print_nth_from(2))
