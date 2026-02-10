class C_Queue:
    def __init__(self, max=100):
        self.list = [None] * max
        self.front = -1
        self.rear = -1
        self.size = max

    def insert(self, x):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
            return
        if self.front == -1:
            self.front = 0
            self.rear = 0
            self.list[self.rear] = x
        else:
            self.rear = (self.rear + 1) % self.size
            self.list[self.rear] = x

    def delete_(self):
        if self.front == -1:
            print("Queue is empty")
            return None
        k = self.list[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return k

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def show_valid(self):
        if self.front == -1:
            print("Queue is empty")
            return
        i = self.front
        print("Queue contents:", end=" ")
        while True:
            print(self.list[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

    def find(self, x):
        if self.is_empty():
            print("Queue is empty")
            return None
        i = self.front
        while True:
            if self.list[i] == x:
                return i
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print("Not found")
        return None

    def replace(self, x, y):
        if self.is_empty():
            print("Queue is empty")
            return
        i = self.front
        while True:
            if self.list[i] == x:
                self.list[i] = y
            if i == self.rear:
                break
            i = (i + 1) % self.size
                          
