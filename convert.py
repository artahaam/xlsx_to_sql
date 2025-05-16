import pandas as pd
import psycopg2
from dotenv import load_dotenv
from os import getenv
load_dotenv()

connection = psycopg2.connect(database = getenv("DATABASE"), 
                        user = getenv("USER"), 
                        host= getenv("HOST"),
                        password = getenv("PASSWORD"),
                        port = getenv("PORT"))

df = pd.read_excel('sheets/assignment_1_results.xlsx', na_values=['nan', '?', ''])

columns = df.columns.ravel()
username = columns[0]

curser =  connection.cursor()

# target indices: 0, 1, 2, 4, 6
rows = df.values.tolist()
for row in rows:
    username = row[0]
    student_id = row[1]
    fullname = row[2]
    final_score = row[4]
    judge_score = row[6]
    
    curser.execute(f"INSERT INTO students VALUES('{student_id}', '{username}', '{fullname}')")
    curser.execute(f"INSERT INTO problems(judge_score, final_score ,student_id) VALUES({judge_score}, {final_score}, '{student_id}')")
    
connection.commit()
curser.close()
connection.close()