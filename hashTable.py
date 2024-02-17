
class HashTable:
    def __init__(self) -> None:
        self.Max = 100
        self.arr = [None for i in range(self.Max)]
    
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % 100
    
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__ (self, key):
        h = self.get_hash(key)
        return self.arr[h]
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

t = HashTable()
t['march 6'] = 130
t['march 3'] = 13
t['march 1'] = 5
del t['march 6']
print(t['march 6']) # None
for i in t.arr:
    if i is not None:
        print(i, end=" ")