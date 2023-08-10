import psycopg2
import pandas as pd

#url='https://raw.githubusercontent.com/jchadwich/PSS/main/vdot.csv'

conn = psycopg2.connect(
    database="aprecisioncompanydb",user="postgres",password="infrastructure",host="127.0.0.1",port="5432"
)
conn.autocommit=True
cursor=conn.cursor()

# Create sorted list of id values to get most recent id for cursor.execute
cursor.execute('''SELECT id from __templates__''')
i = cursor.fetchall()
n=0 # Index variable
idList = []
for item in i:
    # Pull int values from lists
    idList.append(i[n][0])
    n += 1
print(idList[-1])

cursor.execute(f'''SELECT * from __templates__ WHERE id = {idList[-1]}''') # Most recent entry only

result=cursor.fetchall()

print(result)

#csvFile = result[1]
#print(pd.read_csv(csvFile))


conn.close()