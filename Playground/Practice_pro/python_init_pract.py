import random
import time
from datetime import datetime
start = time.time()

class Stats:
    
    def __init__(self, list) -> None:
        self.list = sorted(list)
        
    def min(self) -> int:
        return self.list[0]
    
    def max(self) -> int:
        return self.list[-1]
        
    def median(self) -> float:
        a = self.list
        if len(a) % 2 == 0:
            return int(a[len(a) // 2] + a[len(a) //2 - 1]) / 2
        else:
            return int(a[len(a) // 2])

    def mean(self) -> float:
        return sum(self.list) // len(self.list)
    
    def mode(self) -> int:
        modes = {num:self.list.count(num) for num in self.list}
        max_value = 0
        max_key = 0
        for key, value in modes.items():
            if value > max_value:
                max_value = value
                max_key = key
        return max_key, max_value
    
    def var(self) -> int:
        return sum((self.mean() - num)**2 for num in self.list)
    
    def std(self) -> float:
        return self.var()**.5
        
rand_iter = int(input('Please enter the size of a list which will generate random numbers and make some stats of that:'))
rand_num_list1 = [random.choice([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) for _ in range(rand_iter)]
rand_num_list2 = [random.randrange(100, 2000, 100) for _ in range(rand_iter)]
rand_num_list3 = [random.randint(1, 10000) for _ in range(rand_iter)]

class_rand = Stats(rand_num_list1)

print(f'''\nThe list including {len(class_rand.list)} random elements is below: {class_rand.list}
Some basic stats of the provided data are here as follows:

- min: {class_rand.min()}
- max: {class_rand.max()}
- median: {class_rand.median()}
- mean: {int(class_rand.mean())}
- mode: {class_rand.mode()[0]}
- freq (occurences of mode): {class_rand.mode()[1]}
- variance: {class_rand.var()}
- standard deviation: {class_rand.std()}\n''')

end = time.time()

print(f'The program ran in {end - start} seconds, in {datetime.now()}')
#print(help(Stats))





