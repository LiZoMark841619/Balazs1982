def primes(n: int) -> list:
    primes = [i for i in range(2, n+1) if sum(i%k == 0 for k in range(1, i+1)) == 2]
    return primes

if __name__ == '__main__':
    num = int(input('Please enter a number till the primes will be printed out: '))
    print(primes(num))
    
def prime_factors(n: int) -> list:
    primes = [i for i in range(2,n+1) if sum(i%k==0 for k in range(1,i+1)) == 2]
    return [num for num in primes if n%num == 0]

if __name__ == '__main__':
    num = int(input('Please enter a number which prime factors will be printed out: '))
    print(prime_factors(num))

import itertools 

def semi_primes(n: int) -> list:
    primes = [i for i in range(2,n+1) if sum(i%k==0 for k in range(1,i+1)) == 2]
    not_primes = [num for num in range(1,n+1) if num not in primes]
    return [n for (n, i) in itertools.product(not_primes, range(len(primes)))
            for k in range(i, len(primes))
            if n == primes[i]*primes[k]]
    
if __name__ == '__main__':
    num = int(input('Please enter a number till the SEMI-PRIMES will be printed out: '))
    print(semi_primes(num))
