class Stack:
    def __init__(self, limit=1000):
        self.st = []
        self.lim = limit

    def push(self, x):
        if len(self.st) >= self.lim:
            print("stack is full")
            return None
        self.st.append(x)

    def pop(self):
        if not self.st:
            print("stack is empty")
            return None
        return self.st.pop()

    def peek(self):
        if not self.st:
            print("stack is empty")
            return None
        return self.st[-1]

    # ✅ همه ایندکس‌های x را برمی‌گرداند
    def find_all(self, x):
        indexes = []
        for i in range(len(self.st)):
            if self.st[i] == x:
                indexes.append(i)
        return indexes

    # ✅ اولین ایندکس x
    def find_first(self, x):
        for i in range(len(self.st)):
            if self.st[i] == x:
                return i
        return -1

    # ✅ آخرین ایندکس x
    def find_last(self, x):
        for i in range(len(self.st) - 1, -1, -1):
            if self.st[i] == x:
                return i
        return -1

    # ✅ جایگزینی x با y
    def replace(self, x, y):
        for i in range(len(self.st)):
            if self.st[i] == x:
                self.st[i] = y


test = Stack(10)

test.push(23)
test.push(110)
test.push(57)
test.push(110)

print(test.peek())          # 110
print(test.pop())           # 110

print(test.find_all(110))   # [1]
print(test.find_first(57))  # 2
print(test.find_last(110))  # 1

test.replace(23, 999)
print(test.st)              # [999, 110, 57]
