# This py script has All the DataStructures and their Implementaions
#           DataStructures Helps developer TO Structure and Orginize the data
#     -->>     1. Linked list
#     -->>     2. Doubly Linked List
#     -->>     3. Circular Linked List
#     -->>     4. Stack
#     -->>     5. Queue
#     -->>     6. Binary Search Tree
#     -->>     7. Graphs
#     -->>     8. Binary Heaps

# ------------------------- Advance Data Strutures -----------------------------------
#     -->>     9. Circular Queue
#     -->>    10. Priority Queue
#     -->>    11. Deque
#     -->>    12. Self Balancing BSTs
#     -->>    13. AVL Tree
#     -->>    14. Red Black Tree
#     -->>    15. Segment Tree
#     -->>    16. Trie
#     -->>    17. Binary Indexed Tree or Fenwick Tree
#     -->>    18. Suffix Array
#     -->>    19. K Dimensional Tree
#     -->>    20. N-array Trees
#     -->>    21. Disjoint Set
#     -->>    22. Spanning Tree
# new


#      ------------ 1. Linked list --------------


# creating a node       node has two parts one is data other is reference.  (in referance we store id of next node)
from optparse import TitledHelpFormatter


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# this linkedlist class holds the head value
class Linkedlist:
    def __init__(self):
        self.head = None

# This function helps us to view the created linked list


def Printdata(self):
    tmp = self.head
    while (tmp):
        print(tmp.data, end=" ")
        tmp = tmp.next


# The function below helps us to add new list items in the linked list
def Addnewitem(self, val):

    newNode = Node(val)
    newNode.next = self.head

    self.head = newNode


if __name__ == '__main__':
    llist = Linkedlist()
    print(llist)
    llist.head = Node(10)
    middle = Node(20)
    last = Node(30)
    print(middle)

    llist.head.next = middle
    middle.next = last

    Printdata(llist)

    # adding a new list item to linked list in the 1st
    Addnewitem(llist, 100)
    Addnewitem(llist, 200)
    Addnewitem(llist, 300)

    Printdata(llist)
