# pip install pandas
import pandas as pd

mydata = {
    'games' : ["Sep9", "Sep16", "Sep23"],
    'teamscores' : [14, 17, 27]}

print(type(mydata))

mydf = pd.DataFrame(mydata)
print('\n\nMy Data Frame:')
print(mydf)
print(type(mydf))

a = [31, 48, 57]
print('\n\n a is')
print(a)
print(type(a))


myS = pd.Series(a)
print('\n\nmy S')
print(myS)
print(type(myS))

scores = { "Sep 9" : 14, "Sep 16" : 17, "Sep 23" : 27}
myvar = pd.Series(scores)

print(myS)
print(myvar)

print(myS[1])
print(myvar[1])
print(myvar["Sep 16"])
print('\n\n **************************')
print(mydf)

# error: print(mydf[0])
print('\n\nmydf[0]')
print(mydf.loc[0])

x = mydf.loc[0]
print('\n\nx is ', x)
print(type(x))
print()

y = mydf.loc[[0,2]]
print('y is ',y)
print(type(y))

index = ["game 1", "game 2", "game 3"]
mydf2 = pd.DataFrame(mydata, index)
print('\n\nmydf')
print(mydf)
print('\nmydf2')

print(mydf2.loc[["game 1", "game 2"]]) # loc is case sensitive
print(mydf2)
