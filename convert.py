import pandas as pd
import psycopg2
from dotenv import load_dotenv
from os import getenv
load_dotenv()

# Creating a connection to postgresql
connection = psycopg2.connect(database = getenv("DATABASE"), 
                        user = getenv("USER"), 
                        host= getenv("HOST"),
                        password = getenv("PASSWORD"),
                        port = getenv("PORT"),
                        options='-c client_encoding=UTF8')

cursor = connection.cursor()

# extracting student data and inserting to the students table in the database
df = pd.read_excel('fake_data0.xlsx', na_values=['nan', '?', ''])

rows = df.values.tolist()

for row in rows:
    student_id = row[0]
    fullname = row[1]

    cursor.execute(f"INSERT INTO students VALUES('{student_id}', '{fullname}')")

connection.commit()

    
# extracting problem assignments data and inserting to the problems table in the database
for assignment_number in range(1, 4):

    df = pd.read_excel(f'fake_data{assignment_number}.xlsx', na_values=['nan', '?', ''])
  
    rows = df.values.tolist()
  
    for row in rows:
        student_id = row[0]

        # Taking care of nan (null) values 
        final_score = str(row[2]) if str(row[2]) != "nan" else 0
        cursor.execute(f"INSERT INTO problems(final_score, student_id) VALUES({final_score}, '{student_id}')")

connection.commit()

        
# commit and closing the connection
cursor.close()
connection.close()