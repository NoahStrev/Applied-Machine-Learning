# Notes - Intro to Python

# 3 + 5 = 8
x = 3 + 5
print(x , "\n")


# 5 - 3 = 2
x = 5 - 3
print(x, "\n")


# 3 * 5 = 15
x = 3 * 5
print(x, "\n")


# 3 / 5 = .6
x = 3 / 5
print(x, "\n")


# 13 // 2 = 6
x = 3 ** 3
print(x, "\n")


# 3 ** 3 = 27
x = 3 ** 3
print(x, "\n")


# if x > 3:
# Remember to use : not {
# elif x < 3:


# for v in range (1, 5):
# print(v)
# uses the first letter, stops at the second
# outputs 1 2 3 4

for v in range (1, 5):
    print(v)
print("\n")


# PRINTS THE VALUES 3 6 5
mylist = [3, 6, 5]
for m in mylist:
    print(m)
print("\n")


# BREAK STOPS THE LOOP
# continue restarts the loop at the next iteration, so everything after it is not seen
i = 1
while i < 7:
    print(i)
    i += 1
    if i == 5:
        break
    if i == 2:
        continue
        print("This is not seen")
print("\n")

# def name(variable name(s))
# def fun(x, y, z) (The method)
# fun(a, b, c) (Calling the method)


## EXAMPLE FUNCTION
# def sum(nums):
#     total = 0
#     for x in nums:
#         total += nums
#     return total


## ARBITRARY EXAMPLE
def xyz(**info):
    print(info['fname'], info['lname'], info['gpa'])
    print("\n")

xyz(fname = 'Joe', lname = 'Shmoe', gpa = 3.5)


## ANOTHER ARBITRARY EXAMPLE
## ALSO USES HASMAP
def mykwafen(**info):
    all_vals = ""
    for k,v in info.items():
        all_vals += str(k) + '->' + str(v) + ' '
    print(all_vals)
    print("\n")

mykwafen(fname = 'Joe', gpa = 3.5)


## ANOTHER EXAMPLE
## The parameter and argument NAMES need to be the same, but they don't have to be in the same order
def printname(gpa, lname, fname):
    print(fname, lname, gpa)
    print("\n")

printname(fname = 'Ethan', lname = 'Peq', gpa = 3.9)


# SEARCHING A LIST FOR A VALUE
list_toppings = ['sausage', 'pepperoni', 'bacon']
if 'bacon' in list_toppings:
    print('Hello')
    print("\n")

# (_, _) = tuplies
# [_, _] = list
# obj.array turns list -> tuple


##  YOU CAN'T ITTERATE THROUGH A LIST
## THIS DOES NOT WORK
# list[(3,8,1),(10, 2, 12)]
# list.array()
# for l in list:
#     print(l)
# print("\n")


# USING LIBRARIES
import math
y = math.sqrt(4)
print(y)


## CAN ALSO DO THIS
# from math import sqrt
# y = sqrt(4)

# TAKING IN INPUTS
username = input("Enter your username:")

