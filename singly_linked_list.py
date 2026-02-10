class Node:
    def __init__(self, d):
        self.data = d
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None



    def insert_first(self, x):
        a = Node(x)
        a.next = self.head
        self.head = a

    def insert_last(self, x):
        a = Node(x)
        if self.head is None:
            self.head = a
            return
        c = self.head
        while c.next:
            c = c.next
        c.next = a

    def insert_after(self, x, y):
        c = self.head
        while c:
            if c.data == x:
                a = Node(y)
                a.next = c.next
                c.next = a
                return
            c = c.next
        print("not found")

    def insert_before(self, x, y):
        if self.head is None:
            print("list is empty")
            return
        if self.head.data == x:
            self.insert_first(y)
            return

        c = self.head
        while c.next:
            if c.next.data == x:
                a = Node(y)
                a.next = c.next
                c.next = a
                return
            c = c.next
        print("not found")

    

    def del_first(self):
        if self.head is None:
            print("error 0")
            return
        self.head = self.head.next

    def del_last(self):
        if self.head is None:
            print("error 0")
            return
        if self.head.next is None:
            self.del_first()
            return
        c = self.head
        while c.next.next:
            c = c.next
        c.next = None

    def del_after(self, x):
        c = self.head
        while c and c.next:
            if c.data == x:
                c.next = c.next.next
                return
            c = c.next
        print("not found")

    def del_before(self, x):
        if self.head is None or self.head.next is None:
            print("error")
            return
        if self.head.next.data == x:
            self.del_first()
            return

        c = self.head
        while c.next and c.next.next:
            if c.next.next.data == x:
                c.next = c.next.next
                return
            c = c.next
        print("not found")

    def del_x(self, x):
        if self.head is None:
            print("error 0")
            return
        if self.head.data == x:
            self.del_first()
            return

        c = self.head
        while c.next:
            if c.next.data == x:
                c.next = c.next.next
                return
            c = c.next
        print("not found")

    def del_all(self):
        self.head = None


    def display(self):
        t = self.head
        while t:
            print(t.data, end=" -> ")
            t = t.next
        print("None")
