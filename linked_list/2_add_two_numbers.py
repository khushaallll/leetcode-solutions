from Linked_List import ListNode, LinkedList

def addTwoNumbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    
    dummy = ListNode()
    current = dummy
    carry = 0

    while l1 is not None or l2 is not None:

        num1 = l1.val if l1 else 0
        num2 = l2.val if l2 else 0
        
        addition = num1 + num2 + carry
        if addition < 10:
            current.next = ListNode(addition)
        else:
            carry = 1
            current.next = ListNode(addition-10)


        current = current.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    current.next = ListNode(carry)
    return dummy.next

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

l1_ll = LinkedList.build_linked_list(l1)
l2_ll = LinkedList.build_linked_list(l2)
LinkedList.display_linked_list(l1_ll)
print("")
LinkedList.display_linked_list(l2_ll)
print("-----------------------------")
added = addTwoNumbers(l1_ll, l2_ll)
LinkedList.display_linked_list(added)
