class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        if self.head is None:
            print("empty linked list")
        else:
            temp = self.head
            while (temp):
                print(temp.val, end='==>')
                temp = temp.next

    def push(self, data):
         new_node = Node(data)

         # 2. Make next of new Node as head
         new_node.next = self.head

         # 3. Move the head to point to new Node
         self.head = new_node

    def swap(self, x, y):
        if x == y:
            return

        prevx = None
        curx = self.head
        while curx and curx.val != x:
            prevx = curx
            curx = curx.next

        prevy = None
        cury = self.head
        while cury and cury.val != y:
            prevy = cury
            cury = cury.next

        if curx is None or cury is None:
            return

        if prevx is not None:
            prevx.next = cury
        else:
            self.head = cury

        if prevy is not None:
            prevy.next = curx
        else:
            self.head = curx



        temp = curx.next
        curx.next = cury.next
        cury.next = temp








# revrsing the linked list
    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev


# middle of the linked list

    def middle_node(self):
        if self.head is not None:
            fast = slow = self.head
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
            return slow.val
        else:
            print("empty linked list")
            return

    def delete_list(self):
        self.head = None

    # deleting middle node
    def del_middle(self):
        # base condition
        if self.head is None or self.head.next is None:
            return

        # actual
        fast = slow = self.head
        prev = None   # to keep track for the prev node
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        prev.next = slow.next


     # append to the linked list
    def append(self,data):
        New_Node = Node(data)
        if self.head is None:
             self.head = New_Node
             return
        last = self.head
        while last.next:
            last = last.next
        last.next = New_Node




    def deleteMid(self):

        # Base cases
        if (self.head is None or
                self.head.next is None):
            return

        # Initialize slow and fast pointers
        # to reach middle of linked list
        slow_Ptr = self.head
        fast_Ptr = self.head

        # Find the middle and previous of middle
        prev = None

        # To store previous of slow pointer
        while (fast_Ptr is not None and
               fast_Ptr.next is not None):
            fast_Ptr = fast_Ptr.next.next
            prev = slow_Ptr
            slow_Ptr = slow_Ptr.next

        # Delete the middle node
        prev.next = slow_Ptr.next







if __name__ == '__main__':
     obj = LinkedList()
     obj.append(1)
     obj.append(2)
     obj.append(3)
     obj.append(4)
     obj.printList()
     print()
     # obj.del_middle()
     # obj.printList()
     # obj.reverse()
     # print()
     # obj.printList()
     # obj.swap(2,3)
     # print()
     # obj.printList()
     # print(obj.middle_node())
     # obj.delete_list()
     # obj.printList()
