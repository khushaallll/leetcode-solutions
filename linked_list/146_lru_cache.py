class DoubleEndedNode:
    def __init__(self, key = None, val = None):
        self.next = None
        self.prev = None
        self.val = val
        self.key = key

class DoublyLinkedList:
    def __init__(self):
        self.head = DoubleEndedNode()
        self.tail = DoubleEndedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_front(self, node: DoubleEndedNode) -> None:

        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def remove_last(self) -> None:
        if self.tail.prev is self.head: # Empty list
            return None

        node = self.tail.prev
        self.remove(node)
        return node

    def remove(self, node: DoubleEndedNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_map = dict()
        self.cache = DoublyLinkedList()


    def get(self, key: int) -> int:

        if key not in self.node_map:
            return - 1

        node: DoubleEndedNode = self.node_map.get(key)
        self.cache.remove(node)
        self.cache.add_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        current_capacity = len(self.node_map)

        if key not in self.node_map:        # add to node map
            node = DoubleEndedNode(key = key, val = value)
            if current_capacity == self.capacity: # remove last node from cache
                last_node = self.cache.remove_last()
                del self.node_map[last_node.key]
                
            self.node_map[key] = node
            self.cache.add_to_front(node)
                
        else: # update the key
            node: DoubleEndedNode = self.node_map.get(key)
            node.val = value
            self.cache.remove(node)
            self.cache.add_to_front(node)
            return


lRUCache = LRUCache(2);
lRUCache.put(1, 1); # cache is {1=1}
lRUCache.put(2, 2); # cache is {1=1, 2=2}
a = lRUCache.get(1);    # return 1
print(a)
lRUCache.put(3, 3); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
b = lRUCache.get(2);    # returns -1 (not found)
print(b)
lRUCache.put(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
c = lRUCache.get(1);    # return -1 (not found)
print(c)
d = lRUCache.get(3);    # return 3
print(d)
e = lRUCache.get(4);    # return 4
print(e)


