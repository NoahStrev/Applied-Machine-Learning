# Load the cs data into a numpy array and then do some states

import numpy as np
import csv

data = []
csvfile = open('csemploydata.csv')
readCSV = csv.reader(csvfile,delimiter = ',')

next(readCSV) # will also skip header row

for inputline in readCSV:
    data.append(inputline)

# HAVE A PROBLEM READING CSV FOR NUMPY
# SOME OF THE DATA IS TEXT
# AND SO THE DATA MAY POSSIBLY ALL BE READ IN AS STRING DATA

ranks = []
salaries = []
numberPositions = []

for x in data:
    ranks.append(int(x[0]))
    salaries.append(int(x[1]))
    numberPositions.append(int(x[2]))
jobtitles = [x[3] for x in data]

print(ranks)
print(salaries)
print(numberPositions)
print(jobtitles)

# nice columnar output
for i, rank in enumerate(ranks):
    print(rank, salaries[i], numberPositions[i], jobtitles[i])

# Descriptive stats for for salaries
# Max, Min, Mean, Median, Range, STD, Variance
print('\n\n ********** DESCRIPTIVE STATS **********')
print('Max Salary is', np.max(salaries))

# if error then need npsals = np.array(salaries)
print('Min Salary is', np.min(salaries))
print('Mean Salary is', np.mean(salaries))
print('Median Salary is', np.median(salaries))
print('Range of Salaries is', np.ptp(salaries))
print('Standard Deviation of Salaries is', np.std(salaries))
print('Variance of Salaries is', np.var(salaries))

# HISTOGRAMS

hist, bins = np.histogram(salaries, 4)
from matplotlib import pyplot as plt
fig = plt.figure(figsize = (10,7))
plt.hist(salaries, bins)
plt.title('Salary data')
plt.show()
