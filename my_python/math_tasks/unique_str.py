def unique(string: str) -> bool:
    for i in range(len(string)):
        for target in string[i+1:]:
            if string[i] == target:
                return False
    return True

if __name__=='__main__':
    string = input('Please enter a string: ')
    print(f'The bool value of "{string}" has only unique characters is {unique(string)}')