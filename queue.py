class Queue:
    def __init__(self, max=100):
        self.list = [None] * max
        self.front = -1
        self.rear = -1

    def insert(self, x):
        if self.rear >= len(self.list) - 1:
            print("Queue is Full")
            return
        if self.front == -1:
            self.front = 0
            self.rear = 0
            self.list[self.rear] = x
        else:
            self.rear += 1
            self.list[self.rear] = x

    def del_(self):
        if self.front == -1:
            print("Queue is empty")
            return None
        k = self.list[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front += 1
        return k

    def display(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            for i in range(self.front, self.rear + 1):
                print(self.list[i], end=" ")
            print()
        
