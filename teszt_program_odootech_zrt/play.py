# Exercise 2
def adder(a, b):
    return a + b

print(f'''First tests:
{adder(10, 20)}
{adder('apple', 'lemon')}
{adder([10, 20, 30],[40, 50, 60])}''')

# Exercise 3
def adder_new(L):
    first, *rest = L
    return first + adder_new(rest) if rest else first

fruits = ['orange', 'pineapple', 'lemon', 'carrot']
nums = list(range(-50, 50, 15))
alphabet = {chr(i): i-96 for i in range(97, 97+26)}
feats = dict.fromkeys(['name', 'age', 'sex'], 0)
empty = []
mixed = ['orange', 5]
Ls = [10, 20, 30], [20, 30, 40, 50]

for test in [fruits, nums, alphabet, feats, empty, mixed, Ls]:
    if test:
        try: print(adder_new(test), '->', type(adder_new(test)))
        except TypeError: print('TypeError')
def someargs(*args):
    total = args[0]
    for next in args[1:]:
        total += next
    return total

print('Args add: ', someargs(1, 2, 3, 4), someargs('apple', 'lemon'))
print(someargs([1, 2, 3], [5, 10], [30, 40, 10, 10, 40]), someargs(feats))
        
# Exercise 4/1
def adder_defs(good=10, bad=20, ugly=30):
    return good + bad + ugly

zero, one = adder_defs(), adder_defs(20)
two, three = adder_defs(20, 30), adder_defs(20, 30, 50)

print(zero, one, two, three)

# Exercise 4/2
def new_add(**args):
    argkeys = list(args.keys())
    total = args[argkeys[0]]
    for key in argkeys[1:]:
        total += args[key]
    return total, args

print(new_add(a=1, b=2, c=3))

# Exercise 5

def CopyDict(old_dict):
    new_dict = {key: old_dict[key] for key in old_dict}
    return new_dict

print(CopyDict(feats))

def CopyDictAlter(old_dict):
    keys = list(old_dict.keys())[:]
    new_dict = {key:old_dict[key] for key in keys}
    return new_dict

print(CopyDictAlter(feats))
print(CopyDictAlter(alphabet))


# Exercise 6
def addDict(one, two):
    D = {key:one[key] for key in one} | {key: two[key] if key not in one else [one[key], two[key]] for key in two}
    return D

print(addDict({'a':1, 'b':2, 'c':3}, {'a':2, 'd':4}))

# Exercise 7
def f1(a, b): return a, b
print(f1(1, 2))
print(f1(b=2, a=1))

def f2(a, *b): return a, b
print(f2(1, 2, 3))

def f3(a, **b): return a, b
print(f3(1, x=2, y=3))

def f4(a, *b, **c): return a, b, c
print(f4(1, 2, 3, x=2, y=3))

def f5(a, b=2, c=3): return a, b, c
print(f5(1, 4))

def f6(a, b=2, *c): return a, b, c
print(f6(1, 4, 5, 6))

y = 15.0
x = y // 2 
while x > 1:
    if y % x == 0:
        print(y, 'has factor', x)
        break # Skip else
    x -= 1
else: # Normal exit
    print(y, 'is prime')

def forLoop(L = None):  # sourcery skip: list-comprehension
    if L is None: L = [2, 4, 9, 16, 25]
    new_L = []
    for value in L:
        new_L.append(value**.5)
    return new_L
print(forLoop())
print(forLoop([400, 100, 64, 36]))

def mapCall(L = None):
    if L is None: L = [2, 4, 9, 16, 25]
    return list(map(pow, L, [.5]*len(L)))

print(mapCall())
print(mapCall([400, 100, 64, 36]))


def ListCompr(L = None):
    if L is None: L = [2, 4, 9, 16, 25]
    return [value**.5 for value in L]

print(ListCompr())
print(ListCompr([400, 100, 64, 36]))

import math

f = lambda x: math.sqrt(x)
new_L = map(f, [2, 4, 9, 16, 25])

print(next(new_L))
print(next(new_L))
print(next(new_L))

from runtime import timer, best

for test in [forLoop, ListCompr, mapCall]:
    one, two = timer(test)
    three, four = best(test)
    print('--'*33)
    print(f'Time\n{test.__name__} => {one} => {two}')
    print(f'Best time\n{test.__name__} => {three} => {four}')        