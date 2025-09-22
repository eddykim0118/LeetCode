class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    
    def __init__(self, capacity: int):
       # ititialize the LRU cache with positive size capacity
       # in this case, hashmap and doubly linked would be good to use
       # also, I think we probably would need to make dummy cases as Head and Tail
       # capacity = how much key-value it can hold

       self.capacity = capacity
       self.cache = {} # hashmap, 
       # Stores key (the cache key) → Node mappings (a Node object (which contains the key, value, and links to neighbors))
       
       # Node(0, 0) -> dummy
       ## this is simply a place holder
       self.head = Node(0, 0) # always before the least recently used node.
       self.tail = Node(0, 0) # always after the most recently used node.

       # The head and tail are initially connected to each other:
       self.head.next = self.tail
       self.tail.prev = self.head
    
    def get(self, key: int) -> int:
        # put key-value pari
        # if key esists, update and move to front
            # return the value of the "key"
            # if new key and at capacity, evict LRU item first
        # if the key doesn't exist, return -1
        
        if key in self.cache:
            node = self.cache[key]
            self._move_to_front(node)
            return node.value
        
        return -1

    def put(self, key: int, value: int) -> None:
        # update the value key if the key esists
        # add the key-value pair to the cache
        # if the number of keys exceeds the capacity from the operation
        # -> evict the least recently used key
        
        if key in self.cache: # self.cache = dict mapping keys->nodes for O(1) lookup
            node = self.cache[key] 
            node.value = value

            # to move the node to the head of the doubly linked list (marking)
            # -> marking it most recently used
            self._move_to_front(node) 
        else:
            # Add new key
            if len(self.cache) >= self.capacity:
                # Evict least recently used (tail.prev)
                self._evict_lru() 
            
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)


    def _move_to_front(self, node):
        self._remove_node(node) # detaching the node
        self._add_to_front(node) # inserting right after the dummy head node

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
