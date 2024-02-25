def top_score(arr: list, top_score: int) -> list:
    arr.sort()
    res = [val for val in arr if val <= top_score]; res.reverse()
    return res

if __name__ == '__main__':
    length = int(input('Enter the length of the list: '))
    L = map(int, [input(f'Number {i} value: ') for i in range(length)])
    top = int(input('Enter a number which is the maximum of the list: '))
    print(top_score(list(L), top))
    
import random
def getX(arr: list, num: int) -> list:
    arr.sort()
    return 0 if num > len(arr) or not arr else arr[num-1]

if __name__ == '__main__':
    L = [random.choice(list(range(-100, 100, 10))) for _ in range(10)]
    num = int(input('Please enter a number: '))
    print(getX(L, num))