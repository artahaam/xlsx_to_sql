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
df = pd.read_excel('sheets/students.xlsx', na_values=['nan', '?', ''])

rows = df.values.tolist()
print(rows)
for row in rows:
    print(row)
    username = row[0]
    student_id = row[1]
    fullname = row[2]

    cursor.execute(f"INSERT INTO students VALUES('{student_id}', '{username}', '{fullname}')")

connection.commit()

    
# extracting problem assignments data and inserting to the problems table in the database
for assignment_number in range(1, 10):

    df = pd.read_excel(f'sheets/assignment_{assignment_number}_results.xlsx', na_values=['nan', '?', ''])
  
    rows = df.values.tolist()
  
    for row in rows:
        username = row[0]
        student_id = row[1]
        fullname = row[2]
        
        # Taking care of nan (null) values 
        final_score = str(row[4]) if str(row[4]) != "nan" else 0
        judge_score = str(row[6]) if str(row[6]) != "nan" else 0
        cursor.execute(f"INSERT INTO problems(judge_score, final_score, student_id) VALUES({judge_score}, {final_score}, '{student_id}')")

connection.commit()

        
# commit and closing the connection
cursor.close()
connection.close()