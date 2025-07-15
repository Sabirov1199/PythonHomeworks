import pandas as pd

# Step 1: Create the DataFrame
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}

sales_and_expenses = pd.DataFrame(data)

# Step 2: Display the DataFrame
print("Sales and Expenses DataFrame:")
print(sales_and_expenses)

# Step 3: Calculate and display the maximum sales and expenses
max_sales = sales_and_expenses['Sales'].max()
max_expenses = sales_and_expenses['Expenses'].max()
print("\nMaximum Sales:", max_sales)
print("Maximum Expenses:", max_expenses)

# Step 4: Calculate and display the minimum sales and expenses
min_sales = sales_and_expenses['Sales'].min()
min_expenses = sales_and_expenses['Expenses'].min()
print("\nMinimum Sales:", min_sales)
print("Minimum Expenses:", min_expenses)

# Step 5: Calculate and display the average sales and expenses
avg_sales = sales_and_expenses['Sales'].mean()
avg_expenses = sales_and_expenses['Expenses'].mean()
print("\nAverage Sales:", avg_sales)
print("Average Expenses:", avg_expenses)


import pandas as pd

# Step 1: Create the DataFrame
data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

expenses = pd.DataFrame(data)

# Step 2: Set 'Category' as the index
expenses = expenses.set_index('Category')

# Step 3: Display the DataFrame
print("Expenses DataFrame:")
print(expenses)

# Step 4: Maximum expense for each category
max_expense = expenses.max(axis=1)
print("\nMaximum expense for each category:")
print(max_expense)

# Step 5: Minimum expense for each category
min_expense = expenses.min(axis=1)
print("\nMinimum expense for each category:")
print(min_expense)

# Step 6: Average expense for each category
avg_expense = expenses.mean(axis=1)
print("\nAverage expense for each category:")
print(avg_expense)

