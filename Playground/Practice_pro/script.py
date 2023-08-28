import noshmishmosh
import numpy as np

all_visitors = noshmishmosh.customer_visits
paying_visitors = noshmishmosh.purchasing_customers

total_visitor_count = len(all_visitors)
paying_visitor_count = len(paying_visitors)
baseline_percent = paying_visitor_count / total_visitor_count *100
print(baseline_percent)
payment_history = noshmishmosh.money_spent
average_payment = np.mean(payment_history)
print(average_payment)
new_customer_needed = np.ceil(1240 / average_payment)
print(new_customer_needed)
percentage_point_increase = new_customer_needed / total_visitor_count *100
mde = percentage_point_increase / baseline_percent * 100
print(mde)
sig_thres = 0.1
ab_sample_size = 490