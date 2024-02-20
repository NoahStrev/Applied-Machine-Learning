def build_name(*names):
    full_name = ''
    for n in names:
        full_name += n + ' '
    print(full_name)

build_name('John','Smith')
build_name('John','Q.','Public')
build_name('Alexander','J.', 'Madison', 'III')
build_name('Sam','Hall', 'Jr.')

def minmax(list1):
    max = 0
    min = 10000
    for n in list1:
        
        if n > max:
            max = n
        if n < min:
            min = n
    return min, max

list1 = [1,50,20,30,50,20,60,50,90]
minimum, maximum = minmax(list1)
print('\n\nMin and Max', minimum, maximum)

def findEven():
    i = 100
    evens = []
    while i <= 122:
        evens.append(i)
        i += 2
    return evens

evenNumbers = findEven()
print('\n\nEven Numbers', evenNumbers)
