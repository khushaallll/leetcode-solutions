from Linked_List import ListNode, LinkedList

def reverseKGroup(head: ListNode | None, k: int) -> ListNode | None:
    dummy = ListNode(0, head)
    group_prev = dummy

    while True:

        # Step 1 - Check the group's validity
        kth = group_prev
        for _ in range(k):
            kth = kth.next
            if kth is None:
                return dummy.next
        
        group_next = kth.next
        
        # Reversal of the group
        prev = group_next
        current = group_prev.next
        while current is not group_next:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        # Stitch the first element on the reversed linked list to group prev
        old_first = group_prev.next         # this is the head currently which is supposed to be the tail
        group_prev.next = kth               # kth became the new head 
        group_prev = old_first              # set the tail as group prev for next group of nodes

head = [1,2,3,4,5]
k = 2

head = LinkedList.build_linked_list(head)
k_rev = reverseKGroup(head, k)
print(LinkedList.display_linked_list(k_rev))