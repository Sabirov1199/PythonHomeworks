import pandas as pd

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)
df1
#1.  Calculate the average grade for each student.
df1['Average_grade']= df1[['Math', 'English', 'Science']].mean(axis=1)
df1
#2. Find the student with the highest average grade

df1.nlargest(1, 'Average_grade')
#3. Create a new column 'Total' representing the total marks obtained by each student.
df1['Total']= df1[['Math', 'English', 'Science']].sum(axis=1)
df1
#4. Plot a bar chart to visualize the average grades in each subject.

import matplotlib.pyplot as plt

Subject_average= df1[['Math', 'English', 'Science']].mean()
plt.figure(figsize=(8,5))
Subject_average.plot(kind='bar', color=['skyblue', 'lightgreen', 'salmon'])
plt.title('Average grades in each subject')
plt.ylabel('Average grade')
plt.ylim(0,100)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

import pandas as pd

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)
#1. Calculate the total sales for each product

grouped=df2.groupby('Date').agg({'Product_A': 'sum', 'Product_B': 'sum', 'Product_C': 'sum'})

grouped['Total_sales']= grouped.sum(axis=1)
grouped
#Find the date with the highest total sales.

top_dates= grouped[grouped['Total_sales']==grouped['Total_sales'].max()]

top_dates
#3. Calculate the percentage change in sales for each product from the previous day.

df2_pct_change=df2[['Product_A', 'Product_B', 'Product_C']].pct_change()*100
df2_pct_change.insert(0,'Date', df2['Date'])
df2_pct_change=df2_pct_change.round(2)
df2_pct_change
#4. Plot a line chart to visualize the sales trends for each product over time.

import matplotlib. pyplot as plt 
plt.figure(figsize=(10,15))
plt.plot(df2['Date'], df2['Product_A'], marker='o', label='Product A')
plt.plot(df2['Date'], df2['Product_B'], marker='o', label='Product B')
plt.plot(df2['Date'], df2['Product_C'], marker='o', label='Product C')

plt.title('Sales trends over time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()

import pandas as pd

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)
df3.groupby('Department')['Salary'].mean()
df3.groupby(['Employee_ID', 'Name'])['Experience (Years)'].max()
df3
#3.  Create a new column 'Salary Increase' representing the percentage increase in salary from the minimum salary in the dataframe.

df3['Salary Increase']=((df3['Salary']-df3['Salary'].min())/ df3['Salary'].min())*100

#4 Plot a bar chart to visualize the distribution of employees across different departments.

import matplotlib.pyplot as plt 

dep_counts= df3['Department'].value_counts()
plt.figure(figsize=(8,5))
plt.bar(dep_counts.index, dep_counts.values, color='skyblue')

plt.title('Employee Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
import pandas as pd

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)
#1. Calculate the total revenue from all orders.

df4['Total_Price'].sum()
#2. Find the most ordered product.

product_quantity=df4.groupby('Product')['Quantity'].sum()
most_ordered = product_quantity.idxmax()
most_ordered
#3 Calculate the average quantity of products ordered.

Average_quanity= df4['Quantity'].mean()
Average_quanity
#4. Plot a pie chart to visualize the distribution of sales across different products.

import matplotlib.pyplot as plt

sales_by_product= df4.groupby('Product')['Total_Price'].sum()

plt.figure(figsize=(7,7))
plt.pie(sales_by_product, labels=sales_by_product.index, autopct='%1.1f%%', startangle=140, colors=['#66c2a5', '#fc8d62', '#8da0cb'])
plt.title('Sales distribution by product')
plt.axis('equal')
plt.tight_layout()
plt.show()




