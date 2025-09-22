class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    # Caching problem ==> HashMap & Doubly-Linked List
    # We should use Node

    def __init__(self, capacity: int):
      '''
        Initialize the LRU cache with positive size "capacity"
      '''
      self.capacity = capacity
      self.cache = {}

      self.head = Node(0, 0)
      self.tail = Node(0, 0)
      self.head.next = self.tail
      self.tail.prev = self.head
    
    # O(1) avg time complexity required
    def get(self, key: int) -> int:
        '''
            If key exists, RETURN the value of "key"
            If not, RETURN -1
        '''
        if key in self.cache:
            node = self.cache[key]
            self._move_to_front(node)
            return node.value
        
        return -1

    # O(1) avg time complexity required
    def put(self, key: int, value: int) -> None:
        '''
            If key exists:
                - update the value of the key
            else:
                - add the key-value pari to the cache
                - if the number of keys exceeds the "capacity" -> evict lru key
        '''
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                self._evict_lru()
            
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)

    def _move_to_front(self, node):
        self._remove_node(node)
        self._add_to_front(node)

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _evict_lru(self):
        lru_node = self.tail.prev
        self._remove_node(lru_node)
        del self.cache[lru_node.key]