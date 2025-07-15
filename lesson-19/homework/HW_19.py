### Homework Assignment 1: Analyzing Sales Data
import pandas as pd 
import numpy as np 
df=pd.read_csv(r"C:\Users\Musaffa\Downloads\Telegram Desktop\sales_data.csv")
df.head()
#1. 

result=df.groupby('Category').agg({'Quantity': 'sum'})
print(result)
Avg_price=df.groupby('Category').agg({'Price': 'mean'})
print(Avg_price)
max_quant=df.groupby('Category').agg({'Quantity': 'max'})
print(max_quant)
#2. Identify the top-selling product in each category based on the total quantity sold.

result=df.groupby(['Category', 'Product']).agg({'Quantity' : 'sum'})

top_products=result.sort_values('Quantity', ascending=False).groupby('Category'). head(1)
print(top_products)
#3. Find the date on which the highest total sales (quantity * price) occurred.

df['Date']= pd.to_datetime(df['Date'])
df['Sales']=df['Quantity'] * df['Price']

result=df.groupby('Date').agg({'Sales' : 'max'})
max_sales= result.sort_values('Sales', ascending=False).groupby('Date').head(1)
print(max_sales.head(1))

### Homework Assignment 2: Examining Customer Orders
df=pd.read_csv(r"C:\Users\Musaffa\Downloads\Telegram Desktop\customer_orders.csv")
df.head()
result=df.groupby('CustomerID')['Quantity'].count()
under_20= result[result < 20].index
filtered_df= df[df['CustomerID']. isin(under_20)]
print(filtered_df)
#2. Identify customers who have ordered products with an average price per unit greater than $120.

result=df.groupby('CustomerID').agg({'Price': 'mean'})
print(result)
filtered_df=result[result>120]
print(filtered_df)
#3. Find the total quantity and total price for each product ordered, and filter out products that have a total quantity less than 5 units.

result=df.groupby('Product'). agg({'Quantity' : 'sum', 'Price' :'sum'})
print(result.head())

filtered_df=result[result['Quantity'] < 5]
print(filtered_df)
import sqlite3
import pandas as pd 
#### Homework Assignment 3: Population Salary Analysis
conn = sqlite3.connect("population.db")
population_df = pd.read_sql_query("SELECT * FROM population", conn)
salary_bands = pd.DataFrame({
    'Salary Band': ['Low', 'Medium', 'High', 'Very High'],
    'Min': [0, 50000, 100000, 150000],
    'Max': [49999, 99999, 149999, float('inf')]
})

def classify_salary(salary):
    for _, row in salary_bands.iterrows():
        if row['Min'] <= salary <= row['Max']:
            return row['Salary Band']
    return 'Unknown'
population_df['Salary Band'] = population_df['salary'].apply(classify_salary)
state_summary = population_df.groupby(['state', 'Salary Band']).agg(
    Population=('salary', 'count'),
    Average_Salary=('salary', 'mean'),
    Median_Salary=('salary', 'median')
).reset_index()
state_totals = population_df.groupby('state')['salary'].count().rename('TotalStatePop').reset_index()
state_summary = state_summary.merge(state_totals, on='state')
state_summary['Percentage'] = (state_summary['Population'] / state_summary['TotalStatePop']) * 100
state_summary.drop(columns='TotalStatePop', inplace=True)
state_summary.to_excel("state_salary_band_analysis.xlsx", index=False)
print(state_summary.head(10))







