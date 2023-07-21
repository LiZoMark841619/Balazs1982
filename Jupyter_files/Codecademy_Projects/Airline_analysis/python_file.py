import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.api as sm
import matplotlib.pyplot as plt
import math
import codecademylib3

flight = pd.read_csv("flight.csv")

print(f'The average coach price is ${round(np.mean(flight.coach_price))}.')
print(f'The minimum coach price is ${round(np.min(flight.coach_price))}.')
print(f'The maximum coach price is ${round(np.max(flight.coach_price))}.')
print(f'''\nThe $500 coach ticket is in the upper 2% of the coach tickets,
so this is relatively far from the interquartile range, which is between
these two values: {np.percentile(flight.coach_price, [25,75])}. 
The upper 2% range is between these two numbers {np.percentile(flight.coach_price, [98,100])}''')

flight['coach_price_long'] = flight.coach_price[flight.hours == 8]
flight.reset_index()

sns.displot(flight.coach_price_long, kde=True, color='darkgreen')
plt.title('Distribution of "coach prices" in 8 hour-long flights', fontsize=10)
plt.xlabel('Coach prices ($)', fontsize=9)
plt.ylabel('Count (number of flights)', fontsize=9)
plt.show()
plt.clf()

sns.boxplot(x='coach_price_long', data=flight, color='darkgreen')
plt.title('Boxplot of "coach prices" in 8 hour-long flights', fontsize=10)
plt.xlabel('Coach prices ($)', fontsize=9)
plt.show()
plt.clf()

print('The $500 ticket price is more reasonable in a 8 hour-long flight.')
#print(flight.delay.unique())

big_delayes = flight.delay[flight.delay > 60]
sns.histplot(big_delayes, kde=True, bins=11, color='darkred')
plt.title('Distribution of "relevant delays" (more than one hour)', fontsize=10)
plt.xlabel('Minutes of delays', fontsize=9)
plt.ylabel('Count (number of delays)', fontsize=9)
plt.text(x= 1500, y= 25, s=f'''The number of delays in range of \n {np.min(big_delayes)} and {np.max(big_delayes)} minutes is {len(big_delayes)}
 out of the total {len(flight.delay):,} flights''', fontsize=8, color='darkred')
plt.show()
plt.clf()

print('''The scatterplot shows not just that higher coach prices have higher firstclass prices, which means there is a strong 
correlation between them, but it is 100% sure, that flying in firstclass on weekdays is much cheaper than at weekends.''')

sns.boxplot(x='inflight_meal', y='coach_price', data=flight, palette='pastel')
plt.title(f'Relationship between inflight meal and coach price', fontsize=10)
plt.show()
plt.clf()

sns.boxplot(x='inflight_entertainment', y='coach_price', data=flight, palette='pastel')
plt.title(f'Relationship between inflight entertainment and coach price', fontsize=10)
plt.show()
plt.clf()

sns.boxplot(x='inflight_wifi', y='coach_price', data=flight, palette='pastel')
plt.title(f'Relationship between inflight_wifi and coach price', fontsize=10)
plt.show()
plt.clf()

print('Meal does not have much effect on coach prices, but wifi has little and entertainment is the most influential among them.')

sns.set_palette("Spectral")
sns.barplot(x='hours', y='passengers', data=flight)
plt.title('Number of passengers depending on flight hours', fontsize=10)
plt.xlabel('Flight hours', fontsize=9)
plt.ylabel('Number of passengers', fontsize=9)
plt.show()
plt.clf()

model = sm.OLS.from_formula('firstclass_price ~ coach_price', data=flight).fit()
pred_400 = model.params[0] + model.params[1]*400
#print(model.params)
#print(pred_400)
a = 700
data = {'coach_price':[a]}
pred_700 = model.predict(data)
print(f'If the coach price will exceed the ${a}, the predicted firstclass price will reach ${int(round(pred_700[0], 3))}.')
fitted_values = model.predict(flight)
residuals = flight.firstclass_price - fitted_values

sns.scatterplot(fitted_values, residuals, color='darkblue')
plt.title('Scatter plot of fitted values and residuals of firstclass prices', fontsize=10)
plt.xlabel('Fitted_values of firstclass prices', fontsize=9)
plt.ylabel('Residuals', fontsize=9)
plt.axhline(0, color='black')
plt.show()
plt.clf()

sns.lmplot(x='coach_price', y='firstclass_price', data=flight, hue='weekend', fit_reg=False)
plt.title('Relationship between coach and firstclass prices colored by weekend', fontsize=10)
plt.xlabel('Coach prices ($)', fontsize=9)
plt.ylabel('Firstclass prices ($)', fontsize=9)
plt.show()
plt.clf()

plt.figure(figsize=[6,6])
sns.boxplot(x='day_of_week', y='coach_price', data=flight, order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], hue='redeye')
plt.title('Relationship between days and coach price colored by "redeye"', fontsize=10)
plt.xticks(rotation=30)
plt.show()
plt.clf()
