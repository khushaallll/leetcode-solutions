class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

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

class RandomLinkedList:

    def build_random_list(pairs):
        if not pairs:
            return None

        # Step 1: create all nodes first, just with values
        nodes = [Node(val) for val, _ in pairs]

        # Step 2: wire up .next and .random using indices
        for i, (val, random_index) in enumerate(pairs):
            if i + 1 < len(nodes):
                nodes[i].next = nodes[i + 1]
            if random_index is not None:
                nodes[i].random = nodes[random_index]

        return nodes[0]

    def print_random_list(head):
        current = head
        index_map = {}
        # first pass: assign each node an index, for printing random pointers
        node = head
        i = 0
        while node is not None:
            index_map[node] = i
            node = node.next
            i += 1

        current = head
        while current is not None:
            random_index = index_map[current.random] if current.random else None
            print(f"[{current.val}, {random_index}]", end=" -> ")
            current = current.next
        print("None")