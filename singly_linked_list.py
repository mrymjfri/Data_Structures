class node :
    def __init__(self , d):
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
                    return 
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

    def del_first(self):
        if self.head is None:
            print ("error 0")
            return 
        C=self.head
         self.head=C.next
         del C
    def del_last(self):
        if self.head is None:
            print ("error 0")
            return 
        if self.head.next is None:
            self.del_firs()
            return 
        C=self.head
        while C.next.next:
             C=C.next
         del C.next
         C.next=None
    def del_after(self,x):
        if self.head is None:
            print ("error 0")
            return 
        if self.head.next is None:
            print ("error 1")
            self.del_firs()
            return 
        C=self.head
        while C.next.next:
             if C.data==x:
                 a=C.next
                 C.next=a.next
                  del a
                  return 
             C=C.next
        print ("not found")

    def del_befor(self,x):
        if self.head is None:
            print ("error 0")
            return 
        if self.head.data ==x:
            print ("error 1")
            return 
        if self.head.next is None:
            print ("error 2")
        if self.head.next.data=x:
            self.del_first()
            return 
        if self.head.next.next is None:
            print ("error 3")
            return 
        C=self.head
        while C.next.next:
             if C.next.next.data==x:
                 a=C.next
                 C.next=a.next
                  del a
                  return 
             C=C.next
        print ("not found")

    def del_all(self):
        while self.head:
            self.del_first()
    def del_x(self , x):
        if self.head is None:
            print ("error 0")
            return 
        if self.head.data==x:
            self.del_firs()
            return 
        C=self.head
        while C.next:
             if C.next.data==x:
                 a=C.next
                 C.next=a.next
                  del a
                  return 
             C=C.next
        print ("not found")

    def display (self):
        T=self.head
         while T !=None:
            print (T.data , end=" ")
            T=T.next
         print ("Null")
