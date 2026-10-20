
from Linked_List import ListNode

def mergeTwoLists(list1: ListNode, list2: ListNode | None) -> ListNode:
    dummy = ListNode()
    tail = dummy

    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next

    if list1 is not None:
        tail.next = list1
    else:
        tail.next = list2
    
    return dummy.next

def mergeKLists(lists: list[ListNode | None]) -> ListNode | None:
    if not lists: # Edge case - if no lists provided
        return None
    

    
    return lists[0]
    
