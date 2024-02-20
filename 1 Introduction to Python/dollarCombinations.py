# How many possible comvinations of pennies, nickles, dimes, and quarters
# are there that are equivalent to a dollar

quarterValue = .25
dimeValue = .1
nickelValue = .05
pennyValue = .01
dollarValue = 1.0

countLoop = 0
countcombinationsDollar = 0

for q in range(5):
    for d in range(11):
        for n in range(21):
            for p in range(101):
                countLoop += 1
                total = q * quarterValue + d * dimeValue + n * nickelValue + p * pennyValue
                if total == dollarValue:
                    countcombinationsDollar += 1
                    print(q, 'quarters', d, 'dimes', n, 'nickels', p, 'pennies')


print('number of possible combinations', countLoop)
print('\n\nnumber of cominations that change a dollar', countcombinationsDollar)
