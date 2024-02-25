def missing_nums(arr: list, num: int) -> list:
    arr.sort()
    new_arr = list(range(arr[0], arr[-1]+1))
    if num == len(new_arr) - len(arr):
        return [num for num in new_arr if num not in arr]
    else:
        raise ValueError('K is out of range')
    
if __name__=='__main__':
    L = [1, 2, 3, 4, 8, 10]
    num = 4
    print(missing_nums(L, num))