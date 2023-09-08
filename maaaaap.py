
def mapp(func,*iterable):
    min = len(iterable[0])
    for i in range(1,len(iterable)):
        if min>len(iterable[i]):
            min = len (iterable[i])

    for i in range(min):
        yield func(*(x[i] for x in iterable))

def foo(a,b):
    return a+b

x = mapp(foo,[1,2,3],[4, 5])
print(next(x))
print(next(x))
