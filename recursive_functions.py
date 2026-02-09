#fib(n)
1,1,2,3,5,8,13,
#fib(n) = fib(n-1) + fib(n-2)
#shart bazgasht :
#if (n = 1) or (n = 2) :
#meqdar bazgasht :
#1
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1) + fib(n-2)




    for i in range (n):
        for j in range(n):
            for k in range(n):
                c[i,k] = c[i,k] + a[i,j] *b[j.k]


def test(a,b):
    if a>b :
        return a*b
    return test(a , b-2) + test(a-1 , b-3) +6
test(3,7)

جواب:۴۲


تابع بازگشتی بنویسید که دو عدد a,b را که مثبت اند را بر هم تقسیم کند.

def div(a,b):
    if a<b:
        return 
    return div(a-b,b)+1


تابع بازگشتی بنویسید که حاصل ضرب دو عدد مثبت a,b را محاسبه کند.

def mull(a,b):
    if b==0:
        return 0
    return mull(a,b-1)+a
