# MySQL and Multilinear Regression Model

import pandas as pd
# pip install pymysql
# pip install cryptography

import pymysql
# Connect to the database
connection = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user = 'root',
    password = 'root',
    db = 'sqlregress'
    )

pd.options.display.max_columns = None

# Read data into Pandas DataFrame
df = pd.read_sql('SELECT Category,Sub_Category,Segment,Profit FROM super_store;', con=connection)
# print(df.info())

# Reformatting some of my data so that it can be used in my model
# and my model is a Linear Regression model
# so this is a combo of my sql data nad Python types

df['Category'] = df['Category'].astype('category')
df['Category_code'] = df['Category'].cat.codes
   
df['Sub_Category'] = df['Sub_Category'].astype('category')
df['Sub_Category_code'] = df['Sub_Category'].cat.codes

df['Segment'] = df['Segment'].astype('category')
df['Segment_code'] = df['Segment'].cat.codes

df.drop(columns=['Category','Sub_Category', 'Segment'], inplace=True)

X = df.drop(columns=['Profit'])
y = df.Profit

import statsmodels.api as sm
X = sm.add_constant(X)
LRModel = sm.OLS(y,X).fit()
print(LRModel.summary())
