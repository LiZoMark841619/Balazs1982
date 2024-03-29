class Adder:
  
    def __init__(self, start=None):
        if start is None:
            start = []
        self.data = start
        
    def __add__(self, other):
        return self.add(other)
    
    def add(self, y):
        print('Not implemented')
        
class ListAdder(Adder):
    def add(self, y):
        return self.data + y

class DictAdder(Adder):
    def add(self, y):
        return {k:self.data[k] for k in self.data} | {k:y[k] for k in y}

if __name__ == '__main__':
    Adder(10).add(20)
    Adder('Hallo') + 'Balazs'
    print(ListAdder([1]).add([2]))
    print(ListAdder([1]) + [2])
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
    
class MyList:
    def __init__(self, start):
        self.wrapped = []
        for x in start: self.wrapped.append(x)
        
    def __add__(self, other):
        return MyList(self.wrapped + other)
    
    def __mul__(self, time):
        return MyList(self.wrapped * time)
    
    def __getitem__(self, offset):
        return self.wrapped[offset]
    
    def __len__(self):
        return len(self.wrapped)
    
    def __getslice__(self, low, high):
        return MyList(self.wrapped[low:high])
    
    def append(self, node):
        self.wrapped.append(node)
        
    def __getattr__(self, name):
        return getattr(self.wrapped, name)
    
    def __repr__(self):
        return repr(self.wrapped)
    
if __name__ == '__main__':
    x = MyList('spam')
    print(x)
    print(x[2])
    print(x[1:])
    print(x + ['eggs'])
    print(x * 3)
    x.append('a')
    x.sort()
    for c in x: print(c, end=' ')
    
class MySubList(MyList):
    calls = 0
    
    def __init__(self, start):
        self.counts = 0
        MyList.__init__(self, start)
    
    def __add__(self, other):
        MySubList.calls += 1
        self.counts += 1
        return MyList.__add__(self, other)

    def stats(self):
        return self.calls, self.counts
    
if __name__ == '__main__':
    x = MySubList('spam')
    y = MySubList('foo')
    print(x[2])
    print(x[1:])
    print(x + ['eggs'])
    print(x + ['toast'])
    print(y + ['bar'])

