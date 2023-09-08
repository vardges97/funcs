def filt(func,*iter):
    minlen = min(len(item) for item in iter)
    if func == None:
        for i in iter:
            if bool(i)== True:
                yield i

    else:
        for i in range(minlen):
            yield func(*(x[i] for x in iter))



x = filt(lambda x,y: x*y,[1,2,3,4],[2,3,4,5])
print(int(next(x)))
print(int(next(x)))