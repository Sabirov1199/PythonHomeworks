import pandas as pd 
df=pd.read_csv(r"C:\Users\Musaffa\Downloads\Telegram Desktop\stackoverflow_qa.csv")

df.head()
#1. Find all questions that were created before 2014

df['creationdate']=pd.to_datetime(df['creationdate'])

df_before_2014=df[df['creationdate']< '2014-01-01']

print(df_before_2014.head())
# 2.Find all questions with a score more than 50

print(df[df['score'] >50].head())
# 3.Find all questions with a score between 50 and 100

print(df[df['score'].between(50,100)].head())
#4. Find all questions answered by Scott Boston

print(df[df['ans_name']=='Scott Boston'])
#5. Find all questions answered by the following 5 users

print(df[df['ans_name'].isin(['Scott Boston','Jason Strimpel','Joe Kington'])])
#6. Find all questions that were created between March, 2014 and October 2014 that were answered by Unutbu and have score less than 5.

q1=df['ans_name']=='Unutbu'
q2=df['score'] <5
q3=df['creationdate'].between('2014-03-01', '2014-10-01')
filtered_df=df[q1 & q2 & q3]

print(filtered_df)
#7. Find all questions that have score between 5 and 10 or have a view count of greater than 10,000

print(df[(df['score'].between(5,10)) | (df['viewcount']>10000)])

titanic_df=pd.read_csv(r"C:\Users\Musaffa\Downloads\Telegram Desktop\titanic.csv")
titanic_df.head()
#1.Select Female Passengers in Class 1 with Ages between 20 and 30: Extract a DataFrame containing female passengers in Class 1 with ages between 20 and 30.

print(titanic_df[(titanic_df['Sex']=='female') & (titanic_df['Pclass']==1) & (titanic_df['Age'].between(20,30))])

#2. Filter Passengers Who Paid More than $100: Create a DataFrame with passengers who paid a fare greater than $100

print(titanic_df[titanic_df['Fare']> 100])
# 3. Select Passengers Who Survived and Were Alone: Filter passengers who survived and were traveling alone (no siblings, spouses, parents, or children).

print(titanic_df[(titanic_df['Survived']==1) & (titanic_df['SibSp']==0) & (titanic_df['Parch']==0)])
# Filter Passengers Embarked from 'C' and Paid More Than $50: Create a DataFrame with passengers who embarked from 'C' and paid more than $50.

print(titanic_df[(titanic_df['Embarked']=='C') & (titanic_df['Fare']> 50)])
# Select Passengers with Siblings or Spouses and Parents or Children: Extract passengers who had both siblings or spouses aboard and parents or children aboard.

print(titanic_df[(titanic_df['SibSp']==1) | (titanic_df['Parch']==1)])
# 6. Filter Passengers Aged 15 or Younger Who Didn't Survive: Create a DataFrame with passengers aged 15 or younger who did not survive.

print(titanic_df[(titanic_df['Age']<=15) & (titanic_df['Survived']==0)])
#7. Select Passengers with Cabins and Fare Greater Than $200: Extract passengers with known cabin numbers and a fare greater than $200.

print(titanic_df[(titanic_df['Cabin'].notna()) & (titanic_df['Fare']>200) ])
#8.Filter Passengers with Odd-Numbered Passenger IDs: Create a DataFrame with passengers whose PassengerId is an odd number.

print(titanic_df[titanic_df['PassengerId'] % 2 !=0])

#9.Select Passengers with Unique Ticket Numbers: Extract a DataFrame with passengers having unique ticket numbers

unique_tickets = titanic_df['Ticket'].value_counts()[titanic_df['Ticket'].value_counts() == 1].index
unique_ticket_df = titanic_df[titanic_df['Ticket'].isin(unique_tickets)]

print(unique_ticket_df)
#10. Filter Passengers with 'Miss' in Their Name and Were in Class 1: Create a DataFrame with female passengers having 'Miss' in their name and were in Class 1.

print(titanic_df[(titanic_df['Name'].str.contains('Miss', case=False, na=False)) & (titanic_df['Pclass']==1)])

