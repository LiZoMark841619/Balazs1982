import timeit
repslist = range(1000)
def timer(func, *pargs, **kargs):
    start = timeit.timeit()
    for _ in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timeit.timeit() - start
    return (elapsed, ret)