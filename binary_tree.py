class Tree_Node:
    def __init__(self, x):
        self.Data = x
        self.Lchild = None
        self.Rchild = None


    def Count_0Deg(self):
        if self is None:
            return 0

        if self.Lchild is None and self.Rchild is None:
            return 1

        if self.Lchild is not None and self.Rchild is None:
            return self.Lchild.Count_0Deg()

        if self.Rchild is not None and self.Lchild is None:
            return self.Rchild.Count_0Deg()

        return self.Lchild.Count_0Deg() + self.Rchild.Count_0Deg()

    
    def Count_1Deg(self):
        if self is None:
            return 0

        if self.Lchild is not None and self.Rchild is None:
            return 1 + self.Lchild.Count_1Deg()

        if self.Rchild is not None and self.Lchild is None:
            return 1 + self.Rchild.Count_1Deg()

        if self.Lchild is not None and self.Rchild is not None:
            return self.Lchild.Count_1Deg() + self.Rchild.Count_1Deg()


    def Count_2Deg(self):
        if self is None:
            return 0

        if self.Lchild is not None and self.Rchild is not None:
            return 1 + self.Lchild.Count_2Deg() + self.Rchild.Count_2Deg()

        if self.Lchild is not None and self.Rchild is None:
            return self.Lchild.Count_2Deg()

        if self.Rchild is not None and self.Lchild is None:
            return self.Rchild.Count_2Deg()

        return 0

    
    def height(self):
        if self is None:
            return 0

        left_h = self.Lchild.height() if self.Lchild else 0
        right_h = self.Rchild.height() if self.Rchild else 0

        if left_h > right_h:
            return left_h + 1
        else:
            return right_h + 1


    def pre(self):
        if self is None:
            return
        print(self.Data, end=" ")
        if self.Lchild:
            self.Lchild.pre()
        if self.Rchild:
            self.Rchild.pre()

    
    def post(self):
        if self is None:
            return
        if self.Lchild:
            self.Lchild.post()
        if self.Rchild:
            self.Rchild.post()
        print(self.Data, end=" ")

    
    def search(self, target):
        if self.Data == target:
            return True

        if self.Lchild and self.Lchild.search(target):
            return True

        if self.Rchild and self.Rchild.search(target):
            return True

        return False

    
    def max_Tree(self):
        max_val = self.Data

        if self.Lchild:
            left_max = self.Lchild.max_Tree()
            if left_max > max_val:
                max_val = left_max

        if self.Rchild:
            right_max = self.Rchild.max_Tree()
            if right_max > max_val:
                max_val = right_max

        return max_val

    
    def min_Tree(self):
        min_val = self.Data

        if self.Lchild:
            left_min = self.Lchild.min_Tree()
            if left_min < min_val:
                min_val = left_min

        if self.Rchild:
            right_min = self.Rchild.min_Tree()
            if right_min < min_val:
                min_val = right_min

        return min_val

    
    def sum_Tree(self):
        total = self.Data

        if self.Lchild:
            total += self.Lchild.sum_Tree()

        if self.Rchild:
            total += self.Rchild.sum_Tree()

        return total

    
    
    def count(self):
        total = 1

        if self.Lchild:
            total += self.Lchild.count()

        if self.Rchild:
            total += self.Rchild.count()

        return total

r = Tree_Node(10)
r.Lchild = Tree_Node(5)
r.Rchild = Tree_Node(20)
r.Lchild.Lchild = Tree_Node(3)
r.Lchild.Rchild = Tree_Node(7)

print(r.Count_2Deg())
print(r.height())
print(r.sum_Tree())
r.pre()
        
        
