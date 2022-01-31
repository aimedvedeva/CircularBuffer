class CircularBuffer:
    def __init__(self, size):
        self.capacity = size
        self.data = []
        self.tail_index = 0
        
    def write(self, value):
        
        if (self.tail_index < self.capacity):
            self.data.append(value)
            
       	elif (self.tail_index >= self.capacity):
            self.data[self.tail_index % self.capacity] = value

        self.tail_index += 1               
        
    def read(self, size):
        if (size > len(self.data)):
            return 

        data = []
        
        index = self.tail_index % self.capacity
        while(size > 0 and index < len(self.data)):
            data.append(self.data[index])
            index += 1
            size -= 1
            
        index = 0
        while(index < size):
            data.append(self.data[index])
            index += 1
            
        return data    
        
buffer = CircularBuffer(4)
buffer.write(1)
buffer.write(2)
buffer.write(3)
buffer.write(4)
buffer.write(5)
buffer.write(6)
buffer.write(7)
print(buffer.read(4))

buffer.write(8)
buffer.write(9)

print(buffer.read(3))


class CircularBuffer:
    def __init__(self, size):
        self.capacity = size
        self.data = []

    def write(self, value):
        self.data.append(value)
        
        if (len(self.data) == self.capacity):
            self.count = 0
            self.__class__ = self.__Full

    def readAll(self):
        return self.data
    
    class __Full:
        
        def write(self, value):
            self.data[self.count] = value
            self.count = (self.count + 1) % self.capacity
            
        def readAll(self):
            return self.data[self.count : ] + self.data[ : self.count]

buffer = CircularBuffer(2)
buffer.write(1)
buffer.write(2)
buffer.write(3)
buffer.write(4)
buffer.write(5)
buffer.write(6)
buffer.write(7)
print(buffer.readAll())

buffer.write(8)
buffer.write(9)

print(buffer.readAll())


    