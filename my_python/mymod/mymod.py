def countLines(file):
    with open(file, encoding='utf') as F:
        return len(F.readlines())
print(countLines('..\\..\\teszt_program_odootech_zrt\\feladat.txt'))

def countChars(file):
    with open(file, encoding='utf') as F:
        return len(F.read())
print(countChars('..\\..\\teszt_program_odootech_zrt\\feladat.txt'))

def test(file):
    return {'Lines':countLines(file), 'Chars':countChars(file)}
print(test('..\\..\\teszt_program_odootech_zrt\\feladat.txt'))
    

# def countLinesChars(path: str):
#     with open(path, encoding='utf') as F:
#         L = F.readlines()
#         D = {i:len(L[i]) for i in range(len(L))}
#         return path.split('\\')[-1], len(L), D
    
# test = countLinesChars('..\\..\\teszt_program_odootech_zrt\\feladat.txt')
# print(f'The {test[0]} file has {test[1]} lines which contains characters as follows: ')
# for k in test[-1]:
#     print(f'Line number {k+1} has => {test[-1][k]} characters.')
