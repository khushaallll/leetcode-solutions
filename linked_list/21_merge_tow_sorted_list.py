
from Linked_List import LinkedList, ListNode

def mergeTwoLists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
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

list1 = [1,2,4]
list2 = [1,3,4]
linked_list_1= LinkedList.build_linked_list(list1)
linked_list_2= LinkedList.build_linked_list(list2)
merged = mergeTwoLists(linked_list_1, linked_list_2)
LinkedList.display_linked_list(merged)