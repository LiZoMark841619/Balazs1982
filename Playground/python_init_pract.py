import random
import time
start = time.time()

class Stats:
    
    def __init__(self, list):
        self.list = list
        
    def min(self):
        a = sorted(self.list)
        return a[0]
    
    def max(self):
        a = sorted(self.list)
        return a[-1]
        
    def median(self):
        a = self.list
        if len(a) % 2 == 0:
            return int(a[len(a) // 2] + a[len(a) //2 - 1]) / 2
        else:
            return int(a[len(a) // 2])
         
    def mean(self):
        a = sum(self.list)
        b = len(self.list)
        return int(a / b)

#list_2 = Stats([100, 90, 150, 250, 200])
#print(list_2.median())
#print(list_2.min(), list_2.max(), list_2.mean())

rand_iter = int(input('Please enter the size of a list which will generate random numbers and make some stats of that:'))
rand_10_num_list = [random.randint(0, 2000) for _ in range(rand_iter)]
class_rand = Stats(rand_10_num_list)

print(f'''\nThe list including {rand_iter} random elements is below: {rand_10_num_list}
Some basic stats of the provided data are here as follows:

- min: {class_rand.min()}
- max: {class_rand.max()}
- median: {class_rand.median()}
- mean: {class_rand.mean()}\n''')

end = time.time()

print(f'The program ran in {end - start} seconds')
print(help(Stats))