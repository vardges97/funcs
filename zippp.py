def zip(*iterab):
    minlen = min(len(item)for item in iterab)
    for i in range(minlen):
        items=tuple(item[i]for item in iterab)
        yield items

x = zip([1,2,3,4],[5,6,7,8])
print(next(x))
print(next(x))