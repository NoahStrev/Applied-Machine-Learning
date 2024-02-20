def addmultem(*nums):
    zsum = 0
    prod = 1
    for x in nums:
        zsum += x
        prod *= x
    return zsum, prod

# get result in tuple form
result = addmultem(3, 8, 12, 24)
print(result)
print(type(result))

# unpack the tuple
total, product = addmultem(3, 8, 12, 24)
print(total)
print(product)

def funone():
    return 1, 2, 3

print(funone())

# Accessing elements of a list and elements of a tuple
list1 = [1,2,3,4]
tuple1 = (1,2,3,4)

# print second element in each
print(list1[1], tuple1[1])

list1[1] = 2
# tuple1[1] = 9

list2 = list1
tuple2 = tuple1

print('\n\nCopying')
print(list2, tuple2)

tuple3 = tuple1 + tuple2
print('\n\nAdding Tuples:')
print(tuple3)

print('\n\nSlicing:')
tuple4 = tuple3[3:-1]
print(tuple4)

tuple5 = tuple3[3:-2]
print(tuple5)

tuple6 = tuple3[:-1]
print(tuple6)

tuple7 = tuple3[0:-1]
print(tuple7)

tuple8 = tuple3[2:5]
print(tuple8)


list3 = list1 + list2
print('\n\nAdding Lists:')
print(list3)

print('\n\nSlicing:')
list4 = list3[3:-1]
print(list4)

list5 = list3[3:-2]
print(list5)

list6 = list3[:-1]
print(list6)

list7 = list3[0:-1]
print(list7)

list8 = list3[2:5]
print(list8)
