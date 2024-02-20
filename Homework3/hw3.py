# imports
import numpy as np
import csv
from matplotlib import pyplot as plt

# load the data
data = []
csvfile = open('NFL2023Season.csv')
readCSV = csv.reader(csvfile,delimiter = ',')

next(readCSV)

for inputline in readCSV:
    data.append(inputline)

# put the data into arrays
wins = []
ties = []
loses = []
percents = []
ptsFor = []
ptsAgainst = []
netPts = []

team = [x[0] for x in data]
for x in data:
    wins.append(int(x[1]))
    ties.append(int(x[2]))
    loses.append(int(x[3]))
    percents.append(float(x[4]))
    ptsFor.append(int(x[5]))
    ptsAgainst.append(int(x[6]))
    netPts.append(int(x[7]))

# 1) print the formatted data
print('\n\n1) Formatted Columns:')
for i, win in enumerate(wins):
    print(team[i], win, ties[i], loses[i], "{:.2f}".format(percents[i]), ptsFor[i], ptsAgainst[i], netPts[i])

percentsArray = np.array(percents)

# 2) Winning Percentage

print('\n\n2) Winning Percentage:')
print('The Maximum is', np.max(percents))
print('The Minimum is', np.min(percents))
print('The Mean (arithmetic) is', np.mean(percents))
print('The Median is', np.median(percents))
print('The Range is', np.ptp(percents))
print('The Standard Deviation is', np.std(percents))
print('Variance is', np.var(percents))

# 3) Points Against

print('\n\n3) Points Against:')
print('The Maximum is', np.max(ptsAgainst))
print('The Minimum is', np.min(ptsAgainst))
print('The Mean (arithmetic) is', np.mean(ptsAgainst))
print('The Median is', np.median(ptsAgainst))
print('The Range is', np.ptp(ptsAgainst))
print('The Standard Deviation is', np.std(ptsAgainst))
print('Variance is', np.var(ptsAgainst))

# 4) Wins Histogram
# hist, bins = np.histogram(wins, bins=16) I like how it shows the distribution across all possibilities
hist, bins = np.histogram(wins, bins=10)
fig = plt.figure(figsize=(10,7))
plt.hist(wins, bins)
plt.title('NFL Wins Distribution')
plt.show()
