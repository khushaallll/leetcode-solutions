
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
    
    while len(lists) > 1: # runs until your list only has one linked list

        merged_round = []
        for i in range(0, len(lists), 2):
            list1 = lists[i]
            list2 = lists[i+1] if i+1 < len(lists) else None

            merged = mergeTwoLists(list1, list2)
            merged_round.append(merged)
        
        lists = merged_round # replace old list with new one
    
    return lists[0]
    
