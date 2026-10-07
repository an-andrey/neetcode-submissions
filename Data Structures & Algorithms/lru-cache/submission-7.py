class DLLNode:
    def __init__(self, val, key, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None  # MRU
        self.tail = None  # LRU
        self.nodes = {}

    def _remove(self, node: DLLNode) -> None:
        if node.prev:
            node.prev.next = node.next
        else:
            self.tail = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.head = node.prev

        node.prev = None
        node.next = None

    def _append_to_head(self, node: DLLNode) -> None:
        if not self.head:
            self.head = self.tail = node
            return

        self.head.next = node
        node.prev = self.head
        node.next = None
        self.head = node

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1

        node = self.nodes[key]
        self._remove(node)
        self._append_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            node.val = value
            self._remove(node)
            self._append_to_head(node)
            return

        if len(self.nodes) == self.capacity:
            lru = self.tail
            self._remove(lru)
            del self.nodes[lru.key]

        new_node = DLLNode(value, key)
        self.nodes[key] = new_node
        self._append_to_head(new_node)