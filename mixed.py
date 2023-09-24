hairstyles = ['sport', 'casual', 'extra']
prizes = [100, 300, 900]
hairstyles = {hairstyles[i]:prizes[i] for i in range(len(hairstyles))}
new = {key:value for key, value in hairstyles.items() if value < 900}
hairstyles
suits = {'sport':25, 'casual':10, 'elegant':5}
from typing import ChainMap
list(ChainMap(hairstyles, suits))
combined = hairstyles.copy()
combined.update(suits)
list(combined)
x = 0.3508
x.as_integer_ratio()
nominator,denomiator = x.as_integer_ratio()
print(nominator)