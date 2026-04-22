import numpy as np
import skfuzzy as fuzz

x = np.arange(0, 11, 1)

low = fuzz.trimf(x, [0, 0, 5])
medium = fuzz.trimf(x, [0, 5, 10])
high = fuzz.trimf(x, [5, 10, 10])

value = 7

low_val = fuzz.interp_membership(x, low, value)
med_val = fuzz.interp_membership(x, medium, value)
high_val = fuzz.interp_membership(x, high, value)

print("Low:", low_val)
print("Medium:", med_val)
print("High:", high_val)