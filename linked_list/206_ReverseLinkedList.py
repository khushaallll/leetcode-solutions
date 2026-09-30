class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(values):
    dummy = ListNode()  # starting point, throw away box/node
    current = dummy     # 

    for v in values:
        current.next = ListNode(v)      # attach a new box/node
        current = current.next          # move to that new box/node

    return dummy.next                   # starting point of the real Linked List

def display_linked_list(head):
    current = head

    while current.next is not None:
        print(current.val, end = " -> ")
        current = current.next

    print("None")

def reverseList(head: ListNode | None) -> ListNode | None:
    current = head
    prev = None
    while current is not None:
        next_node = current.next        # save next node
        current.next = prev             # flip the pointer backwards
        prev = current                  # move prev forward
        current = next_node             # move the current forward

    return prev

head = [1,2,3,4,5]
head_LL = build_linked_list(head)
# display_linked_list(head_LL)
he = reverseList(head_LL)
display_linked_list(he)