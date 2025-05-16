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

curser = connection.cursor()

# Use this query if you want to have the details of each assignment(problem)
query1 = """
SELECT student_id, fullname, final_score, total FROM
    students NATURAL JOIN problems NATURAL JOIN 
        (SELECT student_id, SUM(final_score) / 9 as total FROM
            problems GROUP BY (student_id)) ORDER BY student_id;
"""

# Use this query if you only need the student_id, name and the final score
query2 = """
SELECT student_id, fullname, total FROM
    (SELECT student_id, fullname, final_score, total FROM
        students NATURAL JOIN problems NATURAL JOIN 
            (SELECT student_id, SUM(final_score) / 9 as total FROM
                problems GROUP BY (student_id)))
GROUP BY (student_id, fullname, total) ORDER BY student_id;
"""

curser.execute(query1);
data = curser.fetchall()
for d in data:
    ws.append(d)
    
wb.save("results.xlsx")