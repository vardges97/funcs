def reduce(func,seq):
    x = func(seq[0],seq[1])
    for i in range(1,len(seq)-1):
        yield func(x,seq[i+1])

x = reduce(lambda x,y: x*y,[4,5,6])

print(next(x))
