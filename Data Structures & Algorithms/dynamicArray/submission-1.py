class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [0 for i in range(capacity)]
        self.size = 0
        self.cap = capacity

    def get(self, i: int) -> int:
        return self.arr[i]
            
    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size >= self.cap:
            self.resize()
        self.arr[self.size] = n
        self.size += 1


    def popback(self) -> int:
        self.size -= 1
        return self.arr[self.size]

    def resize(self) -> None:
        self.arr += [0 for i in range(self.cap)]
        self.cap *= 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.cap
