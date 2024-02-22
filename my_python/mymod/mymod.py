def countLines(file):
    with open(file, encoding='utf') as F:
        return len(F.readlines())
    
def countChars(file):
    with open(file, encoding='utf') as F:
        return len(F.read())
    
def test(file):
    return {'Lines':countLines(file), 'Chars':countChars(file)}
if __name__=='__main__': print(test('mymod.py'))
    
def countLinesChars(file):
    with open(file, encoding='utf') as F:
        L = F.readlines()
        return {'file': file.split('\\')[-1], 'Line:chars':{i+1:len(L[i]) for i in range(len(L))}}
if __name__=='__main__': print(countLinesChars('mymod.py'))