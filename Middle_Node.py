class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None




linkedList = LinkedList(2)
linkedList.next = LinkedList(7)
linkedList.next.next = LinkedList(3)
linkedList.next.next.next = LinkedList(5)
# linkedList.next.next.next.next = LinkedList(9)
# linkedList.next.next.next.next.next = LinkedList(10)

def middleNode(linkedList):
    # current = linkedList
    # slow = current.next
    # fast = current.next.next

    # if slow is None:
    #     # print("Printing current")
    #     return current.value
    # else:
    #     # print("Printing slow")
    #     slow.value

    # while fast is not None:
    #     if fast.next is None:
    #         return slow.next.value
    #     else:
    #         fast = fast.next

    # current = linkedList
   
    # if current.next is None:
    #     print("Printing current")
    #     return current.value
    
    # if current.next.next is None:
    #     print("Printing slow")
    #     return current.next.value
    # else:

    #     while current.next is not None:
    #         if current.next.next is None:
    #             print("fast value:",current.next.value)
    #             return current.value
    #         else:

    #             current = current.
    
    slowNode = linkedList
    fastNode = linkedList
    while fastNode and fastNode.next:
        slowNode = slowNode.next
        fastNode = fastNode.next.next

    return slowNode.value
    
    print("Complete")

print("Middle Node is:",middleNode(linkedList))

