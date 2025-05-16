import pandas as pd
import psycopg2
from dotenv import load_dotenv
from os import getenv
load_dotenv()


df = pd.read_excel('sheets/assignment_1_results.xlsx', na_values=['nan', '?', ''])

connection = psycopg2.connect(database = getenv("DATABASE"), 
                        user = getenv("USER"), 
                        host= getenv("HOST"),
                        password = getenv("PASSWORD"),
                        port = getenv("PORT"))
curser =  connection.cursor()

# target indices: 0, 1, 2, 4, 6
# reading the first assignment file to initialize the students table
# and add first problem scores
rows = df.values.tolist()
for row in rows:
    username = row[0]
    student_id = row[1]
    fullname = row[2]
    final_score = row[4]
    judge_score = row[6]
    
    curser.execute(f"INSERT INTO students VALUES('{student_id}', '{username}', '{fullname}')")
    curser.execute(f"INSERT INTO problems(judge_score, final_score ,student_id) VALUES({judge_score}, {final_score}, '{student_id}')")
    
# inseting data of remained assignments (2 to 9) to the problems table
for assignment_number in range(2, 10):
    df = pd.read_excel(f'sheets/assignment_1_results.xlsx', na_values=['nan', '?', ''])
  
    rows = df.values.tolist()
  
    for row in rows:
        username = row[0]
        student_id = row[1]
        fullname = row[2]
        final_score = row[4]
        judge_score = row[6]

    curser.execute(f"INSERT INTO problems(judge_score, final_score ,student_id) VALUES({judge_score}, {final_score}, '{student_id}')")

# commit and closing the connection
connection.commit()
curser.close()
connection.close()