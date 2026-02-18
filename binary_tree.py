        class Tree_Node:
    def __init__(self, x):
        self.Data = x
        self.Lchild = None
        self.Rchild = None

    # شمارش برگ‌ها
    def Count_leaves(self):
        if self is None:
            return 0
        if self.Lchild is None and self.Rchild is None:
            return 1
        c = 0
        if self.Lchild:
            c += self.Lchild.Count_leaves()
        if self.Rchild:
            c += self.Rchild.Count_leaves()
        return c

    # شمارش گره‌های درجه ۱
    def Count_1Deg(self):
        count = 0
        if (self.Lchild is not None) ^ (self.Rchild is not None):
            count = 1
        if self.Lchild:
            count += self.Lchild.Count_1Deg()
        if self.Rchild:
            count += self.Rchild.Count_1Deg()
        return count

    # شمارش گره‌های درجه ۲
    def Count_2Deg(self):
        count = 0
        if self.Lchild and self.Rchild:
            count = 1
        if self.Lchild:
            count += self.Lchild.Count_2Deg()
        if self.Rchild:
            count += self.Rchild.Count_2Deg()
        return count

    # ارتفاع درخت
    def height(self):
        if self is None:
            return 0
        hL = self.Lchild.height() if self.Lchild else 0
        hR = self.Rchild.height() if self.Rchild else 0
        return 1 + max(hL, hR)

    # پیمایش پیش‌سفری
    def pre(self):
        print(self.Data)
        if self.Lchild:
            self.Lchild.pre()
        if self.Rchild:
            self.Rchild.pre()

    # پیمایش پس‌سفری
    def post(self):
        if self.Lchild:
            self.Lchild.post()
        if self.Rchild:
            self.Rchild.post()
        print(self.Data)

    # جستجو
    def search(self, target):
        if self.Data == target:
            return True
        found = False
        if self.Lchild:
            found |= self.Lchild.search(target)
        if self.Rchild:
            found |= self.Rchild.search(target)
        return found

    # بیشینه
    def max_Tree(self):
        m = self.Data
        if self.Lchild:
            m = max(m, self.Lchild.max_Tree())
        if self.Rchild:
            m = max(m, self.Rchild.max_Tree())
        return m

    # کمینه
    def min_Tree(self):
        m = self.Data
        if self.Lchild:
            m = min(m, self.Lchild.min_Tree())
        if self.Rchild:
            m = min(m, self.Rchild.min_Tree())
        return m

    # مجموع
    def sum_Tree(self):
        s = self.Data
        if self.Lchild:
            s += self.Lchild.sum_Tree()
        if self.Rchild:
            s += self.Rchild.sum_Tree()
        return s

    # تعداد گره‌ها
    def count(self):
        c = 1
        if self.Lchild:
            c += self.Lchild.count()
        if self.Rchild:
            c += self.Rchild.count()
        return c


r = Tree_Node(10)
r.Lchild = Tree_Node(5)
r.Rchild = Tree_Node(20)
r.Lchild.Lchild = Tree_Node(3)
r.Lchild.Rchild = Tree_Node(7)

print(r.Count_2Deg())   # 2
print(r.height())       # 3
print(r.sum_Tree())     # 45
r.pre()
            
