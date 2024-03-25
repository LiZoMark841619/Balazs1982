class Adder:
    
    def add(self, y):
        print('Not implemented')
        
    def __init__(self, start=[]):
        self.data = start
        
    def __add__(self, other):
        return self.add(other)
        
class ListAdder(Adder):
    def add(self, y):
        return self.data + y

class DictAdder(Adder):
    def add(self, y):
        return {k:self.data[k] for k in self.data} | {k:y[k] for k in y}

class Mylist:
    pass
    
if __name__ == '__main__':
    Adder(10).add(20)
    Adder('Hallo') + 'Balazs'
    print(ListAdder([1]).add([2]))
    print(ListAdder(1).add(2))
    print(ListAdder('Hey').add('Balazs'))
    x = DictAdder({'start':0})
    z = x + {'end':100}
    print(z)
    print(x.add({'new_end':50}))
    D = DictAdder({0:'start'})
    E = D + {i-96:chr(i) for i in range(97, 97+26)}
    F = DictAdder(E) + {27:'end'}
    print(F)