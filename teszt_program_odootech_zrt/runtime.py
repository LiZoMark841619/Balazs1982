import time
repslist = range(1000)
def timer(func, *pargs, **kargs):
    start = time.time()
    for _ in repslist:
        ret = func(*pargs, **kargs)
    elapsed = time.time() - start
    return (elapsed, ret)