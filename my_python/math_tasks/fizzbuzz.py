def fizzbuzz(n:int) -> list:
    return ['Fizz' if k%3 == 0 and k%5 !=0 else 'Buzz' if k%5 == 0 and k%3 !=0
            else 'FizzBuzz' if k%3 ==0 and k%5 ==0 else k for k in range(1,n+1)]
    
if __name__=='__main__':
    num = int(input('Please enter a number: '))
    print(fizzbuzz(num))