from Linked_List import LinkedList, ListNode

def removeNthFromEnd(head: ListNode | None, n: int) -> ListNode | None:
    dummy = ListNode(0, head)
    leader = dummy
    follower = dummy
    leader_hops = 0
    prev = ListNode()
    flag = False

    while leader.next is not None:

        if leader_hops == n-1:
            flag = True

        leader = leader.next
        leader_hops += 1
        
        if flag:
            prev = follower
            follower = follower.next
    
    prev.next = follower.next
    return dummy.next

head = [1]
n = 1
linked_list= LinkedList.build_linked_list(head)
modified_LL = removeNthFromEnd(linked_list, n)
LinkedList.display_linked_list(modified_LL)