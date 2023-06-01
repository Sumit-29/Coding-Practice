class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# Linked list = 1 -> 1 -> 3 -> 4 -> 4 -> 4 -> 5 -> 6 -> 6
#  Output = 1 -> 3 -> 4 -> 5 -> 6


linkedList = LinkedList(1)
linkedList.next = LinkedList(1)
linkedList.next.next = LinkedList(3)
linkedList.next.next.next = LinkedList(4)
linkedList.next.next.next.next = LinkedList(4)
linkedList.next.next.next.next.next = LinkedList(4)
linkedList.next.next.next.next.next.next = LinkedList(5)
linkedList.next.next.next.next.next.next.next = LinkedList(6)
linkedList.next.next.next.next.next.next.next.next = LinkedList(6)


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    # if linkedList is None:
    #     return None
    # print("Value:",linkedList.value)
    # print("X:",linkedList.next.value)
    # if linkedList.value == linkedList.next.value:
    #     linkedList.next = linkedList.next.next
    
    
    
    # removeDuplicatesFromLinkedList(linkedList.next)
    cur = linkedList
    while cur.next is not None:
        
        if cur.value == cur.next.value:
            cur.next = cur.next.next
            
        else:
            cur = cur.next
        
    return linkedList
    
print(removeDuplicatesFromLinkedList(linkedList))    