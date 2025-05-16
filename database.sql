-- Active: postgres@@127.0.0.1@5432@xlsx_to_sql
CREATE TABLE students(
    student_id VARCHAR(9) PRIMARY KEY,
    fullname VARCHAR(60),
)


CREATE TABLE problems(
    final_score INTEGER,
    student_id VARCHAR(9) REFERENCES students(student_id)
)
