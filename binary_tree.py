class Tree_Node :
    def __init__(self , x):
        self.Data = x
        self.Lchild = None
        self.Rchild = None
#تابع بازگشتی بنویسید که تعداد برگ های درخت باینری روت را محاسبه کند
    def Count_leaves(root):
        if root is None:
            return 0
        if root.Lchild is None and root.Rchild is None:
            return 1
        return Count_leaves(root.Lchild) + Count_leaves(root.Rchild)

#تابع بازگشتی بنویسید که گره های درجه یک ، درخت باینری را محاسبه کند
    def Count_1Deg(root):
        if root is None:
            return 0
        if root.Lchild is None and root.Rchild is not None:
            return 1+Count_1Deg(root.Rchild)
        if root.Rchild None and root.Lchild is not None:
            return 1+Count_1Deg(root.Lchild)
        return Count_1Deg(root.Lchild) + Count_1Deg(root.Rchild)   

    def Count_2Deg (root):
        if root is None :
            return 0
        if root.Lchild is None and root.Rchild is not None:
            return Count_2Deg (root.Rchild)
        if root.Rchild  is None and root.Lchild is not None:
            return Count_2Deg(root.Lchild)
        return Count_2Deg(root.Lchild) + Count_2Deg(root.Rchild)


    def height (root):
        if root is None:
            return 0
        return 1+max(height (root.Rchild), height (root.Lchild))

    def pre(root):
        if root is None:
            return[ ]
        return print((root.Data)pre,(root.Lchild),pre(root.Rchild))       

    def post(root):
        if root is None:
            return[ ]
        return print(post(root.Lchild),post(root.Rchild),(root.Data))    

#تابعی بازگشتی بنویسید که مقدار تارگت را در یک درخت جستجو کند
    def search(root , t):
        if root is None:
            return False
        if root.Data == target:
            return True
        return search(root.Lchild) or search(root.Rchild)      

#تابعی بازگشتی بنویسید که مقدار حداکثر یک درخت را بازگرداند
    def max_Tree(root):
        if root is None:
            return float("-lnf")
        return max(max_Tree(data.Lchild) , max_t(data.Rchild) , root.data)
    


    def min_Tree(root):
        if root is None:
            return float("+lnf")
        return min(min_Tree(data.Lchild) , min_t(data.Rchild) , root.data)
    
#تابعی بازگشتی بنویسید که حاصل جمع تمامی داده های یک درخت دودویی را بازگرداند
    def sum_Tree(root):
        if root is None:
            return 0
        if root.Lchild is None and root.Rchild is not None:
            return sum_Tree(root.Rchild) + root.Data
        if root.Rchild is None and root.Lchild is not None:
            return sum_Tree(root.Lchild) + root.Data
        return sum_Tree(root.Lchild) + sum_Tree(root.Rchild) + root.Data


#تابعی بازگشتی بنوبسید که تعداد نود های یک درخت باینری را بازگرداند

    def count(root):
        if root is None:
            return 0
        return count(root.Lchild) + count(root.Rchild)+1
