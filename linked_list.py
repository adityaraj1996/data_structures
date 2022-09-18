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

    def beginInsert(self, newval):
        # creating the Node
        first = Node(newval)
        if self.head is None:
            print("empty linked list..adding the node as the first Node")
            self.head = first
        else:
            # updating the head pointer
            first.next = self.head
            self.head = first

    def endInsert(self, newval):
        # creation of new node
        last = Node(newval)
        # for empty list
        if self.head is None:
            self.head = last
        else:
            n = self.head
            # reaching the last node
            while (n.next):
                n = n.next
            n.next = last  # updating the pointer

    def afternode(self, value, x):
        #find the node
        n = self.head
        while n is not None:
            if n.val == x:
                break
            n = n.next
        if n is None:
            print("x not present...!!!")
        else:
            new_node = Node(value)# creating the new node
            new_node.next = n.next # adjusting the pointers
            n.next = new_node

    def beforenode(self,value,x):
        # check if the list is empty
        if self.head is None:
            print("the link list is empty")
            return

        # first check if x is the first node
        if self.head.val == x:    # copying add_begin code
            first = Node(value)  # create the node
            first.next = self.head
            self.head = first
            return
        # we will find the previous node of x and then apply addafter method to that previous code
        n = self.head
        while n is not None:
            if n.next.val == x:
                break
            n = n.next
        if n is None:
            print("x not present...!!!")
        else:
            new_node = Node(value)# creating the new node
            new_node.next = n.next # adjusting the pointers
            n.next = new_node




    def del_begin(self):
        if self.head is None:  # checking if the LL is empty
            print("the LL is empty , can't delete the nodes...!!!")
            return
        self.head = self.head.next  # pointing the header to the second node

    def del_end(self):
        if self.head is None:  # checking if the LL is empty
            print("the LL is empty , can't delete the nodes...!!!")
            return
        # now we want to find the second last node and will update its next to NULL
        n = self.head
        while n.next.next is not None:
            n = n.next
        n.next = None

    def del_by_value(self, data):
        if self.head is None:
            print(" the LL is empty")
            return
        # now we want to see if the given node is the first node , in that case we will apply del_begin method
        if self.head.val == data:
            self.head = self.head.next  # pointing the header to the second node
            return

        # now if not the first node , we will find the previous node and change its next to data.next
        n = self.head
        while n.next is not None:
            if n.next.val == data:
                break
            n = n.next
        if n.next is None:
            print("node not present ...can't delete")
            return
        n.next = n.next.next


if __name__ == '__main__':
    l1 = LinkedList()
    l1.beginInsert(10)
    l1.beforenode(20, 10)
    l1.beforenode(30, 20)
    l1.beforenode(40, 10)
    l1.del_by_value(10)
    l1.printList()
    # l1.head = Node(1)
    # second = Node(2)
    # third = Node(3)
    # l1.head.next = second
    # second.next = third
    # l1.printList()
    # l1.beginInsert(0)
    # print()
    # l1.printList()
    # print()
    # l1.endInsert(4)
    # l1.printList()
    # print()
    # l1.afternode(3.5, 3)
    # l1.printList()
    # print()
    # l1.beforenode(1.5,2)
    # l1.printList()
    # print()
    # l1.del_begin()
    # l1.printList()
    # print()
    # l1.del_end()
    # l1.printList()
    # print()
    # l1.del_mid(10)
    # l1.printList()




