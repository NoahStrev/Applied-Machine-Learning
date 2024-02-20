# CSV stands for Comma Seperated Values
# data must be Joe, Noah, Kyle
# or Joe| Noah| Kyle
# must have something common across the database seperating the values


# CONVERT A TEXT FILE TO CSV
# It could be opened in Excel and Save As .csv
# But this may not work, and sometimes we want a file that merges multiple
# streams so this is a good tool to have

import re
import csv

# Are the data records uniform?? YES
# data record: 1  134230 345893  Principal Software Engineer

pattern = r"(^\d+)\s+(\d+)\s+(\d+)\s+([A-Za-z ]+)"


# OPEN THE TEXT FILE
infile = open('ComputerScienceEmployment.txt')


# SET UP THE OUTPUT CSV FILE
outfile = open('csemploydata.csv', 'w', newline = '') # otherwise blank lines between
outfile_writer = csv.writer(outfile)

# add header row to the data in the csv
fieldnames = ["Rank", "Average Salary", "Num of Positions", "Title"]
outfile_writer.writerow(fieldnames)

# Process each line of data from the text file
for data in infile:
    datarec = re.match(pattern, data)
    print(datarec)
    if datarec:
        outfile_writer.writerow([datarec.group(1), datarec.group(2), datarec.group(3), datarec.group(4)])

outfile.close()
print('ALL DONE')
