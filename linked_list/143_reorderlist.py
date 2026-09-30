from Linked_List import LinkedList, ListNode

def reorderListBruteForce(head: ListNode | None) -> None:
    current = head
    while current.next is not None and current.next.next is not None:
        X = current.next
        # print(f"[current] val: {current.val} next: {current.next.val}")
        traveller = current
        while traveller.next.next is not None:
            # print(f"[traveller] val: {traveller.val} next: {traveller.next.val}")
            traveller = traveller.next
        
        move = traveller.next
        traveller.next = None
        # print("Traveller Traverse ends.")
        # print(f"[traveller] val: {traveller.val} next: {traveller.next}")
        current.next = move
        move.next = X
        current = X
        # break
    
    return head

def reorderList(head: ListNode | None) -> None:

    # Step 1: Split the Linked List in half
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    second = slow.next
    slow.next = None

    # Step 2: Reverse the second half
    prev = None
    current = second
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    second = prev   # prev holds the head of the reversed second half

    # Merge slow and current
    first = head

    while second is not None:
        first_next = first.next
        second_next = second.next

        first.next = second
        second.next = first_next

        first = first_next
        second = second_next
    return head

head = [1,2,3,4, 5]
linked_list = LinkedList.build_linked_list(head)
print("Unordered Linked List: ")
LinkedList.display_linked_list(linked_list)
print("")

head_ordered = reorderList(linked_list)
print("\nOrdered Linked List: ")
LinkedList.display_linked_list(head_ordered)



