class node :
    def init(self , d):
        self.Data = d
        self.next = None




class linked_list :
    def init(self):
        self.head = None
    def insert_frist(self , x):
        if self.head == None:
            self.head = node(x)
        else:
            a = node(x)
            a.next = self.head
            self.head = a     
    def insert_last(self , x):
        if self.head == None:
            self.head = node(x)
        else:
            a = node(x)
            c = self.head
            while c.next:
                c = c.next 
            c.next = a
    def insert_after(self , x, y):
        if self.head is None:
            print("list is empty")
        else:
            c = self.head
            while c:
                if c.Data == x:
                    a = node(y)
                    a.next = c.next
                    c.next = a
                c = c.next
            print("not found")

    def insert_befor(self , x, y):
        if self.head is None:
            print("list is empty")
            return
        if self.head.Data == x:
            self.insert_frist(y)
            return
       C=self.head
        while c.next:
            if c.next.Data == x:
                a = node(y)
                a.next = c.next
                C.next = a
                return
            C= C.next
        print("not found")
