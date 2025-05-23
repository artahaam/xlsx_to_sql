from os import getenv

import psycopg2
from openpyxl import Workbook
from dotenv import load_dotenv
load_dotenv()

# Create and managing the xlsx file
wb = Workbook()
ws = wb.active
ws.title = "results.xlsx"
ws.append(["student_id", "fullname", "score", "total"])
wb.save("results.xlsx")

connection = psycopg2.connect(database = getenv("DATABASE"), 
                        user = getenv("USER"), 
                        host= getenv("HOST"),
                        password = getenv("PASSWORD"),
                        port = getenv("PORT"),
                        options='-c client_encoding=UTF8')

cursor = connection.cursor()

# Use this query if you want to have the details of each assignment(problem)
query1 = """
SELECT student_id, fullname, final_score, total FROM
    students NATURAL JOIN problems NATURAL JOIN 
        (SELECT student_id, SUM(final_score) as total FROM
            problems GROUP BY (student_id)) ORDER BY student_id;
"""

# Use this query if you only need the student_id, name and the final score
query2 = """
SELECT student_id, fullname, total FROM
    (SELECT student_id, fullname, final_score, total FROM
        students NATURAL JOIN problems NATURAL JOIN 
            (SELECT student_id, SUM(final_score) as total FROM
                problems GROUP BY (student_id)))
GROUP BY (student_id, fullname, total) ORDER BY student_id;
"""

# Create resluts table
crate_table = """
CREATE TABLE results(
    id SERIAL PRIMARY KEY,
    student_id VARCHAR(9) REFERENCES students(student_id),
    fullname VARCHAR(60),
    score INTEGER,
    total INTEGER
    )
"""
cursor.execute(crate_table)
connection.commit()
cursor.execute(query1);

data = cursor.fetchall()
for d in data:
    student_id, fullname, score, total = d
    print(student_id, fullname, score, total)
    
    # Add data as rows to the xlsx file
    ws.append(d)
    
    # Insert into resluts table
    cursor.execute(f"""
                INSERT INTO results(student_id, fullname, score, total) VALUES('{student_id}', '{fullname}', {score}, {total})
                """)
    
wb.save("results.xlsx")
connection.commit()


cursor.close()
connection.close()
