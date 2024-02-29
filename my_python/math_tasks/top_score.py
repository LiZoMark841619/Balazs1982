def top_score(arr: list=None, top_score: int=None) -> list:
    if not arr or not top_score:
        raise ValueError('Only valid list and top_score are accepted!')
    arr.sort()
    res = [val for val in arr if val <= top_score]; res.reverse()
    return res

if __name__ == '__main__':
    length = int(input('Enter the length of the list: '))
    L = map(int, [input(f'Number {i} value: ') for i in range(length)])
    top = int(input('Enter a number which is the maximum of the list: '))
    print(top_score(list(L), top))
    
import random
def getX(arr: list=None, num: int=None) -> list:
    if not arr or not num:
        raise ValueError('Only valid list and top_score are accepted!')
    elif num > len(arr):
        raise IndexError('The required top score is out of range!')
    arr.sort()
    return arr[num-1]

if __name__ == '__main__':
    L = [random.choice(list(range(-100, 100, 10))) for _ in range(10)]
    num = int(input('Please enter a number: '))
    print(getX(L, num))