class ListNode:
    def __init__(self, val):
        self.val = val     # the values in the node
        self.next = None    # the note that points to next node


first = ListNode(1)
second = ListNode(2)
third = ListNode(3)

first.next = second         # node 1 points to node 2
second.next = third         # node 2 points to node 3

# third is already None, so it is the end.

# --------- USE -----------


"""
Inserting in an Array is expensive. Have to move elements

In Linked List, inserting is cheap.
Just change the where the node points.

If suppose we want to insert 99 between 1 and 2
Earlier -> [1] -> [2] -> [3]

1. Create a new node for value 99.
2. Make node 1 point to 99 instead of 2
3. Make 99 point to node 2
After: 
[1] -> [99] -> [2] -> [3]

Tradeoff:
1. Array is fast to access any element directly, slow to insert or delete.
2. Linked List is slow to access element (have to walk from start), fast to insert or delete once you are at right spot.
"""

current = first
while current is not None:
    print(f"Current value: {current.val} ----- Current Next: {current.next}")
    current = current.next

print(type(current))