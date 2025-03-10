class CustomList:
    def __init__(self, capacity=10):
        self.capacity=capacity
        self.size=0
        self.array =[None]* self.capacity

    def resize(self):
        new_capacity=self.capacity*2
        new_array=[None]*new_capacity
        for i in range(self.size):
            new_array[i]=self.array[i]
        self.array= new_array
        self.capacity = new_capacity

    def append(self,element):
        if self.size == self.capacity:
            self.resize()
        self.array[self.size]= element
        self.size +=1

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range!")
        return self.array[index]
    

    def set(self, index, element):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range!")
        if self.size == self.capacity:
            self.resize()
        for i in range(self.size, index):
            self.array[i] = self.array[i]
        self.array[index] = element
        
    def size(self):
        return self.size
    

if __name__ == "__main__":

    custom_list = CustomList()
    custom_list.append(5)
    print(f"Element at index 0:{custom_list.get(0)}")

    custom_list.set(0, 10)
    print(f"Element at index 0:{custom_list.get(0)}")

    print(f"Current size: {custom_list.size}")