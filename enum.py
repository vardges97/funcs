def enumerate(arg,start=0):
    for i in range(len(arg)):
        yield(i+start,arg[i])

x = enumerate([1,2,3,4])
print(next(x))
print(next(x))
print(next(x))