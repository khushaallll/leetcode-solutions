from dataclasses import dataclass

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def build_linked_list(values):
        dummy = ListNode()
        current = dummy

        for value in values:
            current.next = ListNode(value)
            current = current.next

        return dummy.next

    def display_linked_list(head: ListNode):
        current = head

        while current is not None:
            print(current.val, end = " -> " if current.next is not None else "")
            current = current.next
