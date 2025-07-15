!pip install numpy
import numpy as np
##1
import numpy as np


original_list = [12.23, 13.32, 100, 36.32]


array = np.array(original_list)


print("Original List:", original_list)
print("One-dimensional NumPy array:", array)

##2
import numpy as np

matrix = np.arange(2, 11).reshape(3, 3)

print(matrix)

##3
import numpy as np

vector = np.zeros(10)
print("Original vector:")
print(vector)


vector[6] = 11
print("\nUpdated vector:")
print(vector)

##4
import numpy as np

array = np.arange(12, 38)

print(array)

##5
import numpy as np

original_array = np.array([1, 2, 3, 4])
print("Original array:", original_array)


float_array = original_array.astype(float)
print("Array converted to float:", float_array)

##6
import numpy as np

centigrade = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])


fahrenheit = centigrade * 9/5 + 32

original_fahrenheit = np.array([0, 12, 45.21, 34, 99.91, 32.])

print("Values in Fahrenheit degrees (original sample):", original_fahrenheit)
print("Values in Centigrade degrees:", centigrade)
print("Values in Fahrenheit degrees (converted):", np.round(fahrenheit, 2))

##7
import numpy as np

original_array = np.array([10, 20, 30])
print("Original array:", original_array)

values_to_append = [40, 50, 60, 70, 80, 90]


new_array = np.append(original_array, values_to_append)

print("After append values to the end of the array:", new_array)

##8
import numpy as np

random_array = np.random.rand(10)

print("Random array:", random_array)

mean = np.mean(random_array)
median = np.median(random_array)
std_dev = np.std(random_array)

print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)

##9
import numpy as np


array_10x10 = np.random.rand(10, 10)

print("10x10 Random Array:\n", array_10x10)

min_value = np.min(array_10x10)
max_value = np.max(array_10x10)

print("\nMinimum value:", min_value)
print("Maximum value:", max_value)

##10
import numpy as np

array_3x3x3 = np.random.rand(3, 3, 3)

print("3x3x3 Random Array:\n", array_3x3x3)


