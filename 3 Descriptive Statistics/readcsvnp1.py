import numpy as np

# demonstrate what happens when we use numpy to load numeric data with non-numeric data

# load numeric data into a numpy array and then some quick stats

data = np.loadtxt('justnums.csv', delimiter=',', skiprows=1) # skips header

print(data)

# NOW FORMAT
print('\n\nNOW FORMATTED:')
for row in data:
    print(int(row[0]), "{:.2f}".format(row[1]))
# can do data[0][2] to go into the exact values in the rows

IDs = [x[0] for x in data]
GPAs = [x[1] for x in data]

print('\nIDs:', IDs)
print('\nGPAs:', GPAs)

print(type(GPAs))
# list

# in order to use the NumPy methods we need numpy arrays
GPAarray = np.array(GPAs)
print(type(GPAarray))


# NOW WE CAN DO SOME NumPy stats and some plots
print('Maximum GPA is', np.max(GPAarray)) # array
print('Maximum GPA is', np.max(GPAs)) # list


print('Minimum GPA is', np.min(GPAarray))
print('Mean (arithmetic) GPA is', np.mean(GPAarray))
print('Median GPA is', np.median(GPAarray))

# WHY MIGHT YOU WANT TO USE THE np array RATHER THAN A LIST???
# (1) Less Memory Usage
# (2) Less Execution Time

# range is max - min
# which is also Peak-to-Peak

print('\nThe range of values', np.ptp(GPAarray))

print(np.sort(GPAarray))

print('What is the spread of the data? The distribution?')
print('The standard deviation is', np.std(GPAarray))

print('and it is the square root of the variance')
print(np.var(GPAarray))

# Histogram
hist, bins = np.histogram(GPAarray, bins=4)
print('hist', hist)
print('bins', bins)

# What about the grpah?
from matplotlib import pyplot as plt
fig = plt.figure(figsize=(10,7))
plt.hist(GPAarray, bins)
plt.title('GPAs')
plt.show()
