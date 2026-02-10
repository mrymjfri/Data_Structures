class dnode:
    def __init__(self, x):
        self.Data = x
        self.next = None
        self.back = None


class dlinked_list:
    def __init__(self):
        self.head = None

    def ins_first(self, x):
        a = dnode(x)
        if self.head is not None:
            a.next = self.head
            self.head.back = a
        self.head = a

    def ins_last(self, x):
        if self.head is None:
            self.ins_first(x)
            return
        c = self.head
        while c.next:
            c = c.next
        a = dnode(x)
        c.next = a
        a.back = c

    def ins_after(self, x, y):
        c = self.head
        while c:
            if c.Data == x:
                if c.next is None:
                    self.ins_last(y)
                    return
                a = dnode(y)
                a.next = c.next
                a.back = c
                c.next.back = a
                c.next = a
                return
            c = c.next
        print("not found")

    def ins_before(self, x, y):
        c = self.head
        while c:
            if c.Data == x:
                if c.back is None:
                    self.ins_first(y)
                    return
                a = dnode(y)
                a.next = c
                a.back = c.back
                c.back.next = a
                c.back = a
                return
            c = c.next
        print("not found")

    def del_first(self):
        if self.head is None:
            print("error")
            return
        c = self.head
        self.head = c.next
        if self.head:
            self.head.back = None
        del c

    def del_last(self):
        if self.head is None:
            print("error")
            return
        c = self.head
        while c.next:
            c = c.next
        if c.back is None:
            self.del_first()
            return
        c.back.next = None
        del c

    def del_before(self, x):
        c = self.head
        while c:
            if c.Data == x:
                if c.back is None:
                    print("no node before head")
                    return
                a = c.back
                if a.back:
                    a.back.next = c
                    c.back = a.back
                else:
                    self.head = c
                    c.back = None
                del a
                return
            c = c.next
        print("not found")

    def del_after(self, x):
        c = self.head
        while c:
            if c.Data == x:
                if c.next is None:
                    print("no node after")
                    return
                a = c.next
                c.next = a.next
                if a.next:
                    a.next.back = c
                del a
                return
            c = c.next
        print("not found")

    def del_x(self, x):
        c = self.head
        while c:
            if c.Data == x:
                if c.back is None:
                    self.del_first()
                    return
                if c.next is None:
                    self.del_last()
                    return
                c.back.next = c.next
                c.next.back = c.back
                del c
                return
            c = c.next
        print("not found")
            
