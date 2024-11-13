class DynamicArray:

    def __init__(self, capacity: int):
        self.Capacity = capacity
        self.Lenght = 0
        self.Array = [0] * self.Capacity

    def get(self, i: int):
        return self.Array[i]

    def set(self, i: int, n: int):
        self.Array[i] = n

    def pushback(self, n: int):
        if self.Lenght == self.Capacity:
            self.resize()

        self.Array[self.Lenght] = n
        self.Lenght += 1

    def popback(self) -> int:
        if self.Lenght > 0:
            # soft delete the last element
            self.Lenght -= 1
        # return the popped element
        return self.Array[self.Lenght]

    def resize(self):
        self.Capacity = self.Capacity * 2
        new_arr = [0] * self.Capacity

        for i in range(self.Lenght):
            new_arr[i] = self.Array[i]
        self.Array = new_arr

    def getSize(self) -> int:
        return self.Lenght

    def getCapacity(self):
        return self.Capacity











array = DynamicArray(7)
print(array.lenght())



