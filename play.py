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

print('Args add: ', someargs(1, 2, 3, 4), someargs('apple', 'lemon'), someargs([1, 2, 3], [5, 10], [30, 40, 10, 10, 40]), someargs(feats))
        
# Exercise 4/1
def adder_defs(good=10, bad=20, ugly=30):
    return good + bad + ugly

zero = adder_defs()
one = adder_defs(20)
two = adder_defs(20, 30)
three = adder_defs(20, 30, 50)

print(zero, one, two, three)
print(adder_defs(ugly=1, bad=1))

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
    return new_dict, old_dict

print(CopyDict(feats))

def CopyDictAlter(old_dict):
    keys = list(old_dict.keys())[:]
    new_dict = {key:old_dict[key] for key in keys}
    return new_dict

print(CopyDictAlter(feats))
print(CopyDictAlter(alphabet))


# Exercise 6
import random
def addDict(one, two):
    D = {key:one[key] for key in one} | {key: two[key] if key not in one else random.choice([one[key], two[key]]) for key in two}
    return D

print(addDict({'a':1, 'b':2, 'c':3}, {'a':2, 'd':4}))
print(random.choice([feats['age'], feats['sex']]))