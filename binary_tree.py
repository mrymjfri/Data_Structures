class Tree_Node:
    def __init__(self, x):
        self.Data = x
        self.Lchild = None
        self.Rchild = None

    #شمارش برگ های درخت باینری
    def Count_leaves(root):
        if root is None:
            return 0

        if root.Lchild is None and root.Rchild is None:
            return 1

        return Count_leaves (root.Lchild)+Count_leaves(root.Rchild)
    
# شمارش گره های درجه یک در درخت باینری 
    
    def Count_1Deg(root):
        if root is None:
            return 0

        if root.Lchild is not None and root.Rchild is None:
            return 1 + Count_1Deg(root.Lchild)

        if root.Rchild is not None and root.Lchild is None:
            return 1 + Count_1Deg(root.Rchild)

        if self.Lchild is not None and self.Rchild is not None:
            return Count_1Deg(root.Lchild) + Count_1Deg(root.Rchild)

#شمارش  گره های درجه دو در درخت باینری
    def Count_2Deg(root):
        if root is None:
            return 0

        if root.Lchild is not None and root.Rchild is not None:
            return 1 + Count_2Deg(root.Lchild) + Count_2Deg(root.Rchild)

        if root.Lchild is not None and root.Rchild is None:
            return Count_2Deg(root.Lchild)

        if root.Rchild is not None and root.Lchild is None:
            return Count_2Deg(root.Rchild)


    #محاسبه ارتفاع یک درخت باینری
    def height(root):
        if root is None:
            return 0
        return 1+ max(height(root.Lchild),height(root.Rchild))
        


    def pre(root):
        if root is None:
            return
        print(root.Data)
        pre(root.Lchild)
        pre(root.Rchild)

    
    def post(root):
        if root is None:
            return
        post(root.Lchild)
        post(root.Rchild)
        print(root.Data)

    #جست و جوی مقدار یک تارگت
    def search(root, target):
        if root is None :
            return False

        if root.Data==target:
            return target 
        return search (root.Lchild) or search (root.Rchild) 

    #مقدار حداکثر یک درخت
    def max_Tree(root):
        if root is None:
            return float ("-inf")
        return max(max_Tree(root.Lchild) , max_Tree(root.Rchild) , root.Data)
    
    #مقدار حداقل یک دخت
    def min_Tree(root):
        if root is None:
            return float ("+inf")
        return min(min_Tree(root.Lchild) , min_Tree(root.Rchild) , root.Data)

    #حاصل جمع همه‌ی داده های یک درخت
    def sum_Tree(root):
        if root is None:
        return 0
    if root.Lchild is not None and root.Rchild is None:
        return sum_Tree(root.Lchild) + root.Data
    if root.Rchild is not None and root.Lchild is None:
        return sum_Tree(root.Rchild) + root.Data
    return sum_Tree(root.Lchild) + sum_Tree(root.Rchild) + root.Data

    
    #تعداد نود های یک درخت باینری
    def count(root):
        if root is None:
            return 0

        return count(root.Lchild)+count(root.Rchild)+1

r = Tree_Node(10)
r.Lchild = Tree_Node(5)
r.Rchild = Tree_Node(20)
r.Lchild.Lchild = Tree_Node(3)
r.Lchild.Rchild = Tree_Node(7)

print(r.Count_2Deg())
print(r.height())
print(r.sum_Tree())
r.pre()
        
        
