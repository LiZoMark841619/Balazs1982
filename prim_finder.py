def prim_finder(n):
    prims = []
    for i in range(2, n + 1):
        counter = 0
        for k in range(1, i + 1):
            if i % k == 0:
                counter += 1
        if counter == 2:
            prims.append(i)
    return prims

print(prim_finder(100))
