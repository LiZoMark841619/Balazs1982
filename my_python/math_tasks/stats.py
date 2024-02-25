def mean(L: list) -> float:
    return round(sum(L)/len(L), 2)

if __name__=='__main__':
    length = int(input('Enter the length of the list: '))
    L = [float(input('Enter the numbers of that collection: ')) for _ in range(length)]
    print(mean(L))
    
def median(L: list) -> float:
    L.sort()
    return L[len(L)//2] if len(L) % 2 != 0 else (L[len(L)//2] + L[len(L)//2 - 1]) / 2

if __name__=='__main__':
    length = int(input('Enter the length of the list: '))
    L = [float(input('Enter the numbers of that collection: ')) for _ in range(length)]
    print(mean(L))

def mode(L):
    L = [val for val in L if val]
    L = sorted(L)
    D = {key:L.count(key) for key in L}
    max_val = 0
    key = 0
    for k in D:
        if D[k] > max_val:
            max_val = D[k]
            key = k
    return key
        
if __name__=='__main__':
    test_1 = input('Please enter your name: ').strip().split()
    print(mode(test_1))
    test_2 = int(input('Enter the length of the list: '))
    L = [float(input('Enter the numbers of that collection: ')) for _ in range(test_2)]
    print(mode(L))

    
def std(L):
    pass
    
    