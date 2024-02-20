# PROBLEM ONE

def listPrimes(a, b):
    primeList = []
    if a < 1:
        print("The lowerbound number given was invalid, try again") # Making sure the lowerbound is valid
        exit(1) # Wasn't specified what to do with bad numbers, so I just kill it the program
    elif a == 1:
        a = a + 1
        
    if b < a: # making sure that the upperbound is valid
        print("The lowerbound number was higher than the upperbound number,try again with different parameters.")
        exit(1) # Wasn't specified what to do with bad numbers, so I just kill it the program
        
    for i in range(a, b + 1): # +1 because the end is not inclusive
        for j in range (2, i): # creating the loop to check if a number is prime 
            if (i % j) == 0:   # checking if the number is not prime
                break
            else:
                if i not in primeList: # seeing if the number is in the list
                    primeList.append(i) # adding the prime numbers to a list
    return primeList

primeNumbers = listPrimes(1,11)
print(primeNumbers)


# PROBLEM 2

def fibonacci(n):
    fibonacciList = []
    previous_num, temp, highest_num = 0, 0, 1
    i = 0 # creating the variables
    
    fibonacciList.append(previous_num) # putting the zero in the list
    if n < 3: # making sure the list is long enough
        print("The number entered was not higher than 2, please try again") 
    while i <= n - 2: # setting up the loop length
        fibonacciList.append(highest_num) # adding the numbers to the list

        temp = highest_num + previous_num 
        previous_num = highest_num 
        highest_num = temp # setting the numbers to their new values
        i += 1
    return fibonacciList

fibonacciNumbers = fibonacci(8)
print(fibonacciNumbers)


# PROBLEM 3

def listAndTuple(list1, tuple1):
    combinedList = []
    if len(list1) > 0: # checking if the list is populated
        for i in list1: # adding each part of the list to the combined list
            combinedList.append(i)
    if len(tuple1) > 0: # checking if the tuple is populated
        for i in tuple1: # adding each part of the tuple to the combined list
            combinedList.append(i)
    return combinedList

list1 = ['Soccer', 10, 50]
tuple1 = (15, 'Hello')

combined = listAndTuple(list1, tuple1)
print(combined)
