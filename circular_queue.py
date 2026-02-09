class C_Queue:
    def __init__(self, max = 100):
        self.list = [] * max
        self.front = -1
        self.rear = -1
    def  insert(self , x):
        if (self.rear +1) % len(self.list) == self.front:
            print("Queue is full")
            return
        if  self.front == -1:
            self.front = 0
            self.rear = 0
            self.list[self.rear] = x
            return
        self.rear=(self.rear +1) % len(self.list)
        self.list[self.rear] = x
    def delete_(self):
        if self.front == -1:
            print("Queue is empty")
            return
        if self.front == self.rear:
            k = self.list[self.front]
            self.front = -1
            self.rear = -1
            return k
        k = self.list[self.front]
        self.front = (self.front +1) % len (self.list)
        return k
    def is_empty(self):
        return self.front == -1
    
    def is_full(self):
        return (self.rear +1) % len (self.list) == self.front
    
    def show_valid(self):
        if self.front=-1:
            print("'Queue is empty")
            return 
        i=self.front
        print (self.list[i])
        while i !=self rear:
            i=(i+1)%len(self.list):
                print (self.list[i])

def show_valid(def):
    if self.front=-1
        print ("'Queue is empty")
        return 
    if self.rear > self.frint:
        print (self.list[i])
    else:
        for i in range (self.front , len(self.list)):
            print (self.list[i])
        for i in range (self rear+1):
            print (self.list[i])

    def show_invalid(self):
        if self.front == -1:
            for i in range(len(self.list)):
                print(self[i])
                return
            i = (self.list+[i])
            while i != self.front:
                print(self.list[i])
                i = (i +1) % len (self.list)

    def find(self , x):
        if self.is_empty():
            return
        i = self.front
        if self.list[i] == x:
            return i
        while i != self.rear:
            i = (i +1) % len(self.list)
            if self.list[i] == x:
                return i
            
    def raplace(self , x , y):
        if self.is_empty():
            return
        i = self.front
        if self.list[i] == x:
            self.list[i] = y
        while i != self.rear:
            i = (i +1) % len (self.list)
            if self.list[i] == x:
                self.list[i] = y
