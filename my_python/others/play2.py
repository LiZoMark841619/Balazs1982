class Adder:
    
    def add(self, x, y):
        print('Not implemented')
        
    def __init__(self, data=None):
        if data is None:
            data = []
            self.data = data
        
    def __add__(self, y):
        self.add(self.x, y)
        
class ListAdder(Adder):
    def add(self, x, y):
        return x + y

class DictAdder(Adder):
    def add(self, x, y):
        return {k:x[k] for k in x} | {k:y[k] for k in y}

class Mylist:
    pass
    
    

if __name__ == '__main__':
    Adder().add(10, 20)
    Adder() + ['Hallo', 'Balazs']
    print(ListAdder().add([1], [2]))
    print(ListAdder().add(1, 2))
    print(ListAdder().add('Hey', 'Balazs'))
    x = DictAdder()
    print(x.add({1:1}, {2:2}))
