class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # HashMap: key --> Node

        # Create dummy head and tail nodes for easier list manipulation
        self.head = Node(0, 0) # Most recently used (dummy)
        self.tail = Node(0, 0) # Least recently used (dummy)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Move to front (mark as most recently used)
            self._move_to_front(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing key
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
        else:
            # Add new key
            if len(self.cache) >= self.capacity:
                # Evict least recently used (tail.prev)
                self._evict_lru()
            
            # Create new node and add to front
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)

    def _move_to_front(self, node):
        """Move existing node to front (most recently used position)"""
        self._remove_node(node)
        self._add_to_front(node)
    
    def _remove_node(self, node):
        """Remove node from its current position in the list"""
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add_to_front(self, node):
        """Add node right after head (most recently used position)"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def _evict_lru(self):
        """Remove least recently used item (tail.prev)"""
        lru_node = self.tail.prev
        self._remove_node(lru_node)
        del self.cache[lru_node.key]
    

class Node:
    """Doubly linked list node for storing key-value pairs"""
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)