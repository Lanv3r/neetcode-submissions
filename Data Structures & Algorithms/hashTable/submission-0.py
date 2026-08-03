class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = [None] * self.capacity
        self.size = 0 

    def hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash(key)

        while True:
            if self.map[index] is None:
                self.map[index] = Pair(key, value)
                self.size += 1
                if self.size >= self.capacity * 0.5:
                    self.resize()
                return
            if self.map[index].key == key:
                self.map[index].val = value
                return  
            index = (index + 1) % self.capacity

    def get(self, key: int) -> int:
        index = self.hash(key)
        while self.map[index] is not None:
            if self.map[index].key == key:
                return self.map[index].val
            index = (index + 1) % self.capacity
        return -1

    def remove(self, key: int) -> bool:
        index = self.hash(key)
        while self.map[index] is not None:
            if self.map[index].key == key:
                self.map[index] = None
                self.size -= 1 
                new_index = (index + 1) % self.capacity
                while self.map[new_index] is not None:
                    p_key, p_val = self.map[new_index].key, self.map[new_index].val
                    self.map[new_index] = None
                    self.size -= 1
                    self.insert(p_key, p_val)
                    new_index = (new_index + 1) % self.capacity
                return True
            index = (index + 1) % self.capacity

        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity *= 2
        new_map = [None] * self.capacity
        old_map = self.map
        self.map = new_map
        self.size = 0
        for pair in old_map:
            if pair is not None:
                self.insert(pair.key, pair.val)