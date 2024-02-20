def triMult():
    i = 3
    while i <= 33:
        print(i)
        i += 3

print('Running through a loop')
triMult()

def listTriMult():
    i = 3
    triList = []
    while i <= 33:
        triList.append(i)
        i += 3
    return triList

print('\nLooping through a list')
newList = listTriMult()
print(newList)

def listTriMultOther():
    triList = [n for n in range(3,34,3)]
    print(triList)

print('\nAnother way of looping through a list')
listTriMultOther()

print_multis3 = listTriMultOther
print('\nAlias example')
print_multis3()

def swapTuple(tuple1, tuple2):
    temptuple = tuple1
    tuple1 = tuple2
    tuple2 = temptuple
    return tuple1,tuple2
    
tuple1 = (14,5)
tuple2 = (9,11)
print('\nTuple1 and Tuple2\n', tuple1, tuple2)
tuple1, tuple2 = swapTuple(tuple1, tuple2)
print('\nSwapped\n', tuple1, tuple2)
# Can also do
# tuple1, tuple2 = tuple2, tuple1


def findFiftyTuple(tuple1):
    count = 0
    for i in tuple1:
        if i == 50:
            count = count + 1
    return count
        
tuple1 = (10,50,20,30,50,20,60,50,90)
counter = findFiftyTuple(tuple1)
print('\nNumber of Fifties in the tuple:', counter)


def findFiftyList(list1):
    count = 0
    for i in list1:
        if i == 50:
            count = count + 1
    return count

list1 = [10,50,20,30,50,20,60,50,90]
counter2 = findFiftyList(list1)
print('\nNumber of Fifties in the list:', counter2)

list = [n for n in list1 if n == 50]
print(len(list))
