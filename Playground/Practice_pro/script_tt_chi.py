# Import libraries
import pandas as pd
import numpy as np

# Load datasets
lifespans = pd.read_csv('familiar_lifespan.csv')
iron = pd.read_csv('familiar_iron.csv')
print(lifespans.head(),'\n')

# Tasks: Part One
vein_pack_lifespans = lifespans.lifespan[lifespans.pack == 'vein']
print(f'The mean lifespan in Vein Pack subscr. group: {round(np.mean(vein_pack_lifespans))}')

from scipy.stats import ttest_1samp
sig_thres = 0.05
t_stat, pval = ttest_1samp(vein_pack_lifespans, 73)
print(f'Pval: {pval}\n')
if pval < sig_thres:
  print(f'''It is lower than the significance threshold meaning the Null Hypothesis is rejected and there is a significance difference between the means of the sample and the population.\n''')

# Tasks: Part Two
artery_pack_lifespans = lifespans.lifespan[lifespans.pack == 'artery']
print(f'The mean lifespan in Artery Pack subscr. group: {round(np.mean(artery_pack_lifespans))}')


from scipy.stats import ttest_ind

t_stat_2t, pval_2t = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
print(f'Pval {pval_2t}\n')

if pval_2t < sig_thres:
  print(f'''It is lower than the significance threshold meaning the Null Hypothesis is rejected. There is significant difference between the means of the 2 groups''')
else:
  print(f'''It is higher than the significance threshold meaning the Null Hypothesis is accepted. There is no significant difference between the means of the 2 groups.\n''')
print(iron.head(),'\n')
from scipy.stats import chi2_contingency
Xtab = pd.crosstab(iron.pack, iron.iron)
print(Xtab,'\n')
stat, pval_ch, dof, expected = chi2_contingency(Xtab)
print(f'Pval: {pval_ch}\n')
if pval_ch < sig_thres:
  print(f'''It is lower than the significance threshold meaning the Null Hypothesis is rejected. There is significant difference between the the variables.''')
else:
  print(f'''It is higher than the significance threshold meaning the Null Hypothesis is accepted. There is no significant difference between the variables.\n''')

