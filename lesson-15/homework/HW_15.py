import sqlite3


conn = sqlite3.connect('animals.db')  
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Roster (
        Name TEXT,
        Species TEXT,
        Age INTEGER
    )
''')

print("Database and Roster table created successfully.")


conn.commit()
conn.close()

--
import sqlite3


conn = sqlite3.connect('animals.db')
cursor = conn.cursor()


data = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]

cursor.executemany('INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)', data)


conn.commit()
conn.close()

print("Data inserted successfully into Roster table.")

--
import sqlite3


conn = sqlite3.connect('animals.db')
cursor = conn.cursor()


cursor.execute('''
    UPDATE Roster
    SET Name = 'Ezri Dax'
    WHERE Name = 'Jadzia Dax'
''')


conn.commit()
conn.close()

print("Name updated successfully.")
---
import sqlite3


conn = sqlite3.connect('animals.db')
cursor = conn.cursor()


cursor.execute('''
    SELECT Name, Age FROM Roster
    WHERE Species = 'Bajoran'
''')


results = cursor.fetchall()
for name, age in results:
    print(f"Name: {name}, Age: {age}")


conn.close()

