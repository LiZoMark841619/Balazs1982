def fib_def(n: int) -> list:
    fib_list = [0, 1]
    fib_list.extend(fib_list[i] + fib_list[i+1] for i in range(n-2))
    return fib_list

if __name__ == '__main__':
    request = int(input('Please enter the length of the fibonacci list: '))
    print('The list is below:',fib_def(request))
    
def fib_mod(n: int, fib_list: list) -> list:
    fib_list.extend(fib_list[i]+fib_list[i+1] for i in range(n-2))
    return fib_list

if __name__ == '__main__':
    request = int(input('Please enter a different length of the fibonacci list : '))
    L = map(int, [input(f'Enter the number {i+1} initial value of the list: ') for i in range(2)])
    print('The list is below: ',fib_mod(request, list(L)))
    




