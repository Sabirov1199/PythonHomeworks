import sqlite3
import pandas as pd 
conn=sqlite3.connect('chinook.db')
tables=pd.read_sql("Select name From sqlite_master where type='table';" , conn)
print(tables)
#1. Find the total amount spent by each customer on purchases (considering invoices).
query= """
SELECT c.customerId, c.FirstName, SUM(i.Total) AS total_spent
FROM Customer c
JOIN Invoice i ON c.customerId = i.customerId
GROUP BY c.customerId, c.FirstName
"""

result=pd.read_sql(query, conn)
print(result.head())
conn.close()
conn = sqlite3.connect('chinook.db')
#2. Identify the top 5 customers with the highest total purchase amounts.


query= """
SELECT c.customerId, c.FirstName, SUM(i.Total) AS total_spent
FROM Customer c
JOIN Invoice i ON c.customerId = i.customerId
GROUP BY c.customerId, c.FirstName
order by total_spent desc
Limit 5
"""

top_customers=pd.read_sql(query, conn)
print(top_customers)

conn.close()
#3. Display the customer ID, name, and the total amount spent for the top 5 customers.


conn = sqlite3.connect('chinook.db')

query= """
SELECT c.customerId, c.FirstName, SUM(i.Total) AS total_spent
FROM Customer c
JOIN Invoice i ON c.customerId = i.customerId
GROUP BY c.customerId, c.FirstName
order by total_spent desc
Limit 5
"""

top_customers=pd.read_sql(query, conn)
print(top_customers)

conn.close()
tables=pd.read_sql("Select name From sqlite_master where type='table';" , conn)
print(tables)
#### Album vs. Individual Track Purchases:
#Determine the percentage of customers who prefer to buy individual tracks instead of full albums.

import sqlite3
import pandas as pd
conn = sqlite3.connect('chinook.db')
query= """
with cte1 as (
Select AlbumId, COUNT(*) as total_tracks
from Track
group by AlbumId
), 

cte2 as (
Select il.InvoiceId, t.AlbumId, count(*) as tracks_bought
from InvoiceLine il
join Track t on il.TrackId=t.TrackId
group by il.InvoiceId, t.AlbumId
),

cte3 as (
Select i.CustomerId
from cte2 c2
join cte1 c1
on c2.AlbumId=c1.AlbumId
join Invoice i on i.InvoiceId= c2.InvoiceId
where c2.tracks_bought=c1.total_tracks
group by i.CustomerId
), 
cte4 as (
Select CustomerId from Customer
)

Select 
round(100.0 * 
(Select count(*) from cte4 where CustomerId not in (Select CustomerId from cte3))
/
(Select count(*) from cte4), 2
) as percent_track_buyers

"""
percentage=pd.read_sql(query, conn)
print(percentage)
conn.close()
query = """

WITH AlbumTrackCounts AS (
    SELECT AlbumId, COUNT(*) AS total_tracks
    FROM Track
    GROUP BY AlbumId
),
InvoiceAlbumTrackCounts AS (
    SELECT i.InvoiceId, c.CustomerId, t.AlbumId, COUNT(*) AS tracks_bought
    FROM InvoiceLine il
    JOIN Track t ON il.TrackId = t.TrackId
    JOIN Invoice i ON il.InvoiceId = i.InvoiceId
    JOIN Customer c ON i.CustomerId = c.CustomerId
    GROUP BY i.InvoiceId, c.CustomerId, t.AlbumId
),
FullAlbumPurchases AS (
    SELECT DISTINCT CustomerId
    FROM InvoiceAlbumTrackCounts iatc
    JOIN AlbumTrackCounts atc ON iatc.AlbumId = atc.AlbumId
    WHERE iatc.tracks_bought = atc.total_tracks
),
CustomerPreference AS (
    SELECT 
        c.CustomerId,
        CASE 
            WHEN fap.CustomerId IS NOT NULL THEN 'album_buyers'
            ELSE 'track_buyers'
        END AS preference
    FROM Customer c
    LEFT JOIN FullAlbumPurchases fap ON c.CustomerId = fap.CustomerId
),
Summary AS (
    SELECT 
        preference,
        COUNT(*) AS customer_count
    FROM CustomerPreference
    GROUP BY preference
)
SELECT 
    preference,
    customer_count,
    ROUND(100.0 * customer_count / (SELECT COUNT(*) FROM Customer), 2) AS percentage
FROM Summary
ORDER BY percentage DESC;



"""
import sqlite3
import pandas as pd

conn = sqlite3.connect('chinook.db')




summary = pd.read_sql(query, conn)
print(summary)

conn.close()





