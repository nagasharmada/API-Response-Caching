from cache.node import Node
class LRUCache:
    def __init__(self,capacity:int):
        self.capacity=capacity
        self.cache={}

        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.hits=0
        self.misses=0
    def _add_node(self,node):
        node.prev=self.head
        node.next=self.head.next
        self.head.next.prev=node
        self.head.next=node
    def _remove_node(self,node):
        prev=node.prev
        nxt=node.next
        prev.next=nxt
        nxt.prev=prev
    def _move_to_Front(self,node):
        self._remove_node(node)
        self._add_node(node)
    def _pop_tail(self):
        node = self.tail.prev
        self._remove_node(node)
        return node
    
    def get(self,key):
        if key not in self.cache:
            self.misses +=1
            return None
        node = self.cache[key]
        self._move_to_Front(node)
        self.hits+=1;
        return node.value
    def put(self,key,value):
        if key in self.cache:
            node=self.cache[key]
            node.value=value
            self._move_to_Front(node)
            return
        node=Node(key,value)
        self.cache[key]=node
        self._add_node(node)

        if len(self.cache)>self.capacity:
            lru=self._pop_tail()
            del self.cache[lru.key]

