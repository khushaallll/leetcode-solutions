from typing import Optional
from Linked_List import Node, RandomLinkedList

## 1 - With O(N) SPACE COMPLEXITY - MAP
def copyRandomList_extra_space(head: 'Optional[Node]') -> 'Optional[Node]':
    node_map = {}
    current = head

    ## Pass 1: Create a mapping of nodes
    while current is not None:
        node_map[current] = Node(current.val)
        current = current.next

    ## Pass 2: Wire up the copy pointers
    current = head                          # Reset current
    while current is not None:
        duplicate = node_map.get(current)
        duplicate.next = node_map.get(current.next, None)
        duplicate.random = node_map.get(current.random)
        current = current.next
    
    return node_map.get(head)

# 2 - O(1)  TIME SPACE COMPLEXITY
def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
    if head is None:
        return None
    
    current = head

    # Pass 1 - Interleave
    while current is not None:
        next_node = current.next
        duplicate_node = Node(current.val, next_node)
        current.next = duplicate_node
        current = next_node

    # Pass 2 - Random Connections
    current = head                  # reset current
    counter = 0
    prev = None
    while current is not None:
        if counter % 2 == 0:
            prev = current
        else:
            current.random = prev.random.next if prev.random else None
        counter += 1
        current = current.next

    # Alternative for pass 2
    """ while current is not None:
            if current.random is not None:
                current.next.random = current.random.next
            current = current.next.next
    """

    # Pass 3 - Un-interleave
    
    current = head
    copy_head = head.next

    while current is not None:
        duplicate_node = current.next
        current.next = duplicate_node.next
        duplicate_node.next = duplicate_node.next.next if duplicate_node.next else None
        current = current.next
    
    return copy_head.next


pairs = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
pairs = []
head = RandomLinkedList.build_random_list(pairs)

deep_copy = copyRandomList(head)
RandomLinkedList.print_random_list(deep_copy)