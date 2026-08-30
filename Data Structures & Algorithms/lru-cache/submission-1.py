class Node:
    def __init__(self, key:int, value:int):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.start = Node(0,0)
        self.end = Node(0,0)
        self.start.next = self.end
        self.end.prev = self.start
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def remove(self, node):
        left = node.prev
        right = node.next
        left.next = right
        right.prev = left

    def insert(self, node):
        right = self.end
        left = self.end.prev
        left.next = node
        node.prev = left
        node.next = right
        right.prev = node
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])
        else:
            self.cache[key] = Node(key, value)

        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            least_used = self.start.next
            self.remove(least_used)
            del self.cache[least_used.key]


        

  





        
