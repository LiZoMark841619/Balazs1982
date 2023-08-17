import random
import time
from datetime import datetime
start = time.time()

class Stats:
    
    def __init__(self, list) -> None:
        self.list = sorted(list)
        
    def min(self) -> int:
        a = self.list
        return a[0]
    
    def max(self) -> int:
        a = self.list
        return a[-1]
        
    def median(self) -> float:
        a = self.list
        if len(a) % 2 == 0:
            return int(a[len(a) // 2] + a[len(a) //2 - 1]) / 2
        else:
            return int(a[len(a) // 2])
         
    def mean(self) -> float:
        a = sum(self.list)
        b = len(self.list)
        return a / b
    
    def mode(self) -> int:
        a = self.list
        modes = {num:a.count(num) for num in a}
        max_value = 1
        for key, value in modes.items():
            if value >= max_value:
                max_value = value
        for key, value in modes.items():
            if value == max_value:
                return key, value
    
rand_iter = int(input('Please enter the size of a list which will generate random numbers and make some stats of that:'))
rand_num_list = [random.randint(0, 1000) for _ in range(rand_iter)]
class_rand = Stats(rand_num_list)

print(f'''\nThe list including {rand_iter} random elements is below: {rand_num_list}
Some basic stats of the provided data are here as follows:

- min: {class_rand.min()}
- max: {class_rand.max()}
- median: {class_rand.median()}
- mean: {int(class_rand.mean())}
- mode: {class_rand.mode()[0]}
- freq (occurences of mode): {class_rand.mode()[1]}\n''')

end = time.time()

print(f'The program ran in {end - start} seconds, in {datetime.now()}')
#print(help(Stats))