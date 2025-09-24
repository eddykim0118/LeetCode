# Well, 
# First things first, if we want to be able to evict an lru, we need to be able to track recency
# We need to be able to find which one is the lru
# Also, we need to be able to move items to front fast
# That means we need to have something that will pull to the front really fast

# I think we will need to use Node and a dummy nodes (head and tail) so that we can both move it fast and track lru

# O(1) lookups (maybe by key) mean hashtable --> direct access to Node objects
# O(1) eviction of LRU means doubly linked list

# So now, we are going to start with nodes, let's think of what has to be inside a node
# 1. key-value
# 2. prev and next <- this would be to track what was used before and after

#Looks like both key and value are in numbers [key, value]

class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    # Data Structure Design

    def __init__(self, capacity: int):
        ''' 
        Initialize the LRU cache with positive size "capacity (int)" 
        '''
        self.capacity = capacity
        self.cache = {} # would dictionary the one to use right now? 

        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        '''
        If key exists, Return the value of the "key (int)"
        If key does not exist, Return -1
        
        Must have time-complexity of O(1) 
        '''
        if key in self.cache:
            node = self.cache[key]
            self._move_to_front(node)
            return node.value
        
        return -1


    def put(self, key: int, value: int) -> None:
        '''
        If key exists, 
            UPDATE the value of the key
        If key does not exist, 
            ADD the key-value pair to the cache
        If the number of keys exceeds the capacity from this operation
            EVICT the least recently used key

        Must have time-complexity of O(1) 
        '''
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            self._move_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                # evict
                self._evict_lru()

            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)

    def _unlinking(self, node):
        # unlinking
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node):
        # insert to the front
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _move_to_front(self, node):
        self._unlinking(node)
        self._add_to_front(node)

    def _evict_lru(self):
        lru_node = self.tail.prev
        self._unlinking(lru_node)
        del self.cache[lru_node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)